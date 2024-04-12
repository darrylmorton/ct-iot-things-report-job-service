import os

import boto3
import pytest
from dotenv import load_dotenv
from moto import mock_aws

load_dotenv(dotenv_path=".env.test")

# import config
# from tests.helper.data_helper import create_table


# @pytest.fixture
# def test_environment_variables():
#     os.environ["THINGS_REPORT_JOB_BUCKET_NAME"] = "./dist"


@pytest.fixture
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"


@pytest.fixture
def sqs_client(aws_credentials):
    with mock_aws():
        conn = boto3.client("sqs", region_name="eu-west-2")
        yield conn


# @pytest.fixture(scope="function")
# def setup_db(db_client: dynamodb):
#     create_table(db_client)
