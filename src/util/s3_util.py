import csv
import logging
import os

from ..schemas import ThingPayload, CSVRow
from .service_util import (
    create_default_epoch_timestamps,
    isodate_to_timestamp,
)
from ..config import THINGS_REPORT_JOB_BUCKET_NAME, THINGS_REPORT_JOB_FILE_PATH_PREFIX
from ..crud import find_thing_payloads_by_timestamps

log = logging.getLogger("things_report_job_service")


def create_csv_report_job_path(
    user_id: str, report_name: str, job_index, start_timestamp: str, end_timestamp: str
) -> tuple[str, str, str]:
    start_timestamp = isodate_to_timestamp(start_timestamp)
    end_timestamp = isodate_to_timestamp(end_timestamp)

    report_job_file_path = f"{THINGS_REPORT_JOB_FILE_PATH_PREFIX}/{user_id}/{report_name}-{start_timestamp}-{end_timestamp}"
    report_job_upload_path = (
        f"{user_id}/{report_name}-{start_timestamp}-{end_timestamp}"
    )
    report_job_filename = f"{report_name}-{job_index}.csv"

    return report_job_file_path, report_job_upload_path, report_job_filename


def create_csv_row(user_id: str, thing_payload: ThingPayload) -> CSVRow:
    device_id = thing_payload.device_id
    payload_timestamp = thing_payload.payload_timestamp

    payload = thing_payload.payload
    cadence = payload["cadence"]
    battery = payload["battery"]
    temperature = payload["temperature"]
    humidity = payload["humidity"]

    return CSVRow(
        user_id=user_id,
        device_id=device_id,
        payload_timestamp=payload_timestamp,
        cadence_unit=cadence["unit"],
        cadence_value=cadence["value"],
        temperature_unit=temperature["unit"],
        temperature_value=temperature["value"],
        humidity_unit=humidity["unit"],
        humidity_value=humidity["value"],
        battery_unit=battery["unit"],
        battery_value=battery["value"],
    )


async def create_csv_rows(
    user_id: str, start_timestamp: str, end_timestamp: str
) -> list[CSVRow]:
    if not start_timestamp or not end_timestamp:
        start_timestamp, end_timestamp = create_default_epoch_timestamps()
    else:
        start_timestamp = isodate_to_timestamp(start_timestamp)
        end_timestamp = isodate_to_timestamp(end_timestamp)

    thing_payloads_result = await find_thing_payloads_by_timestamps(
        start_timestamp, end_timestamp
    )

    csv_rows: list[CSVRow] = []

    for item in thing_payloads_result:
        csv_rows.append(create_csv_row(user_id, item))

    return csv_rows


def write_data_to_csv(
    report_job_path: str,
    report_job_filename: str,
    csv_data_rows: list,
) -> None:
    if not os.path.exists(f"{report_job_path}"):
        os.makedirs(f"{report_job_path}")

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


def s3_upload_csv(s3_client, file_path, upload_path) -> None:
    with open(file_path, "rb") as f:
        s3_client.upload_file(file_path, THINGS_REPORT_JOB_BUCKET_NAME, upload_path)

        f.close()
