import os
import logging

from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.environ.get("AWS_REGION")

ENVIRONMENT = os.environ.get("ENVIRONMENT")
LOG_LEVEL = os.environ.get("LOG_LEVEL")
SERVICE_NAME = os.environ.get("SERVICE_NAME")
THING_PAYLOADS_DB_NAME = os.environ.get("THING_PAYLOADS_DB_NAME")
THINGS_REPORT_JOB_QUEUE = os.environ.get("THINGS_REPORT_JOB_QUEUE")
THINGS_REPORT_ARCHIVE_JOB_QUEUE = os.environ.get("THINGS_REPORT_ARCHIVE_JOB_QUEUE")
THINGS_REPORT_JOB_FILE_PATH_PREFIX = os.environ.get(
    "THINGS_REPORT_JOB_FILE_PATH_PREFIX"
)
THINGS_REPORT_JOB_BUCKET_NAME = os.environ.get("THINGS_REPORT_JOB_BUCKET_NAME")

DATABASE_URL_PREFIX = "postgresql+asyncpg"
DATABASE_URL_SUFFIX = (
    "{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}".format(
        DB_USERNAME=os.environ.get("DB_USERNAME"),
        DB_PASSWORD=os.environ.get("DB_PASSWORD"),
        DB_HOST=os.environ.get("DB_HOST"),
        DB_PORT=os.environ.get("DB_PORT"),
        DB_NAME=os.environ.get("DB_NAME"),
    )
)
DATABASE_URL = f"{DATABASE_URL_PREFIX}://{DATABASE_URL_SUFFIX}"


def get_logger() -> logging.Logger:
    logger = logging.getLogger("uvicorn")
    logger.setLevel(logging.getLevelName(LOG_LEVEL))

    return logger
