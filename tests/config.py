import os

from dotenv import load_dotenv

load_dotenv(dotenv_path=".env.test")

AWS_REGION = os.environ.get("AWS_REGION")

THING_PAYLOADS_DB_NAME = os.environ.get("THING_PAYLOADS_DB_NAME")
QUEUE_WAIT_SECONDS = int(os.environ.get("QUEUE_WAIT_SECONDS"))
THINGS_REPORT_JOB_QUEUE = os.environ.get("THINGS_REPORT_JOB_QUEUE")
THINGS_REPORT_JOB_DLQ = os.environ.get("THINGS_REPORT_JOB_DLQ")
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
