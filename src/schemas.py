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
