import datetime
from unittest.mock import patch, MagicMock

import boto3
import pytest
import uuid

from config import get_logger
from tests.helper.thing_payloads_helper import (
    expected_thing_payloads,
)
from tests.helper.archive_job_helper import (
    expected_archive_job_message,
    report_archive_job_consumer,
    assert_archive_job_messages,
)
from tests.helper.helper import create_sqs_queue
from tests.config import (
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
from tests.helper.job_helper import (
    service_poll,
    create_job_messages,
    create_csv_rows_data,
)
from util.service_util import isodate_to_timestamp

log = get_logger()


@pytest.mark.asyncio
class TestJobService:
    user_id = str(uuid.uuid4())
    report_name = "report_name_0"
    job_index = 0
    start_timestamp = "2020-06-20T12:00:00Z"
    start_epoch_timestamp = isodate_to_timestamp(start_timestamp)
    end_timestamp = "2020-06-23T12:00:00Z"
    end_epoch_timestamp = isodate_to_timestamp(end_timestamp)
    # fmt: off
    job_file_path_prefix = (f"""
        {THINGS_REPORT_JOB_FILE_PATH_PREFIX}/{user_id}/
        {report_name}-{start_epoch_timestamp}-{end_epoch_timestamp}
    """)
    job_upload_path = (
        f"{user_id}/{report_name}-{start_epoch_timestamp}-{end_epoch_timestamp}"
    )
    job_path_suffix = f"{report_name}-{0}.csv"

    # uploading disabled
    @patch("things_report_job_service.service.get_thing_payloads")
    @patch("things_report_job_service.service.s3_upload_csv")
    async def test_job_consumer_with_thing_payloads_request_and_uploading_mocks(
            self, mock_get_thing_payloads, mock_s3_upload_csv, job_service
    ):
        mock_get_thing_payloads.return_value = MagicMock(
            return_value=expected_thing_payloads()
        )
        mock_s3_upload_csv.return_value = MagicMock(return_value=None)

        report_job_queue, _ = create_sqs_queue(
            THINGS_REPORT_JOB_QUEUE, THINGS_REPORT_JOB_DLQ
        )
        report_archive_job_queue, _ = create_sqs_queue(THINGS_REPORT_ARCHIVE_JOB_QUEUE)

        message_batch_one = create_job_messages(
            self.start_timestamp, self.end_timestamp
        )

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

    # uploading disabled
    @patch("things_report_job_service.service.s3_upload_csv")
    @pytest.mark.skip(reason="requires running thing-payloads-service")
    async def test_job_consumer_with_upload_mock(
            self, mock_s3_upload_csv, job_service
    ):
        mock_s3_upload_csv.return_value = None

        report_job_queue, _ = create_sqs_queue(
            THINGS_REPORT_JOB_QUEUE, THINGS_REPORT_JOB_DLQ
        )
        report_archive_job_queue, _ = create_sqs_queue(THINGS_REPORT_ARCHIVE_JOB_QUEUE)

        message_batch_one = create_job_messages(
            self.start_timestamp, self.end_timestamp
        )

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
        start = datetime.datetime.fromtimestamp(
            self.start_epoch_timestamp, tz=datetime.timezone.utc
        ).isoformat()
        end = datetime.datetime.fromtimestamp(
            self.start_epoch_timestamp, tz=datetime.timezone.utc
        ).isoformat()

        actual_result_file_path, actual_result_upload_path, actual_result_filename = (
            create_csv_report_job_path(
                self.user_id,
                self.report_name,
                self.job_index,
                start_timestamp=start,
                end_timestamp=end,
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

    @pytest.mark.skip
    async def test_job_consumer_dlq(self, job_service):
        pass
