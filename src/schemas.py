from pydantic import BaseModel


class PayloadValueUnit(BaseModel):
    value: str
    unit: str


class Temperature(PayloadValueUnit):
    connection: str


class Humidity(Temperature):
    precipitation: bool


class Payload(BaseModel):
    cadence: PayloadValueUnit
    battery: PayloadValueUnit
    temperature: Temperature
    humidity: Humidity


class ThingPayload(BaseModel):
    id: str
    device_id: str
    thing_payload: Payload
    payload_timestamp: int
