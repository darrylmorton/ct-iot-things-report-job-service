import datetime
import json

import requests
from dateutil.parser import isoparse

from config import get_logger, THING_PAYLOADS_SERVICE_URL
from schemas import ThingPayload

log = get_logger()


def isodate_to_timestamp(timestamp: str) -> int:
    return int(isoparse(timestamp).timestamp())


def get_date_range_days(start: str, end: str) -> int:
    start_timestamp = datetime.datetime.fromisoformat(start)
    end_timestamp = datetime.datetime.fromisoformat(end)

    return int((end_timestamp - start_timestamp).days)


def create_default_epoch_timestamps() -> tuple[int, int]:
    today = datetime.datetime.now(datetime.UTC)

    today_timestamp = int(today.timestamp())
    yesterday_timestamp = int((today - datetime.timedelta(days=1)).timestamp())

    return today_timestamp, yesterday_timestamp


def create_archive_job_message(
    message_id: str,
    user_id: str,
    report_name: str,
    job_path: str,
    job_upload_path: str,
) -> dict:
    return dict(
        Id=message_id,
        MessageAttributes={
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
            "JobPath": {
                "DataType": "String",
                "StringValue": job_path,
            },
            "JobUploadPath": {
                "DataType": "String",
                "StringValue": job_upload_path,
            },
        },
        MessageBody=json.dumps({
            "Id": message_id,
            "UserId": user_id,
            "ReportName": report_name,
            "JobPath": job_path,
            "JobUploadPath": job_upload_path,
        }),
        MessageDeduplicationId=message_id,
    )


def get_thing_payloads(start_timestamp: str, end_timestamp: str) -> list[ThingPayload]:
    if not start_timestamp or not end_timestamp:
        start_timestamp, end_timestamp = create_default_epoch_timestamps()
    else:
        start_timestamp = isodate_to_timestamp(start_timestamp)
        end_timestamp = isodate_to_timestamp(end_timestamp)

    response = requests.get(
        THING_PAYLOADS_SERVICE_URL,
        params={"start_timestamp": start_timestamp, "end_timestamp": end_timestamp},
    )

    if response.status_code != 200:
        log.error("Failed to get thing-payloads")

        raise requests.HTTPError("Failed to get thing-payloads")

    return response.json()
