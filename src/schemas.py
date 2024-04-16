from pydantic import BaseModel, Field


class PayloadValueUnit(BaseModel):
    value: str
    unit: str

    class ConfigDict:
        from_attributes = True


class Temperature(PayloadValueUnit):
    connection: str

    class ConfigDict:
        from_attributes = True


class Humidity(Temperature):
    precipitation: bool

    class ConfigDict:
        from_attributes = True


class Payload(BaseModel):
    cadence: PayloadValueUnit
    battery: PayloadValueUnit
    temperature: Temperature
    humidity: Humidity

    class ConfigDict:
        from_attributes = True


class ThingPayload(BaseModel):
    id: str
    device_id: str = Field(alias="deviceId")
    thing_payload: Payload = Field(alias="thingPayload")
    payload_timestamp: int = Field(alias="payloadTimestamp")

    class ConfigDict:
        from_attributes = True


class MessageAttribute(BaseModel):
    DataType: str
    StringValue: str


class JobArchiveMessageAttribute(BaseModel):
    Id: MessageAttribute
    UserId: MessageAttribute
    ReportName: MessageAttribute
    JobPath: MessageAttribute
    JobUploadPath: MessageAttribute


class JobArchiveMessageBody(BaseModel):
    Id: str
    UserId: str
    ReportName: str
    JobPath: str
    JobUploadPath: str


class CSVRow(BaseModel):
    user_id: str
    device_id: str
    payload_timestamp: int
    cadence_unit: str
    cadence_value: float
    temperature_unit: str
    temperature_value: float
    humidity_unit: str
    humidity_value: float
    battery_unit: str
    battery_value: int
