import json
import logging
import uuid

import boto3
from botocore.exceptions import ClientError

from ..constants import WAIT_SECONDS
from ..schemas import CSVRow
from ..util.service_util import create_archive_job_message
from ..config import (
    THINGS_REPORT_JOB_QUEUE,
    AWS_REGION,
    THINGS_REPORT_ARCHIVE_JOB_QUEUE,
    THINGS_REPORT_JOB_DLQ,
)
from ..util.s3_util import (
    write_data_to_csv,
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
        self.report_job_dlq = self.sqs.Queue(f"{THINGS_REPORT_JOB_DLQ}.fifo")
        self.report_archive_job_queue = self.sqs.Queue(
            f"{THINGS_REPORT_ARCHIVE_JOB_QUEUE}.fifo"
        )

    async def _process_messages(self, message_body: dict) -> None:
        report_name = message_body["ReportName"]
        user_id = message_body["UserId"]
        job_index = message_body["JobIndex"]
        start_timestamp = message_body["StartTimestamp"]
        end_timestamp = message_body["EndTimestamp"]
        archive_report = message_body["ArchiveReport"]

        (
            report_job_file_path,
            report_job_upload_path,
            _,
        ) = create_csv_report_job_path(
            user_id, report_name, job_index, start_timestamp, end_timestamp
        )

        if archive_report == "True":
            message_id = str(uuid.uuid4())

            archive_message = create_archive_job_message(
                message_id,
                user_id,
                report_name,
                job_path=report_job_file_path,
                job_upload_path=report_job_upload_path,
            )

            await self.produce([archive_message])
        else:
            await self.upload_csv_job(
                user_id,
                report_name,
                job_index,
                start_timestamp,
                end_timestamp,
            )

    async def poll(self) -> None:
        log.debug("Polling...")

        while True:
            await self.consume()

    async def consume(self) -> None:
        try:
            job_messages = self.report_job_queue.receive_messages(
                MessageAttributeNames=["All"],
                MaxNumberOfMessages=10,
                WaitTimeSeconds=WAIT_SECONDS,
            )

            if len(job_messages) > 0:
                for job_message in job_messages:
                    message_body = json.loads(job_message.body)

                    job_message.delete()

                    await self._process_messages(message_body)

        except ClientError as error:
            log.error(f"Couldn't receive report_job_queue messages error {error}")

            raise error

    async def upload_csv_job(
        self, user_id, report_name, job_index, start_timestamp, end_timestamp
    ) -> None:
        report_job_file_path, report_job_upload_path, report_job_filename = (
            create_csv_report_job_path(
                user_id,
                report_name,
                job_index,
                start_timestamp,
                end_timestamp,
            )
        )

        try:
            result: list[CSVRow] = await create_csv_rows(
                user_id, start_timestamp, end_timestamp
            )

            write_data_to_csv(report_job_file_path, report_job_filename, result)

            s3_upload_csv(
                self.s3_client,
                f"{report_job_file_path}/{report_job_filename}",
                f"{report_job_upload_path}/{report_job_filename}",
            )
        except ClientError as error:
            log.error(f"S3 client upload error: {error}")

            raise error

    async def produce(self, archive_job_messages: list[dict]) -> list[dict]:
        log.debug("Send archive job message")

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
