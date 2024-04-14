import datetime
import json
import logging

log = logging.getLogger("things_report_job_service")


def create_report_timestamp(iso_date: str) -> datetime:
    return datetime.datetime.strptime(iso_date, "%Y-%m-%d %H:%M:%S")


def get_date_range_days(start: datetime, end: datetime) -> int:
    return int((end - start).days)


def create_archive_job_message(
    message_id: str,
    user_id: str,
    report_name: str,
    job_path: str,
    job_upload_path: str,
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
            "JobPath": {
                "DataType": "String",
                "StringValue": job_path,
            },
            "JobUploadPath": {
                "DataType": "String",
                "StringValue": job_upload_path,
            },
        },
        "MessageBody": json.dumps({
            "Id": message_id,
            "UserId": user_id,
            "ReportName": report_name,
            "JobPath": job_path,
            "JobUploadPath": job_upload_path,
        }),
        "MessageDeduplicationId": message_id,
    }
