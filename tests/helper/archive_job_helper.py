import json
import logging
import time
import uuid
from typing import Any

from src.config import THINGS_REPORT_JOB_FILE_PATH_PREFIX
from src.util.s3_util import isodate_to_timestamp
from ..helper.helper import validate_uuid4
from src.things_report_job_service.service import ThingsReportJobService
from src.util.service_util import create_archive_job_message

log = logging.getLogger("test_things_report_job_service")


def expected_archive_job_message(message: Any):
    message_body = json.loads(message["MessageBody"])

    start_timestamp = isodate_to_timestamp(message_body["StartTimestamp"])
    end_timestamp = isodate_to_timestamp(message_body["EndTimestamp"])

    message_id = uuid.uuid4()
    job_path_prefix = f"{message_body["UserId"]}/{message_body["ReportName"]}"
    job_path_suffix = f"{int(start_timestamp)}-{int(end_timestamp)}"
    job_path = f"{job_path_prefix}-{job_path_suffix}"

    job_upload_path = job_path
    job_path = f"{THINGS_REPORT_JOB_FILE_PATH_PREFIX}/{job_path}"

    return [
        create_archive_job_message(
            message_id=str(message_id),
            user_id=message_body["UserId"],
            report_name=message_body["ReportName"],
            job_path=job_path,
            job_upload_path=job_upload_path,
        )
    ]


async def service_poll(job_service: ThingsReportJobService, timeout_seconds=0):
    timeout = time.time() + timeout_seconds

    while True:
        if time.time() > timeout:
            log.info(f"Task timed out after {timeout_seconds}")
            break
        else:
            await job_service.consume()


async def report_archive_job_consumer(
    report_archive_job_queue: Any, timeout_seconds=0
) -> Any:
    log.info(f"Starting report archive job consumer...")

    timeout = time.time() + timeout_seconds
    messages = []

    while True:
        log.info(f"Archive job consuming...")

        if time.time() > timeout:
            log.info(f"Task timed out after {timeout_seconds}")
            break

        archive_job_messages = report_archive_job_queue.receive_messages(
            MessageAttributeNames=["All"],
            MaxNumberOfMessages=10,
            WaitTimeSeconds=5,
        )
        log.info(f"**** Archive job messages {archive_job_messages}")
        log.info(f"**** Archive job messages ARRAY LENGTH {len(archive_job_messages)}")

        for archive_job_message in archive_job_messages:
            messages.append(archive_job_message)

            archive_job_message.delete()

    return messages


def assert_archive_job_message(actual_result: Any, expected_result: Any):
    assert validate_uuid4(actual_result["Id"])
    assert validate_uuid4(expected_result["Id"])
    assert actual_result["Id"] != expected_result["Id"]

    assert actual_result["UserId"] == expected_result["UserId"]
    assert actual_result["ReportName"] == expected_result["ReportName"]

    log.info(
        f"assert_actual_archive_job_message actual_result {actual_result["JobPath"]}"
    )
    log.info(
        f"assert_actual_archive_job_message expected_result {expected_result["JobPath"]}"
    )

    assert actual_result["JobPath"] == expected_result["JobPath"]
    assert actual_result["JobUploadPath"] == expected_result["JobUploadPath"]


def assert_archive_job_messages(actual_result: Any, expected_result: Any):
    # log.info(f"json.loads(actual_result): {json.loads(actual_result)}")

    assert len(actual_result) == len(expected_result)
    index = 0

    for archive_message in actual_result:
        archive_message_body = json.loads(archive_message.body)

        expected_message = expected_result[index]
        expected_result_body = json.loads(expected_message["MessageBody"])

        assert_archive_job_message(archive_message_body, expected_result_body)

        index = index + 1
