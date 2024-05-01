from dataclasses import dataclass

from pydantic import BaseModel


class PayloadValueUnit(BaseModel):
    value: str | int | float
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


@dataclass
class ThingPayload(BaseModel):
    id: str
    device_id: str
    payload: Payload
    payload_timestamp: int

    class ConfigDict:
        from_attributes = True


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
