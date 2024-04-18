import logging
import datetime

import uuid

from config import THINGS_REPORT_JOB_FILE_PATH_PREFIX
from util.s3_util import create_csv_report_job_path
from util.service_util import (
    create_default_epoch_timestamps,
    isodate_to_timestamp,
)

log = logging.getLogger("test_things_report_job_service")


class TestUtil:
    user_id = str(uuid.uuid4())
    report_name = "report_name_0"
    job_index = 0
    start_timestamp = "2024-04-12T00:00:00Z"
    start_epoch_timestamp = 1712880000
    end_timestamp = "2024-04-12T23:59:59Z"
    # fmt: off
    job_file_path_prefix = (
        f"{THINGS_REPORT_JOB_FILE_PATH_PREFIX}/{user_id}/{report_name}-1712880000-1712966399"
    )
    job_upload_path = f"{user_id}/{report_name}-1712880000-1712966399"
    job_path_suffix = f"{report_name}-{0}.csv"

    def test_csv_report_job_path(self):
        expected_result_file_path = self.job_file_path_prefix
        expected_result_upload_path = self.job_upload_path
        expected_result_filename = self.job_path_suffix

        actual_result_file_path, actual_upload_path, actual_result_filename = (
            create_csv_report_job_path(
                self.user_id,
                self.report_name,
                self.job_index,
                self.start_timestamp,
                self.end_timestamp,
            )
        )

        assert actual_result_file_path == expected_result_file_path
        assert actual_upload_path == expected_result_upload_path
        assert actual_result_filename == expected_result_filename

    def test_create_default_timestamps(self):
        today = datetime.datetime.today()
        expected_today_timestamp = int(today.timestamp())
        expected_yesterday_timestamp = int(
            (today - datetime.timedelta(days=1)).timestamp()
        )

        actual_yesterday_timestamp, actual_today_timestamp = (
            create_default_epoch_timestamps()
        )
        log.info(f"{actual_yesterday_timestamp=}")
        log.info(f"{actual_today_timestamp=}")

        assert actual_yesterday_timestamp >= expected_yesterday_timestamp
        assert actual_today_timestamp <= expected_today_timestamp

    def test_create_timestamp(self):
        expected_epoch_timestamp = self.start_epoch_timestamp
        actual_epoch_timestamp_result = isodate_to_timestamp(self.start_timestamp)

        assert actual_epoch_timestamp_result == expected_epoch_timestamp
