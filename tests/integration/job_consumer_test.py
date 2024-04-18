import logging
from unittest.mock import patch

import boto3
import pytest
import uuid

from ..helper.db_helper import assert_thing_payloads, create_thing_payloads_data
from crud import find_thing_payloads_by_timestamps
from ..helper.archive_job_helper import (
    expected_archive_job_message,
    report_archive_job_consumer,
    assert_archive_job_messages,
)
from ..helper.helper import create_sqs_queue
from config import (
    THINGS_REPORT_JOB_QUEUE,
    AWS_REGION,
    THINGS_REPORT_JOB_FILE_PATH_PREFIX,
    THINGS_REPORT_ARCHIVE_JOB_QUEUE,
    THINGS_REPORT_JOB_DLQ,
)
from util.s3_util import (
    create_csv_report_job_path,
    write_data_to_csv,
    s3_upload_csv,
)
from ..helper.job_helper import (
    service_poll,
    create_job_messages,
    create_csv_rows_data,
)

log = logging.getLogger("test_things_report_job_service")


@pytest.mark.asyncio
class TestJobService:
    user_id = str(uuid.uuid4())
    report_name = "report_name_0"
    job_index = 0
    start_timestamp = "2024-04-12T00:00:00Z"
    end_timestamp = "2024-04-12T23:59:59Z"
    # fmt: off
    job_file_path_prefix = (
        f"{THINGS_REPORT_JOB_FILE_PATH_PREFIX}/{user_id}/{report_name}-1712880000-1712966399"
    )
    job_upload_path = f"{user_id}/{report_name}-1712880000-1712966399"
    start_epoch_timestamp = 1712880000
    job_path_suffix = f"{report_name}-{0}.csv"

    # uploading disabled
    @patch(
        "things_report_job_service.service.ThingsReportJobService.upload_csv_job"
    )
    async def test_job_consumer(self, mock_upload_csv_job, job_service):
        mock_upload_csv_job.return_value = None

        report_job_queue, _ = create_sqs_queue(
            THINGS_REPORT_JOB_QUEUE, THINGS_REPORT_JOB_DLQ
        )
        report_archive_job_queue, _ = create_sqs_queue(THINGS_REPORT_ARCHIVE_JOB_QUEUE)

        message_batch_one = create_job_messages(3)
        expected_archive_job_message_batch_one = expected_archive_job_message(
            message_batch_one[2]
        )

        report_job_queue.send_messages(Entries=message_batch_one)
        await service_poll(job_service, 10)

        actual_archive_job_messages_batch_one = await report_archive_job_consumer(
            report_archive_job_queue, 10
        )

        assert_archive_job_messages(
            actual_archive_job_messages_batch_one,
            expected_archive_job_message_batch_one,
        )

    @pytest.mark.skip(reason="requires real aws credentials")
    def test_s3_report_job(self):
        actual_result_file_path, actual_result_upload_path, actual_result_filename = (
            create_csv_report_job_path(
                self.user_id,
                self.report_name,
                self.job_index,
                self.start_timestamp,
                self.end_timestamp,
            )
        )

        csv_data_rows = create_csv_rows_data()

        write_data_to_csv(
            self.job_file_path_prefix, self.job_path_suffix, csv_data_rows
        )

        s3_client = boto3.client("s3", region_name=AWS_REGION)

        s3_upload_csv(
            s3_client,
            f"{actual_result_file_path}/{actual_result_filename}",
            f"{actual_result_upload_path}/{actual_result_filename}",
        )

    async def test_find_payloads_by_timestamps(self):
        start = 1712650196
        end = 1712653796

        expected_result = create_thing_payloads_data()

        actual_result = await find_thing_payloads_by_timestamps(start, end)

        assert_thing_payloads(actual_result, expected_result)

    @pytest.mark.skip
    async def test_job_consumer_dlq(self, job_service):
        pass
