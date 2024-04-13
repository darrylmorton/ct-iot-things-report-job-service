import logging
from unittest.mock import patch

import boto3
import pytest
import uuid

from src.config import (
    THINGS_REPORT_JOB_QUEUE,
    THINGS_REPORT_JOB_BUCKET_NAME,
    AWS_REGION,
)
from src.things_report_job_service.service import ThingsReportJobService
from src.util.s3_util import create_csv_report_job_path, s3_upload_report_job

from ..helper.helper import create_sqs_queue
from ..helper.job_helper import service_poll, create_job_messages, create_csv_rows_data

log = logging.getLogger("test_things_report_job_service")


@pytest.mark.asyncio
class TestRequestService:
    user_id = str(uuid.uuid4())
    report_name = "report_name_0"
    job_index = 0
    start_timestamp = "2024-04-12 00:00:00"
    end_timestamp = "2024-04-12 23:59:59"
    job_path_prefix = (
        f"{THINGS_REPORT_JOB_BUCKET_NAME}/{user_id}/{report_name}-1712876400-1712962799"
    )
    job_path_suffix = f"{report_name}-{0}.csv"

    # @patch("src.util.s3_util.create_csv_report_job_path")
    @pytest.mark.skip
    def test_csv_report_job_path(self):
        # mock_create_csv_report_job_path.return_values((
        #     self.job_path_prefix,
        #     self.job_path_suffix,
        # ))

        expected_result_path = self.job_path_prefix
        expected_result_filename = self.job_path_suffix

        log.info(f"*** *** expected_result_path: {expected_result_path}")
        log.info(f"*** *** expected_result_filename: {expected_result_filename}")

        actual_result_path, actual_result_filename = create_csv_report_job_path(
            self.user_id,
            self.report_name,
            self.job_index,
            self.start_timestamp,
            self.end_timestamp,
        )

        log.info(f"*** *** expected_result_path: {actual_result_path}")
        log.info(f"*** *** expected_result_filename: {actual_result_filename}")
        assert actual_result_path == expected_result_path
        assert actual_result_filename == expected_result_filename

    # @patch("src.util.s3_util.create_csv_report_job_path")
    @pytest.mark.skip
    async def test_job_consumer(self, sqs_client):
        # job_path_prefix = f"dist/{self.user_id}"
        # job_path_suffix = f"{self.report_name}"
        # job_path_prefix = f"{self.user_id}/{self.report_name}-1712876400-1712962799"

        # mock_create_csv_report_job_path.returns(job_path_prefix, self.job_path_suffix)
        job_service = ThingsReportJobService()
        report_job_queue = create_sqs_queue(THINGS_REPORT_JOB_QUEUE)
        # report_archive_job_queue = create_sqs_queue(THINGS_REPORT_ARCHIVE_JOB_QUEUE)

        message_batch_one = create_job_messages(1)
        # expected_archive_job_message_batch_one = expected_archive_job_message(message_batch_one[0])
        # log.info(f"message_batch_one {message_batch_one}")

        report_job_queue.send_messages(Entries=message_batch_one)
        await service_poll(job_service, 30)

        # actual_archive_job_messages_batch_one = report_archive_job_consumer(report_archive_job_queue, 20)
        # assert_archive_job_messages(actual_archive_job_messages_batch_one, expected_archive_job_message_batch_one)

    # skipping as requires real aws credentials
    async def test_s3_report_job(self):
        actual_result_path, actual_result_filename = create_csv_report_job_path(
            self.user_id,
            self.report_name,
            self.job_index,
            self.start_timestamp,
            self.end_timestamp,
        )

        s3_client = boto3.client("s3", region_name=AWS_REGION)

        csv_data_rows = create_csv_rows_data()
        response = s3_upload_report_job(
            s3_client, csv_data_rows, f"{actual_result_path}/{actual_result_filename}"
        )

        log.info(f"S3 RESPONSE {response}")
