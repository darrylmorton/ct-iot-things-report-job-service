from typing import Any

import logging

from schemas import ThingPayload
from models import ThingPayloadModel

log = logging.getLogger("test_things_report_job_service")


def create_thing_payloads_data() -> list[ThingPayloadModel]:
    return [
        {
            "device_id": "bbb-222222",
            "payload": {
                "battery": {"unit": "%", "value": 50},
                "cadence": {"unit": "seconds", "value": 1800},
                "humidity": {
                    "unit": "%",
                    "value": 59.60831587981174,
                    "connection": "pin:6",
                    "precipitation": False,
                },
                "temperature": {
                    "unit": "C",
                    "value": 36.679276484514965,
                    "connection": "pin:4",
                },
            },
            "payload_timestamp": 1712650196,
            "id": "6bd8fd0e-737d-4233-83a7-0ce05ac6af45",
        },
        {
            "device_id": "aaa-111111",
            "payload": {
                "battery": {"unit": "%", "value": 50},
                "cadence": {"unit": "seconds", "value": 1800},
                "humidity": {
                    "unit": "%",
                    "value": 35.64459899808784,
                    "connection": "pin:6",
                    "precipitation": False,
                },
                "temperature": {
                    "unit": "C",
                    "value": 22.306011847141157,
                    "connection": "pin:4",
                },
            },
            "payload_timestamp": 1712653796,
            "id": "371e3f15-42a4-412c-a49f-59de21cd7214",
        },
        {
            "device_id": "ddd-444444",
            "payload": {
                "battery": {"unit": "%", "value": 50},
                "cadence": {"unit": "seconds", "value": 1800},
                "humidity": {
                    "unit": "%",
                    "value": 80.16768747715003,
                    "connection": "pin:6",
                    "precipitation": False,
                },
                "temperature": {
                    "unit": "C",
                    "value": 22.70617415839729,
                    "connection": "pin:4",
                },
            },
            "payload_timestamp": 1712650196,
            "id": "0595938f-9213-4f54-bd56-695b234fa945",
        },
        {
            "device_id": "eee-555555",
            "payload": {
                "battery": {"unit": "%", "value": 50},
                "cadence": {"unit": "seconds", "value": 1800},
                "humidity": {
                    "unit": "%",
                    "value": 36.86621941144663,
                    "connection": "pin:6",
                    "precipitation": False,
                },
                "temperature": {
                    "unit": "C",
                    "value": 22.948120560575177,
                    "connection": "pin:4",
                },
            },
            "payload_timestamp": 1712650196,
            "id": "dd230efa-d9ca-4791-979f-7e650a633318",
        },
        {
            "device_id": "fff-666666",
            "payload": {
                "battery": {"unit": "%", "value": 50},
                "cadence": {"unit": "seconds", "value": 1800},
                "humidity": {
                    "unit": "%",
                    "value": 70.23884261944443,
                    "connection": "pin:6",
                    "precipitation": False,
                },
                "temperature": {
                    "unit": "C",
                    "value": 34.853023125929354,
                    "connection": "pin:4",
                },
            },
            "payload_timestamp": 1712650196,
            "id": "e8ef4fec-974f-4b39-b7e5-137c86f277c3",
        },
        {
            "device_id": "aaa-111111",
            "payload": {
                "battery": {"unit": "%", "value": 50},
                "cadence": {"unit": "seconds", "value": 1800},
                "humidity": {
                    "unit": "%",
                    "value": 44.62352382031786,
                    "connection": "pin:6",
                    "precipitation": False,
                },
                "temperature": {
                    "unit": "C",
                    "value": 23.41559033855647,
                    "connection": "pin:4",
                },
            },
            "payload_timestamp": 1712651996,
            "id": "3d179673-a541-4239-a81a-61e876d3b679",
        },
        {
            "device_id": "ddd-444444",
            "payload": {
                "battery": {"unit": "%", "value": 50},
                "cadence": {"unit": "seconds", "value": 1800},
                "humidity": {
                    "unit": "%",
                    "value": 53.99219155948019,
                    "connection": "pin:6",
                    "precipitation": False,
                },
                "temperature": {
                    "unit": "C",
                    "value": 19.160211478738482,
                    "connection": "pin:4",
                },
            },
            "payload_timestamp": 1712651996,
            "id": "ea6af77a-39d1-41d7-8e0a-7de6168d5158",
        },
        {
            "device_id": "eee-555555",
            "payload": {
                "battery": {"unit": "%", "value": 50},
                "cadence": {"unit": "seconds", "value": 1800},
                "humidity": {
                    "unit": "%",
                    "value": 56.632562018510086,
                    "connection": "pin:6",
                    "precipitation": False,
                },
                "temperature": {
                    "unit": "C",
                    "value": 36.220567497982934,
                    "connection": "pin:4",
                },
            },
            "payload_timestamp": 1712651996,
            "id": "a56c4b3d-4659-43ff-b4ba-f932ed2cd2b1",
        },
        {
            "device_id": "bbb-222222",
            "payload": {
                "battery": {"unit": "%", "value": 50},
                "cadence": {"unit": "seconds", "value": 1800},
                "humidity": {
                    "unit": "%",
                    "value": 77.91579785461624,
                    "connection": "pin:6",
                    "precipitation": False,
                },
                "temperature": {
                    "unit": "C",
                    "value": 22.996030681892258,
                    "connection": "pin:4",
                },
            },
            "payload_timestamp": 1712653796,
            "id": "cae86c70-cd4d-4c1c-b0ab-8e38e1883adc",
        },
        {
            "device_id": "ddd-444444",
            "payload": {
                "battery": {"unit": "%", "value": 50},
                "cadence": {"unit": "seconds", "value": 1800},
                "humidity": {
                    "unit": "%",
                    "value": 47.20829301109747,
                    "connection": "pin:6",
                    "precipitation": False,
                },
                "temperature": {
                    "unit": "C",
                    "value": 31.080735524762144,
                    "connection": "pin:4",
                },
            },
            "payload_timestamp": 1712653796,
            "id": "b4342206-5823-49aa-b2b5-4e06e9fc60bc",
        },
        {
            "device_id": "eee-555555",
            "payload": {
                "battery": {"unit": "%", "value": 50},
                "cadence": {"unit": "seconds", "value": 1800},
                "humidity": {
                    "unit": "%",
                    "value": 58.09519371106363,
                    "connection": "pin:6",
                    "precipitation": False,
                },
                "temperature": {
                    "unit": "C",
                    "value": 19.999767511697744,
                    "connection": "pin:4",
                },
            },
            "payload_timestamp": 1712653796,
            "id": "fc825ff2-5ce5-4536-88a0-d54ab700628f",
        },
        {
            "device_id": "ccc-333333",
            "payload": {
                "battery": {"unit": "%", "value": 50},
                "cadence": {"unit": "seconds", "value": 1800},
                "humidity": {
                    "unit": "%",
                    "value": 71.03849097590918,
                    "connection": "pin:6",
                    "precipitation": False,
                },
                "temperature": {
                    "unit": "C",
                    "value": 28.722123104618333,
                    "connection": "pin:4",
                },
            },
            "payload_timestamp": 1712653796,
            "id": "7a54adb9-0477-4dc3-a3ef-ee3caebe43e3",
        },
        {
            "device_id": "ccc-333333",
            "payload": {
                "battery": {"unit": "%", "value": 50},
                "cadence": {"unit": "seconds", "value": 1800},
                "humidity": {
                    "unit": "%",
                    "value": 77.71149880423403,
                    "connection": "pin:6",
                    "precipitation": False,
                },
                "temperature": {
                    "unit": "C",
                    "value": 16.51190194066335,
                    "connection": "pin:4",
                },
            },
            "payload_timestamp": 1712650196,
            "id": "793b00be-e700-49c1-b1cd-cff554c8330a",
        },
        {
            "device_id": "bbb-222222",
            "payload": {
                "battery": {"unit": "%", "value": 50},
                "cadence": {"unit": "seconds", "value": 1800},
                "humidity": {
                    "unit": "%",
                    "value": 32.46805320560854,
                    "connection": "pin:6",
                    "precipitation": False,
                },
                "temperature": {
                    "unit": "C",
                    "value": 29.444982053439933,
                    "connection": "pin:4",
                },
            },
            "payload_timestamp": 1712651996,
            "id": "147a2efe-6c95-4847-954b-e8622542b558",
        },
        {
            "device_id": "fff-666666",
            "payload": {
                "battery": {"unit": "%", "value": 50},
                "cadence": {"unit": "seconds", "value": 1800},
                "humidity": {
                    "unit": "%",
                    "value": 46.384174630660944,
                    "connection": "pin:6",
                    "precipitation": False,
                },
                "temperature": {
                    "unit": "C",
                    "value": 29.579743044393865,
                    "connection": "pin:4",
                },
            },
            "payload_timestamp": 1712651996,
            "id": "ea1d3987-e749-4598-bdb5-91dcddf699e1",
        },
        {
            "device_id": "aaa-111111",
            "payload": {
                "battery": {"unit": "%", "value": 50},
                "cadence": {"unit": "seconds", "value": 1800},
                "humidity": {
                    "unit": "%",
                    "value": 38.00058028676371,
                    "connection": "pin:6",
                    "precipitation": False,
                },
                "temperature": {
                    "unit": "C",
                    "value": 22.474258325222124,
                    "connection": "pin:4",
                },
            },
            "payload_timestamp": 1712650196,
            "id": "03aa88a9-658d-4305-8c9c-e082c8498677",
        },
        {
            "device_id": "ccc-333333",
            "payload": {
                "battery": {"unit": "%", "value": 50},
                "cadence": {"unit": "seconds", "value": 1800},
                "humidity": {
                    "unit": "%",
                    "value": 48.00708912058185,
                    "connection": "pin:6",
                    "precipitation": False,
                },
                "temperature": {
                    "unit": "C",
                    "value": 32.35949167978876,
                    "connection": "pin:4",
                },
            },
            "payload_timestamp": 1712651996,
            "id": "6a16892f-4735-49bd-b821-f05ce5144a10",
        },
        {
            "device_id": "fff-666666",
            "payload": {
                "battery": {"unit": "%", "value": 50},
                "cadence": {"unit": "seconds", "value": 1800},
                "humidity": {
                    "unit": "%",
                    "value": 60.52716333578073,
                    "connection": "pin:6",
                    "precipitation": False,
                },
                "temperature": {
                    "unit": "C",
                    "value": 27.69454741734932,
                    "connection": "pin:4",
                },
            },
            "payload_timestamp": 1712653796,
            "id": "df52c321-0ee8-4936-b83d-63999a45d9b8",
        },
    ]


def assert_thing_payload(
    actual_result: ThingPayload, expected_result: ThingPayload
) -> None:
    assert str(actual_result.id) == expected_result["id"]
    assert actual_result.device_id == expected_result["device_id"]
    assert actual_result.payload_timestamp == expected_result["payload_timestamp"]
    assert actual_result.payload == expected_result["payload"]


def assert_thing_payloads(actual_result: Any, expected_result: Any) -> None:
    assert len(actual_result) == len(expected_result)

    for index in range(len(actual_result) - 1):
        assert_thing_payload(actual_result[index], expected_result[index])
