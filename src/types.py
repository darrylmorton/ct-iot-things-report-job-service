type Message_Attribute = {"DataType": str, "StringValue": str}

type Job_Archive_Message_Attribute = {
    "Id": Message_Attribute,
    "UserId": Message_Attribute,
    "ReportName": Message_Attribute,
    "JobPath": Message_Attribute,
    "JobUploadPath": Message_Attribute,
}

type Job_Archive_Message_Body = {
    "Id": str,
    "UserId": str,
    "ReportName": str,
    "JobPath": str,
    "JobUploadPath": str,
}

type SQS_Message = {
    "Id": str,
    "MessageAttributes": Job_Archive_Message_Attribute,
    "MessageBody": Job_Archive_Message_Body,
    "MessageDeduplicationId": str,
}

type CSV_Row = {
    "user_id": str,
    "device_id": str,
    "payload_timestamp": int,
    "cadence_unit": str,
    "cadence_value": str,
    "temperature_unit": str,
    "temperature_value": str,
    "humidity_unit": str,
    "humidity_value": str,
    "battery_unit": str,
    "battery_value": str,
}
