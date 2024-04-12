import json
import logging
import uuid
from typing import Any

import boto3
from botocore.exceptions import ClientError

from ..schemas import ThingPayload
from ..config import THINGS_REPORT_JOB_QUEUE, AWS_REGION
from ..crud import find_thing_payloads
from ..util.s3_util import (
    create_csv_writer,
    create_csv_rows,
    create_csv_report_job_path,
)
from ..util.service_util import create_archive_job_message

log = logging.getLogger("things_report_job_service")


class ThingsReportJobService:
    def __init__(self):
        self.sqs = boto3.resource("sqs", region_name=AWS_REGION)
        # self.s3_client = boto3.client("s3", region_name=AWS_REGION)
        self.report_job_queue = self.sqs.Queue(f"{THINGS_REPORT_JOB_QUEUE}.fifo")
        # self.report_archive_job_queue = self.sqs.Queue(f"{THINGS_REPORT_ARCHIVE_JOB_QUEUE}.fifo")

    async def poll(self):
        while True:
            await self.consume()

    async def consume(self):
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

                    report_job_path, report_job_filename = create_csv_report_job_path(
                        user_id, report_name, job_index, start_timestamp, end_timestamp
                    )

                    await create_csv_writer(
                        report_job_path, report_job_filename, user_id
                    )

                    # job_path_prefix = (
                    #     f"{message_body["UserId"]}/{message_body["ReportName"]}"
                    # )
                    # job_path_suffix = f"{message_body["StartTimestamp"]}-{message_body["EndTimestamp"]}"
                    # job_path_prefix = (
                    #     f"{message_body["UserId"]}/{message_body["ReportName"]}"
                    # )
                    # job_path_suffix = f"{message_body["StartTimestamp"]}-{message_body["EndTimestamp"]}"

                    # self.produce(archive_message)

                    job_message.delete()
        except ClientError as error:
            log.error(f"Couldn't receive report_job_queue messages error {error}")

            raise error

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
