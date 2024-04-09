import datetime
import json
import logging
import time
import uuid
from typing import Any
from things_report_job_service.service import ThingsReportJobService
from util.service_util import create_report_timestamp, get_date_range_days

log = logging.getLogger("test_things_report_job_service")


def service_poll(job_service: ThingsReportJobService, timeout_seconds=0):
    timeout = time.time() + timeout_seconds

    while True:
        if time.time() > timeout:
            log.info(f"Task timed out after {timeout_seconds}")
            break
        else:
            job_service.consume()


def create_job_message(
        message_id: str,
        user_id: str,
        report_name: str,
        start_timestamp: str,
        end_timestamp: str,
        job_index: str,
        total_jobs: str,
        archive_report: str
):
    return {
        "Id": message_id,
        "MessageAttributes": {
            "Id": {
                "DataType": "String",
                "StringValue": message_id,
            },
            "UserId": {
                "DataType": "String",
                "StringValue": user_id,
            },
            "ReportName": {
                "DataType": "String",
                "StringValue": report_name,
            },
            "StartTimestamp": {
                "DataType": "String",
                "StringValue": start_timestamp,
            },
            "EndTimestamp": {
                "DataType": "String",
                "StringValue": end_timestamp,
            },
            "JobIndex": {
                "DataType": "String",
                "StringValue": job_index,
            },
            "TotalJobs": {
                "DataType": "String",
                "StringValue": total_jobs,
            },
            "ArchiveReport": {
                "DataType": "String",
                "StringValue": archive_report,
            },
        },
        "MessageBody": json.dumps({
            "Id": message_id,
            "UserId": user_id,
            "ReportName": report_name,
            "StartTimestamp": start_timestamp,
            "EndTimestamp": end_timestamp,
            "JobIndex": job_index,
            "TotalJobs": total_jobs,
            "ArchiveReport": archive_report,
        }),
        "MessageDeduplicationId": message_id,
    }


def create_job_messages(total: int, offset=0):
    messages = []
    device_id = "esp-abcdef123456"
    year_delta = 10

    for counter in range(total):
        index = counter + offset

        start_timestamp_isoformat = f"20{year_delta}-01-01T00:00:00"
        start_timestamp = create_report_timestamp(start_timestamp_isoformat)

        year_delta = year_delta + 1
        end_timestamp_isoformat = f"20{year_delta}-01-01T00:00:00"

        end_timestamp = create_report_timestamp(end_timestamp_isoformat)

        date_range_days = get_date_range_days(start_timestamp, end_timestamp)

        message_id = uuid.uuid4()
        user_id = uuid.uuid4()

        messages.append({
            "Id": str(message_id),
            "MessageAttributes": {
                "Id": {
                    "DataType": "String",
                    "StringValue": str(message_id),
                },
                "UserId": {
                    "DataType": "String",
                    "StringValue": str(user_id),
                },
                "ReportName": {
                    "DataType": "String",
                    "StringValue": f"report_name_{index}",
                },
                "DeviceId": {
                    "DataType": "String",
                    "StringValue": device_id,
                },
                "StartTimestamp": {
                    "DataType": "String",
                    "StringValue": start_timestamp_isoformat,
                },
                "EndTimestamp": {
                    "DataType": "String",
                    "StringValue": end_timestamp_isoformat,
                },
                "DateRangeDays": {
                    "DataType": "String",
                    "StringValue": str(date_range_days),
                }
            },
            "MessageBody": json.dumps({
                "Id": str(message_id),
                "UserId": str(user_id),
                "ReportName": f"report_name_{index}",
                "DeviceId": device_id,
                "StartTimestamp": start_timestamp_isoformat,
                "EndTimestamp": end_timestamp_isoformat,
                "DateRangeDays": str(date_range_days),
            }),
            "MessageDeduplicationId": str(message_id),
        })

        year_delta = year_delta + 1

    return messages


def expected_job_messages(messages: Any):
    job_messages = []

    for message in messages:
        message_body = json.loads(message['MessageBody'])

        start_timestamp_iso = message_body["StartTimestamp"]
        start_timestamp = create_report_timestamp(start_timestamp_iso)
        end_timestamp_iso = message_body["EndTimestamp"]
        end_timestamp = create_report_timestamp(end_timestamp_iso)

        date_range_days = get_date_range_days(start_timestamp, end_timestamp)
        total_jobs = date_range_days + 1

        for index in range(total_jobs):
            date = create_report_timestamp(start_timestamp_iso)

            datetime_delta = datetime.timedelta(days=index)

            job_start_date = date.replace(hour=0, minute=0, second=0) + datetime_delta
            job_end_date = date.replace(hour=23, minute=59, second=59) + datetime_delta

            message_id = uuid.uuid4()
            archive_report = index > date_range_days - 1

            job_message = create_job_message(
                message_id=str(message_id),
                user_id=message_body["UserId"],
                report_name=message_body["ReportName"],
                start_timestamp=job_start_date.isoformat(),
                end_timestamp=job_end_date.isoformat(),
                job_index=str(index),
                total_jobs=str(total_jobs),
                archive_report=str(archive_report)
            )

            job_messages.append(job_message)

    return job_messages


# def create_job_messages(total: int, offset=0):
#     messages = []
#     year_delta = 10
#
#     for counter in range(total):
#         index = counter + offset
#
#         start_timestamp_isoformat = f"20{year_delta}-01-01T00:00:00"
#         start_timestamp = create_report_timestamp(start_timestamp_isoformat)
#
#         year_delta = year_delta + 1
#         end_timestamp_isoformat = f"20{year_delta}-01-01T00:00:00"
#
#         end_timestamp = create_report_timestamp(end_timestamp_isoformat)
#
#         date_range_days = get_date_range_days(start_timestamp, end_timestamp)
#
#         message_id = uuid.uuid4()
#         user_id = uuid.uuid4()
#
#         messages.append({
#             "Id": str(message_id),
#             "MessageAttributes": {
#                 "Id": {
#                     "DataType": "String",
#                     "StringValue": str(message_id),
#                 },
#                 "UserId": {
#                     "DataType": "String",
#                     "StringValue": str(user_id),
#                 },
#                 "ReportName": {
#                     "DataType": "String",
#                     "StringValue": f"report_name_{index}",
#                 },
#                 "StartTimestamp": {
#                     "DataType": "String",
#                     "StringValue": start_timestamp_isoformat,
#                 },
#                 "EndTimestamp": {
#                     "DataType": "String",
#                     "StringValue": end_timestamp_isoformat,
#                 },
#                 "DateRangeDays": {
#                     "DataType": "String",
#                     "StringValue": str(date_range_days),
#                 }
#             },
#             "MessageBody": json.dumps({
#                 "Id": str(message_id),
#                 "UserId": str(user_id),
#                 "ReportName": f"report_name_{index}",
#                 "StartTimestamp": start_timestamp_isoformat,
#                 "EndTimestamp": end_timestamp_isoformat,
#                 "DateRangeDays": str(date_range_days),
#             }),
#             "MessageDeduplicationId": str(message_id),
#         })
#
#         year_delta = year_delta + 1
#
#     return messages
#
#
# def assert_job_messages(actual_result: Any, expected_result: Any):
#     assert len(actual_result) == len(expected_result)
#     index = 0
#
#     for request_message in actual_result:
#         assert request_message.body == expected_result[index]["MessageBody"]
#         index = index + 1
