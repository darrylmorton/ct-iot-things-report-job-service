import json
import logging
import time
import uuid
from typing import Any

from tests.helper.helper import validate_uuid4
from things_report_job_service.service import ThingsReportJobService
from util.service_util import create_archive_job_message

log = logging.getLogger("test_things_report_job_service")


def expected_archive_job_message(message: Any):
    message_body = json.loads(message['MessageBody'])

    message_id = uuid.uuid4()
    job_path_prefix = f"{message_body['UserId']}/{message_body['ReportName']}"
    job_path_suffix = f"{message_body["StartTimestamp"]}-{message_body["EndTimestamp"]}"
    job_path = f"{job_path_prefix}/{job_path_suffix}"
    job_path = f"{job_path}.zip"

    return create_archive_job_message(
        message_id=str(message_id),
        user_id=message_body["UserId"],
        report_name=message_body["ReportName"],
        job_path=job_path,
    )


def service_poll(job_service: ThingsReportJobService, timeout_seconds=0):
    timeout = time.time() + timeout_seconds

    while True:
        if time.time() > timeout:
            log.info(f"Task timed out after {timeout_seconds}")
            break
        else:
            job_service.consume()


def report_archive_job_consumer(report_archive_job_queue: Any, timeout_seconds=0) -> Any:
    timeout = time.time() + timeout_seconds
    messages = []

    while True:
        if time.time() > timeout:
            log.info(f"Task timed out after {timeout_seconds}")
            break

        archive_job_messages = report_archive_job_queue.receive_messages(
            MessageAttributeNames=["All"],
            MaxNumberOfMessages=10,
            WaitTimeSeconds=5,
        )

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
    assert actual_result["StartTimestamp"] == expected_result["StartTimestamp"]
    assert actual_result["EndTimestamp"] == expected_result["EndTimestamp"]
    assert actual_result["JobIndex"] == expected_result["JobIndex"]
    assert actual_result["TotalJobs"] == expected_result["TotalJobs"]
    assert actual_result["JobPath"] == expected_result["JobPath"]
    assert actual_result["ArchiveReport"] == expected_result["ArchiveReport"]


def assert_archive_job_messages(actual_result: Any, expected_result: Any):
    assert len(actual_result) == len(expected_result)
    index = 0

    for archive_message in actual_result:
        archive_message_body = json.loads(archive_message.body)

        expected_message = expected_result[index]
        expected_result_body = json.loads(expected_message["MessageBody"])

        assert_archive_job_message(archive_message_body, expected_result_body)

        index = index + 1
