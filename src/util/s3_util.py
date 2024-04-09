import csv


def create_csv_writer(filename: str):
    with open(filename, "w", newline="") as csvfile:
        fieldnames = [
            "report_name",
            "user_id",
            "id",
            "device_id",
            "thing_name",
            "thing_type",
            "payload_timestamp",
            "cadence_value",
            "cadence_unit",
            "battery_value",
            "battery_unit",
            "temperature_value",
            "temperature_unit",
            "humidity_value",
            "humidity_unit"
        ]

        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csv_writer.writeheader()

        return csv_writer
