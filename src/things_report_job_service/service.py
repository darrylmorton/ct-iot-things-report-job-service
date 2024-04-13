import json
import logging
from typing import Any

import boto3
from botocore.exceptions import ClientError

from ..config import THINGS_REPORT_JOB_QUEUE, AWS_REGION, THINGS_REPORT_ARCHIVE_JOB_QUEUE
from ..util.s3_util import (
    create_csv_writer,
    create_csv_rows,
    create_csv_report_job_path,
    s3_upload_csv,
)

log = logging.getLogger("things_report_job_service")


class ThingsReportJobService:
    def __init__(self):
        self.sqs = boto3.resource("sqs", region_name=AWS_REGION)
        self.s3_client = boto3.client("s3", region_name=AWS_REGION)
        self.report_job_queue = self.sqs.Queue(f"{THINGS_REPORT_JOB_QUEUE}.fifo")
        # self.report_archive_job_queue = self.sqs.Queue(f"{THINGS_REPORT_ARCHIVE_JOB_QUEUE}.fifo")

    async def poll(self):
        log.debug(f"Polling...")

        while True:
            await self.consume()

    async def consume(self):
        log.debug(f"Consuming...")

        try:
            job_messages = self.report_job_queue.receive_messages(
                MessageAttributeNames=["All"],
                MaxNumberOfMessages=10,
                WaitTimeSeconds=5,
            )

            if len(job_messages) > 0:
                for job_message in job_messages:
                    message_body = json.loads(job_message.body)

                    report_name = message_body["ReportName"]
                    user_id = message_body["UserId"]
                    job_index = message_body["JobIndex"]
                    start_timestamp = message_body["StartTimestamp"]
                    end_timestamp = message_body["EndTimestamp"]

                    try:
                        await self.upload_csv_job(
                            user_id,
                            report_name,
                            job_index,
                            start_timestamp,
                            end_timestamp,
                        )
                    except ClientError as err:
                        log.error(f"s3 client error: {err}")
                    finally:
                        job_message.delete()

                    # job_path_prefix = (
                    #     f"{message_body["UserId"]}/{message_body["ReportName"]}"
                    # )
                    # job_path_suffix = f"{message_body["StartTimestamp"]}-{message_body["EndTimestamp"]}"
                    # job_path_prefix = (
                    #     f"{message_body["UserId"]}/{message_body["ReportName"]}"
                    # )
                    # job_path_suffix = f"{message_body["StartTimestamp"]}-{message_body["EndTimestamp"]}"

                    # self.produce(archive_message)

        except ClientError as error:
            log.error(f"Couldn't receive report_job_queue messages error {error}")

            raise error

    async def upload_csv_job(
        self, user_id, report_name, job_index, start_timestamp, end_timestamp
    ):
        (
            report_job_file_path,
            report_job_upload_path,
            report_job_filename,
        ) = create_csv_report_job_path(
            user_id,
            report_name,
            job_index,
            start_timestamp,
            end_timestamp,
        )

        result = await create_csv_rows(user_id)

        create_csv_writer(report_job_file_path, report_job_filename, result)

        return s3_upload_csv(
            self.s3_client,
            f"{report_job_file_path}/{report_job_filename}",
            f"{report_job_upload_path}/{report_job_filename}",
        )

        # log.info(f"S3 RESPONSE {response}")

    def produce(self, archive_job_messages: Any) -> Any:
        try:
            if len(archive_job_messages) > 0:
                self.report_archive_job_queue.send_messages(
                    Entries=archive_job_messages
                )

            return archive_job_messages
        except ClientError as error:
            log.error(
                f"Couldn't receive report_archive_job_queue messages error {error}"
            )

            raise error
