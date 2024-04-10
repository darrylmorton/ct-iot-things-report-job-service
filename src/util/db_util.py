import boto3

from ..config import THING_PAYLOADS_DB_NAME, AWS_REGION

dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)


# def get_things_by_start_timestamp_and_end_timestamp(start_timestamp: str, end_timestamp: str):
#     response = table.query(
#         KeyConditionExpression=Key("start_timestamp").gte(start_timestamp).lte(end_timestamp)
#     )
#
#     return response["Items"]


async def query_by_device_id(device_id: str):
    table = dynamodb.Table(THING_PAYLOADS_DB_NAME)

    resource = table.query({
        "TableName": THING_PAYLOADS_DB_NAME,
        "IndexName": "deviceIdIndex",
        "KeyConditionExpression": "deviceId = :deviceId",
        "ExpressionAttributeValues": {":deviceId": device_id},
        "Select": "SPECIFIC_ATTRIBUTES",
        "ProjectionExpression": "id, thingName, deviceId, thingTypeId, description",
    })

    return resource["Items"]
