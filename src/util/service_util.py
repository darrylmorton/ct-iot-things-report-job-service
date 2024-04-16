import datetime
import json
import logging
from typing import Tuple

log = logging.getLogger("things_report_job_service")

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def create_report_timestamp(timestamp: str) -> datetime:
    return datetime.datetime.strptime(timestamp, DATE_FORMAT)


def get_date_range_days(start: datetime, end: datetime) -> int:
    return int((end - start).days)


def create_epoch_timestamp(timestamp: str) -> int:
    return int(datetime.datetime.strptime(timestamp, DATE_FORMAT).timestamp())


def create_default_epoch_timestamps() -> Tuple[int, int]:
    today = datetime.datetime.today()

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
