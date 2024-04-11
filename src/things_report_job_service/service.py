import json
import logging
import uuid
from typing import Any

import boto3
from botocore.exceptions import ClientError

from schemas import ThingPayload
from ..config import THINGS_REPORT_JOB_QUEUE, AWS_REGION
from ..crud import find_thing_payloads
from ..util.s3_util import create_csv_writer
from ..util.service_util import create_archive_job_message

log = logging.getLogger("things_report_job_service")


class ThingsReportJobService:
    def __init__(self):
        self.sqs = boto3.resource("sqs", region_name=AWS_REGION)
        # self.s3_client = boto3.client("s3", region_name=AWS_REGION)
        self.report_job_queue = self.sqs.Queue(f"{THINGS_REPORT_JOB_QUEUE}.fifo")
        # self.report_archive_job_queue = self.sqs.Queue(f"{THINGS_REPORT_ARCHIVE_JOB_QUEUE}.fifo")

    async def poll(self):
        print("*** POLLING...")

        while True:
            await self.consume()

    async def consume(self):
        log.info("*** CONSUMING JOB MESSAGES...")
        # print(f"*** CONSUMING JOB MESSAGES...")

        try:
            job_messages = self.report_job_queue.receive_messages(
                MessageAttributeNames=["All"],
                MaxNumberOfMessages=10,
                WaitTimeSeconds=5,
            )

            log.info(f"*** *** CONSUMING JOB MESSAGES: {len(job_messages)}")

            if len(job_messages) > 0:
                job_path_prefix = "dist"
                job_path_suffix = "test3"
                job_filename = "test3"
                # job_path = f"dist/test/test"
                # log.info(f"*** job_path: {job_path}")

                csv_writer = create_csv_writer(
                    job_path_prefix, job_path_suffix, f"{job_filename}.csv"
                )

                for job_message in job_messages:
                    message_body = json.loads(job_message.body)

                    log.debug("message_body", message_body)

                    report_name = message_body["ReportName"]
                    user_id = message_body["UserId"]
                    device_id = message_body["DeviceId"]

                    things_payloads_result: list[
                        ThingPayload
                    ] = await find_thing_payloads()
                    # log.info(f"*** result: {len(result)}")

                    result = things_payloads_result
                    log.info(f"*** result: {result[0].id}")

                    # job_path_prefix = (
                    #     f"{message_body["UserId"]}/{message_body["ReportName"]}"
                    # )
                    # job_path_suffix = f"{message_body["StartTimestamp"]}-{message_body["EndTimestamp"]}"
                    # job_path_prefix = (
                    #     f"{message_body["UserId"]}/{message_body["ReportName"]}"
                    # )
                    # job_path_suffix = f"{message_body["StartTimestamp"]}-{message_body["EndTimestamp"]}"

                    for item in result:
                        # log.info(f"*** item: {len(job_messages)}")

                        # thing_payload = await query_by_device_id(device_id)
                        payload = item.payload
                        cadence = payload["cadence"]
                        battery = payload["battery"]
                        temperature = payload["temperature"]
                        humidity = payload["humidity"]

                        csv_writer.writerow({
                            "report_name": report_name,
                            "user_id": user_id,
                            # "id": thing_payload["id"],
                            "device_id": payload["device_id"],
                            # "thing_name": thing_payload["thingName"],
                            # "thing_type": thing_payload["thingType"],
                            "payload_timestamp": payload["payloadTimestamp"],
                            "cadence_value": cadence["value"],
                            "cadence_unit": cadence["unit"],
                            "battery_value": battery["value"],
                            "battery_unit": battery["unit"],
                            "temperature_value": temperature["value"],
                            "temperature_unit": temperature["unit"],
                            "humidity_value": humidity["value"],
                            "humidity_unit": humidity["unit"],
                        })

                        message_id = uuid.uuid4()

                        if message_body["ArchiveReport"] == "True":
                            job_path = f"{job_path}.zip"

                            archive_message = create_archive_job_message(
                                message_id=str(message_id),
                                user_id=message_body["UserId"],
                                report_name=message_body["ReportName"],
                                job_path=str(job_path),
                            )

                            # self.produce(archive_message)

                    job_message.delete()
        except ClientError as error:
            log.info(f"Couldn't receive report_job_queue messages error {error}")

            log.error(f"Couldn't receive report_job_queue messages error {error}")

            raise error

    def produce(self, archive_job_messages: Any) -> Any:
        try:
            if len(archive_job_messages) > 0:
                self.report_archive_job_queue.send_messages(
                    Entries=archive_job_messages
                )

            return archive_job_messages
        except ClientError as error:
            log.error(
                f"Couldn't receive report_archive_job_queue messages error {error}"
            )

            raise error
