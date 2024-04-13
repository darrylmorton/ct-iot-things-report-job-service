import csv
import datetime
import logging
import os
from typing import Any

from ..config import THINGS_REPORT_JOB_BUCKET_NAME, THINGS_REPORT_JOB_FILE_PATH_PREFIX
from ..crud import find_thing_payloads

log = logging.getLogger("things_report_job_service")


def create_csv_report_job_path(
    user_id: str, report_name: str, job_index, start_timestamp: str, end_timestamp: str
) -> tuple[str, str, str]:
    datetime_format = "%Y-%m-%d %H:%M:%S"

    start_timestamp = datetime.datetime.strptime(
        start_timestamp, datetime_format
    ).timestamp()
    end_timestamp = datetime.datetime.strptime(
        end_timestamp, datetime_format
    ).timestamp()

    report_job_file_path = f"{THINGS_REPORT_JOB_FILE_PATH_PREFIX}/{user_id}/{report_name}-{int(start_timestamp)}-{int(end_timestamp)}"
    report_job_upload_path = (
        f"{user_id}/{report_name}-{int(start_timestamp)}-{int(end_timestamp)}"
    )
    report_job_filename = f"{report_name}-{job_index}.csv"

    return report_job_file_path, report_job_upload_path, report_job_filename


def create_csv_row(user_id: str, thing_payload: Any) -> Any:
    device_id = "thing_payload.deviceId"
    payload_timestamp = thing_payload.payload_timestamp

    payload = thing_payload.payload
    cadence = payload["cadence"]
    battery = payload["battery"]
    temperature = payload["temperature"]
    humidity = payload["humidity"]

    return {
        "user_id": user_id,
        "device_id": device_id,
        "payload_timestamp": payload_timestamp,
        "cadence_unit": cadence["unit"],
        "cadence_value": cadence["value"],
        "temperature_unit": temperature["unit"],
        "temperature_value": temperature["value"],
        "humidity_unit": humidity["unit"],
        "humidity_value": humidity["value"],
        "battery_unit": battery["unit"],
        "battery_value": battery["value"],
    }


async def create_csv_rows(user_id: str):
    thing_payloads_result = await find_thing_payloads()

    csv_rows = []

    for item in thing_payloads_result:
        csv_rows.append(create_csv_row(user_id, item))

    return csv_rows


def create_csv_writer(
    report_job_path: str,
    report_job_filename: str,
    csv_data_rows: Any,
):
    if not os.path.exists(f"{report_job_path}"):
        os.makedirs(f"{report_job_path}")

    log.info(f"{report_job_path=} {report_job_filename=}")

    with open(f"{report_job_path}/{report_job_filename}", "w", newline="") as csvfile:
        fieldnames = [
            "user_id",
            "device_id",
            "payload_timestamp",
            "cadence_value",
            "cadence_unit",
            "battery_value",
            "battery_unit",
            "temperature_value",
            "temperature_unit",
            "humidity_value",
            "humidity_unit",
        ]

        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csv_writer.writeheader()

        csv_writer.writerows(csv_data_rows)


def s3_upload_csv(s3_client, file_path, upload_path):
    with open(file_path, "rb") as f:
        s3_client.upload_file(file_path, THINGS_REPORT_JOB_BUCKET_NAME, upload_path)

        f.close()


# async def upload_csv_job(
#     self, user_id, report_name, job_index, start_timestamp, end_timestamp
# ):
#     (
#         report_job_file_path,
#         report_job_upload_path,
#         report_job_filename,
#     ) = create_csv_report_job_path(
#         user_id,
#         report_name,
#         job_index,
#         start_timestamp,
#         end_timestamp,
#     )
#
#     result = await create_csv_rows(user_id)
#
#     create_csv_writer(report_job_file_path, report_job_filename, result)
#
#     return s3_upload_csv(
#         self.s3_client,
#         f"{report_job_file_path}/{report_job_filename}",
#         f"{report_job_upload_path}/{report_job_filename}",
#     )
#
#     # log.info(f"S3 RESPONSE {response}")
