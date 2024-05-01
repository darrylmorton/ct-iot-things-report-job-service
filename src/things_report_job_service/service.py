import json
import uuid

import boto3
import requests
from botocore.exceptions import ClientError

from schemas import ThingPayload
from util.service_util import create_archive_job_message, get_thing_payloads
from config import (
    THINGS_REPORT_JOB_QUEUE,
    AWS_REGION,
    THINGS_REPORT_ARCHIVE_JOB_QUEUE,
    THINGS_REPORT_JOB_DLQ,
    QUEUE_WAIT_SECONDS,
    get_logger,
)
from util.s3_util import (
    write_data_to_csv,
    create_csv_rows,
    create_csv_report_job_path,
    s3_upload_csv,
)

log = get_logger()


class ThingsReportJobService:
    def __init__(self):
        log.debug("initializing ThingsReportJobService...")

        self.sqs = boto3.resource("sqs", region_name=AWS_REGION)
        self.s3_client = boto3.client("s3", region_name=AWS_REGION)
        self.report_job_queue = self.sqs.Queue(f"{THINGS_REPORT_JOB_QUEUE}.fifo")
        self.report_job_dlq = self.sqs.Queue(f"{THINGS_REPORT_JOB_DLQ}.fifo")
        self.report_archive_job_queue = self.sqs.Queue(
            f"{THINGS_REPORT_ARCHIVE_JOB_QUEUE}.fifo"
        )

    async def _process_messages(self, message_body: dict) -> None:
        log.debug("Processing job message...")

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
            response_body = get_thing_payloads(start_timestamp, end_timestamp)
            log.info(f"UPLOAD CSV JOB {response_body=}")

            # response_body = json.dumps(response_body)

            await self.upload_csv_job(
                user_id,
                report_name,
                job_index,
                start_timestamp,
                end_timestamp,
                response_body,
            )

    async def poll(self) -> None:
        log.debug("Polling for job messages...")

        while True:
            await self.consume()

    async def consume(self) -> None:
        log.debug("Consuming job messages...")

        try:
            job_messages = self.report_job_queue.receive_messages(
                MessageAttributeNames=["All"],
                MaxNumberOfMessages=10,
                WaitTimeSeconds=QUEUE_WAIT_SECONDS,
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
        self,
        user_id: str,
        report_name: str,
        job_index: int,
        start_timestamp: str,
        end_timestamp: str,
        response_body: list[ThingPayload],
    ) -> None:
        log.debug("Uploading job csv file...")

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
            # response_body = get_thing_payloads(start_timestamp, end_timestamp)
            # log.info(f"UPLOAD CSV JOB {response_body=}")
            #
            # response_body = json.dumps(response_body)

            csv_data_rows: list[dict] = create_csv_rows(user_id, response_body)

            write_data_to_csv(report_job_file_path, report_job_filename, csv_data_rows)

            s3_upload_csv(
                self.s3_client,
                f"{report_job_file_path}/{report_job_filename}",
                f"{report_job_upload_path}/{report_job_filename}",
            )
        # except requests.HTTPError as error:
        #     log.error(f"Http client thing-payloads error: {error}")
        except ClientError as error:
            log.error(f"S3 client upload error: {error}")

            raise error

    async def produce(self, archive_job_messages: list[dict]) -> list[dict]:
        log.debug("Sending archive job message...")

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
