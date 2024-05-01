import datetime
import json
from typing import Tuple

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


def create_default_epoch_timestamps() -> Tuple[int, int]:
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


def get_thing_payloads(
    start_timestamp: int, end_timestamp: int
) -> (int, list[ThingPayload]):
    response = requests.get(
        THING_PAYLOADS_SERVICE_URL,
        params={"start_timestamp": start_timestamp, "end_timestamp": end_timestamp},
    )

    return response.status_code, response.json()
