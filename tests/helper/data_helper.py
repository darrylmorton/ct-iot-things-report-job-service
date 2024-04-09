import boto3

from config import THINGS_DB_NAME, AWS_REGION

dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)


async def create_table(db_client: dynamodb):
    db_client.create_table({
        "TableName": THINGS_DB_NAME,
        "AttributeDefinitions": [
            {
                "AttributeName": "id",
                "AttributeType": "S",
            },
            {
                "AttributeName": "thingName",
                "AttributeType": "S",
            },
            {
                "AttributeName": "deviceId",
                "AttributeType": "S",
            },
            {
                "AttributeName": "thingTypeId",
                "AttributeType": "S",
            },
            {
                "AttributeName": "updatedAt",
                "AttributeType": "S",
            },
        ],
        "KeySchema": [
            {
                "AttributeName": "id",
                "KeyType": "HASH",
            },
        ],
        "ProvisionedThroughput": {
            "ReadCapacityUnits": 1,
            "WriteCapacityUnits": 1,
        },
        "StreamSpecification": {
            "StreamEnabled": False,
        },
        "BillingMode": "PAY_PER_REQUEST",
        "GlobalSecondaryIndexes": [
            {
                "IndexName": "thingNameIndex",
                "KeySchema": [
                    {
                        "AttributeName": "thingName",
                        "KeyType": "HASH",
                    },
                    {
                        "AttributeName": "updatedAt",
                        "KeyType": "RANGE",
                    },
                ],
                "Projection": {
                    "ProjectionType": "ALL",
                },
                "ProvisionedThroughput": {
                    "ReadCapacityUnits": 1,
                    "WriteCapacityUnits": 1,
                },
            },
            {
                "IndexName": "deviceIdIndex",
                "KeySchema": [
                    {
                        "AttributeName": "deviceId",
                        "KeyType": "HASH",
                    },
                    {
                        "AttributeName": "updatedAt",
                        "KeyType": "RANGE",
                    },
                ],
                "Projection": {
                    "ProjectionType": "ALL",
                },
                "ProvisionedThroughput": {
                    "ReadCapacityUnits": 1,
                    "WriteCapacityUnits": 1,
                },
            },
            {
                "IndexName": "thingTypeIdIndex",
                "KeySchema": [
                    {
                        "AttributeName": "thingTypeId",
                        "KeyType": "HASH",
                    },
                    {
                        "AttributeName": "updatedAt",
                        "KeyType": "RANGE",
                    },
                ],
                "Projection": {
                    "ProjectionType": "ALL",
                },
                "ProvisionedThroughput": {
                    "ReadCapacityUnits": 1,
                    "WriteCapacityUnits": 1,
                },
            },
        ],
    })


async def drop_table(db_client: dynamodb):
    db_client.delete.table(TableName=THINGS_DB_NAME)
