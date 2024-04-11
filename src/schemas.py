from pydantic import BaseModel, Field, EmailStr


class Cadence(BaseModel):
    value: str
    unit: str


class Battery(BaseModel):
    value: str
    unit: str


class Temperature(BaseModel):
    value: str
    unit: str


class Humidity(BaseModel):
    value: str
    unit: str
    connection: str
    precipitation: bool


class Payload(BaseModel):
    cadence: Cadence
    battery: Battery
    temperature: Temperature
    humidity: Humidity


class ThingPayload(BaseModel):
    id: str
    device_id: str
    thing_payload: Payload
    payload_timestamp: str
    # start_timestamp: str
    # end_timestamp: str
