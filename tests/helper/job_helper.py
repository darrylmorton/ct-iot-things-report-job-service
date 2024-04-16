import datetime
import json
import logging
import time
import uuid

from schemas import CSVRow
from src.things_report_job_service.service import ThingsReportJobService
from src.util.service_util import get_date_range_days, isodate_to_timestamp

log = logging.getLogger("test_things_report_job_service")


async def service_poll(job_service: ThingsReportJobService, timeout_seconds=0) -> None:
    timeout = time.time() + timeout_seconds

    while True:
        if time.time() > timeout:
            log.info(f"Task timed out after {timeout_seconds}")
            break
        else:
            await job_service.consume()


def create_job_message(
    message_id: str,
    user_id: str,
    report_name: str,
    start_timestamp: str,
    end_timestamp: str,
    job_index: str,
    total_jobs: str,
    archive_report: str,
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
        MessageBody=json.dumps({
            "Id": message_id,
            "UserId": user_id,
            "ReportName": report_name,
            "StartTimestamp": start_timestamp,
            "EndTimestamp": end_timestamp,
            "JobIndex": job_index,
            "TotalJobs": total_jobs,
            "ArchiveReport": archive_report,
        }),
        MessageDeduplicationId=message_id,
    )


def create_job_messages(total: int, offset=0) -> list[dict]:
    messages = []
    year_delta = 10

    for counter in range(total):
        index = counter + offset

        start_timestamp_isoformat = f"20{year_delta}-01-01T00:00:00Z"
        start_timestamp = datetime.datetime.fromisoformat(start_timestamp_isoformat)

        year_delta = year_delta + 1
        end_timestamp_isoformat = f"20{year_delta}-01-01T00:00:00Z"

        end_timestamp = datetime.datetime.fromisoformat(end_timestamp_isoformat)

        date_range_days = get_date_range_days(start_timestamp, end_timestamp)

        message_id = str(uuid.uuid4())
        user_id = str(uuid.uuid4())
        archive_report = index == total - 1

        job_message = create_job_message(
            message_id,
            user_id,
            report_name=f"report_name_0",
            start_timestamp=f"{start_timestamp}",
            end_timestamp=f"{end_timestamp}",
            job_index=f"{index}",
            total_jobs=f"{date_range_days}",
            archive_report=f"{archive_report}",
        )
        messages.append(job_message)

        year_delta = year_delta + 1

    return messages


def expected_job_messages(messages: list[dict]) -> list[dict]:
    job_messages = []

    for message in messages:
        message_body = json.loads(message["MessageBody"])

        start_timestamp_iso = message_body["StartTimestamp"]
        start_timestamp = isodate_to_timestamp(start_timestamp_iso)
        end_timestamp_iso = message_body["EndTimestamp"]
        end_timestamp = isodate_to_timestamp(end_timestamp_iso)

        date_range_days = get_date_range_days(start_timestamp, end_timestamp)
        total_jobs = date_range_days + 1

        for index in range(total_jobs):
            job_date = datetime.datetime.fromisoformat(start_timestamp_iso)

            datetime_delta = datetime.timedelta(days=index)

            job_start_date = (
                job_date.replace(hour=0, minute=0, second=0) + datetime_delta
            )
            job_end_date = (
                job_date.replace(hour=23, minute=59, second=59) + datetime_delta
            )

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
                archive_report=str(archive_report),
            )

            job_messages.append(job_message)

    return job_messages


def assert_job_messages(actual_result: list[dict], expected_result: list[dict]) -> None:
    assert len(actual_result) == len(expected_result)
    index = 0

    for request_message in actual_result:
        assert request_message.body == expected_result[index]["MessageBody"]
        index = index + 1


def create_csv_rows_data() -> list[CSVRow]:
    return [
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712644796,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 35.15662240328055,
            "humidity_unit": "%",
            "humidity_value": 51.6083583513192,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712644796,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 27.276714220539144,
            "humidity_unit": "%",
            "humidity_value": 67.05524930677332,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712644796,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 31.157212181833437,
            "humidity_unit": "%",
            "humidity_value": 68.81753529482991,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712644796,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 23.289647241331927,
            "humidity_unit": "%",
            "humidity_value": 79.07751663450105,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712644796,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 36.9593356982144,
            "humidity_unit": "%",
            "humidity_value": 77.15062410191874,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712644796,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 37.289323878492056,
            "humidity_unit": "%",
            "humidity_value": 37.26870137538795,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712646596,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 17.28557938212959,
            "humidity_unit": "%",
            "humidity_value": 67.60360510122945,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712648396,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 36.059425825609466,
            "humidity_unit": "%",
            "humidity_value": 34.76411286409971,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712646596,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 24.1130893424591,
            "humidity_unit": "%",
            "humidity_value": 59.83784191780981,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712646596,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 26.985929801219125,
            "humidity_unit": "%",
            "humidity_value": 68.37455917106303,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712650196,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 36.679276484514965,
            "humidity_unit": "%",
            "humidity_value": 59.60831587981174,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712653796,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 22.306011847141157,
            "humidity_unit": "%",
            "humidity_value": 35.64459899808784,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712657396,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 36.96746448490633,
            "humidity_unit": "%",
            "humidity_value": 33.43878539112916,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712646596,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 17.117047886318673,
            "humidity_unit": "%",
            "humidity_value": 69.04992408169257,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712648396,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 35.96814266572569,
            "humidity_unit": "%",
            "humidity_value": 78.99821981876713,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712646596,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 31.29279275416532,
            "humidity_unit": "%",
            "humidity_value": 54.03638921953224,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712646596,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 18.085764740077906,
            "humidity_unit": "%",
            "humidity_value": 65.2528450566898,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712648396,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 16.13066321382586,
            "humidity_unit": "%",
            "humidity_value": 77.53828290035203,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712648396,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 29.358286157927104,
            "humidity_unit": "%",
            "humidity_value": 54.327355877400095,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712650196,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 22.70617415839729,
            "humidity_unit": "%",
            "humidity_value": 80.16768747715003,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712650196,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 22.948120560575177,
            "humidity_unit": "%",
            "humidity_value": 36.86621941144663,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712650196,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 34.853023125929354,
            "humidity_unit": "%",
            "humidity_value": 70.23884261944443,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712651996,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 23.41559033855647,
            "humidity_unit": "%",
            "humidity_value": 44.62352382031786,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712651996,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 19.160211478738482,
            "humidity_unit": "%",
            "humidity_value": 53.99219155948019,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712651996,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 36.220567497982934,
            "humidity_unit": "%",
            "humidity_value": 56.632562018510086,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712653796,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 22.996030681892258,
            "humidity_unit": "%",
            "humidity_value": 77.91579785461624,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712653796,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 31.080735524762144,
            "humidity_unit": "%",
            "humidity_value": 47.20829301109747,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712653796,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 19.999767511697744,
            "humidity_unit": "%",
            "humidity_value": 58.09519371106363,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712653796,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 28.722123104618333,
            "humidity_unit": "%",
            "humidity_value": 71.03849097590918,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712655596,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 31.41798332239503,
            "humidity_unit": "%",
            "humidity_value": 67.50727308170478,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712655596,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 23.334580924892165,
            "humidity_unit": "%",
            "humidity_value": 52.165149158820185,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712655596,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 18.204173473739935,
            "humidity_unit": "%",
            "humidity_value": 61.56325207905398,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712655596,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 28.52867168860913,
            "humidity_unit": "%",
            "humidity_value": 80.58103992217254,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712648396,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 33.1665720646418,
            "humidity_unit": "%",
            "humidity_value": 56.722514835844564,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712648396,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 37.73088375821331,
            "humidity_unit": "%",
            "humidity_value": 42.94876805124083,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712650196,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 16.51190194066335,
            "humidity_unit": "%",
            "humidity_value": 77.71149880423403,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712651996,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 29.444982053439933,
            "humidity_unit": "%",
            "humidity_value": 32.46805320560854,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712651996,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 29.579743044393865,
            "humidity_unit": "%",
            "humidity_value": 46.384174630660944,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712655596,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 18.179043336775255,
            "humidity_unit": "%",
            "humidity_value": 34.97432342030874,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712655596,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 31.93975535607653,
            "humidity_unit": "%",
            "humidity_value": 62.55340289275998,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712657396,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 24.184221903426288,
            "humidity_unit": "%",
            "humidity_value": 53.55400400385767,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712650196,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 22.474258325222124,
            "humidity_unit": "%",
            "humidity_value": 38.00058028676371,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712651996,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 32.35949167978876,
            "humidity_unit": "%",
            "humidity_value": 48.00708912058185,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712653796,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 27.69454741734932,
            "humidity_unit": "%",
            "humidity_value": 60.52716333578073,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712657396,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 32.35068540325718,
            "humidity_unit": "%",
            "humidity_value": 39.81060847769592,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712657396,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 28.7565148046883,
            "humidity_unit": "%",
            "humidity_value": 52.84324884920133,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712657396,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 18.63370296740316,
            "humidity_unit": "%",
            "humidity_value": 32.04304098020051,
            "battery_unit": "%",
            "battery_value": 50,
        },
        {
            "user_id": "d4b33dab-e3bd-4c6c-baf3-5a5d72a8df96",
            "device_id": "thing_payload.deviceId",
            "payload_timestamp": 1712657396,
            "cadence_unit": "seconds",
            "cadence_value": 1800,
            "temperature_unit": "C",
            "temperature_value": 24.567522616096102,
            "humidity_unit": "%",
            "humidity_value": 32.6720911720901,
            "battery_unit": "%",
            "battery_value": 50,
        },
    ]
