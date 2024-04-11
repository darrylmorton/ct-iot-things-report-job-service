import csv
import os


def create_csv_writer(job_path_prefix: str, job_path_suffix: str, filename: str):
    if not os.path.exists(f"./{job_path_prefix}/{job_path_suffix}/"):
        os.makedirs(f"./{job_path_prefix}/{job_path_suffix}/")

    job_file_path = f"./{job_path_prefix}/{job_path_suffix}/{filename}"

    with open(job_file_path, "w", newline="") as csvfile:
        fieldnames = [
            "report_name",
            "user_id",
            "id",
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

        return csv_writer
