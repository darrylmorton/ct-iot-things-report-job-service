import logging

from moto import mock_sqs

from config import THINGS_REPORT_JOB_QUEUE, THINGS_REPORT_ARCHIVE_JOB_QUEUE
from things_report_job_service.service import ThingsReportJobService
from ..helper.archive_job_helper import (
    expected_archive_job_message,
    assert_archive_job_messages,
    report_archive_job_consumer
)
from ..helper.helper import create_sqs_queue
from ..helper.job_helper import (
    service_poll,
    create_job_messages
)

log = logging.getLogger("test_things_report_job_service")


class TestRequestService:
    @mock_sqs
    def test_job_consumer(self):
        job_service = ThingsReportJobService()
        report_job_queue = create_sqs_queue(THINGS_REPORT_JOB_QUEUE)
        report_archive_job_queue = create_sqs_queue(THINGS_REPORT_ARCHIVE_JOB_QUEUE)

        message_batch_one = create_job_messages(1)
        # expected_archive_job_message_batch_one = expected_archive_job_message(message_batch_one[0])
        log.info(f"message_batch_one {message_batch_one}")

        report_job_queue.send_messages(Entries=message_batch_one)
        service_poll(job_service, 5)

        # actual_archive_job_messages_batch_one = report_archive_job_consumer(report_archive_job_queue, 20)
        # assert_archive_job_messages(actual_archive_job_messages_batch_one, expected_archive_job_message_batch_one)
