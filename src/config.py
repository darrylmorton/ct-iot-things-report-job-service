import os
import logging

from dotenv import load_dotenv

load_dotenv()

AWS_REGION = os.environ.get("AWS_REGION")

ENVIRONMENT = os.environ.get("ENVIRONMENT")
LOG_LEVEL = os.environ.get("LOG_LEVEL")
SERVICE_NAME = os.environ.get("SERVICE_NAME")
THING_PAYLOADS_DB_NAME = os.environ.get("THING_PAYLOADS_DB_NAME")
QUEUE_WAIT_SECONDS = int(os.environ.get("QUEUE_WAIT_SECONDS"))
THINGS_REPORT_JOB_QUEUE = os.environ.get("THINGS_REPORT_JOB_QUEUE")
THINGS_REPORT_JOB_DLQ = os.environ.get("THINGS_REPORT_JOB_DLQ")
THINGS_REPORT_ARCHIVE_JOB_QUEUE = os.environ.get("THINGS_REPORT_ARCHIVE_JOB_QUEUE")
THINGS_REPORT_JOB_FILE_PATH_PREFIX = os.environ.get(
    "THINGS_REPORT_JOB_FILE_PATH_PREFIX"
)
THINGS_REPORT_JOB_BUCKET_NAME = os.environ.get("THINGS_REPORT_JOB_BUCKET_NAME")

THING_PAYLOADS_SERVICE_HOST = os.environ.get("THING_PAYLOADS_SERVICE_HOST")
THING_PAYLOADS_SERVICE_PORT = os.environ.get("THING_PAYLOADS_SERVICE_PORT")
THING_PAYLOADS_SERVICE_URI = os.environ.get("THING_PAYLOADS_SERVICE_URI")
THING_PAYLOADS_SERVICE_URL = f"http://{THING_PAYLOADS_SERVICE_HOST}:{THING_PAYLOADS_SERVICE_PORT}/{THING_PAYLOADS_SERVICE_URI}"


def get_logger() -> logging.Logger:
    logger = logging.getLogger("uvicorn")
    logger.setLevel(logging.getLevelName(LOG_LEVEL))

    return logger
