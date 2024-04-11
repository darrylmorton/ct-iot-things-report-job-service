import logging

import pytest

from src.config import THINGS_REPORT_JOB_QUEUE
from src.things_report_job_service.service import ThingsReportJobService

from ..helper.helper import create_sqs_queue
from ..helper.job_helper import service_poll, create_job_messages

log = logging.getLogger("test_things_report_job_service")

pytest_plugins = ("pytest_asyncio",)


@pytest.mark.asyncio
class TestRequestService:
    async def test_job_consumer(self, sqs_client):
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
