
from schemas import ThingPayload


def expected_thing_payloads() -> tuple[int, list[ThingPayload]]:
    return 200, [
        {
            "id": "601c61ee-0e30-42dc-9dc0-83c7d2d3bcad",
            "device_id": "aaa-111111",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {"value": 0.0, "unit": "C", "connection": "pin:4"},
                "humidity": {
                    "value": 0.0,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592697600,
        },
        {
            "id": "ad8db732-af2c-4505-aaf8-b1ad7cbe11b2",
            "device_id": "bbb-222222",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {"value": 10.52, "unit": "C", "connection": "pin:4"},
                "humidity": {
                    "value": 50.91,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592697600,
        },
        {
            "id": "c4ea9ab0-4f31-4074-8a23-edc5721455d4",
            "device_id": "ccc-333333",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {"value": 11.37, "unit": "C", "connection": "pin:4"},
                "humidity": {
                    "value": 55.01,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592697600,
        },
        {
            "id": "9f05c3b2-5fcf-41e9-a539-7622a01161c5",
            "device_id": "ddd-444444",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {"value": 1.76, "unit": "C", "connection": "pin:4"},
                "humidity": {
                    "value": 8.54,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592697600,
        },
        {
            "id": "708604d0-1d26-44f2-92e4-9028a2d521ec",
            "device_id": "eee-555555",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {"value": -9.46, "unit": "C", "connection": "pin:4"},
                "humidity": {
                    "value": -45.79,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592697600,
        },
        {
            "id": "e63c4e22-b7b9-4500-8bfb-bd27d568445a",
            "device_id": "fff-666666",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {"value": -11.99, "unit": "C", "connection": "pin:4"},
                "humidity": {
                    "value": -58.01,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592697600,
        },
        {
            "id": "5890a691-ed21-4d23-8183-9e6b3410caa5",
            "device_id": "aaa-111111",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {"value": 5.99, "unit": "C", "connection": "pin:4"},
                "humidity": {
                    "value": 29.01,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592784000,
        },
        {
            "id": "963078a7-7183-47f5-932c-c7aa258ed86a",
            "device_id": "bbb-222222",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {"value": 12.47, "unit": "C", "connection": "pin:4"},
                "humidity": {
                    "value": 60.35,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592784000,
        },
        {
            "id": "cb15515f-76ad-4a43-a1e6-aac2fb49c9cd",
            "device_id": "ccc-333333",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {"value": 7.48, "unit": "C", "connection": "pin:4"},
                "humidity": {
                    "value": 36.21,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592784000,
        },
        {
            "id": "238378fa-0339-46be-83d3-3ff35bc40f4e",
            "device_id": "ddd-444444",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {"value": -4.38, "unit": "C", "connection": "pin:4"},
                "humidity": {
                    "value": -21.22,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592784000,
        },
        {
            "id": "ca59e615-bbdb-41c6-b3be-5917e75a43ed",
            "device_id": "eee-555555",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {"value": -12.22, "unit": "C", "connection": "pin:4"},
                "humidity": {
                    "value": -59.14,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592784000,
        },
        {
            "id": "f80d8017-bfc6-4282-a142-cd51dc68026d",
            "device_id": "fff-666666",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {"value": -8.82, "unit": "C", "connection": "pin:4"},
                "humidity": {
                    "value": -42.69,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592784000,
        },
        {
            "id": "7409dad8-b932-4997-841f-1af5da9921a2",
            "device_id": "aaa-111111",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {"value": 10.52, "unit": "C", "connection": "pin:4"},
                "humidity": {
                    "value": 50.91,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592870400,
        },
        {
            "id": "0563c2b2-7692-4108-89eb-4cfafeee6aa6",
            "device_id": "bbb-222222",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {"value": 11.37, "unit": "C", "connection": "pin:4"},
                "humidity": {
                    "value": 55.01,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592870400,
        },
        {
            "id": "7281fe7d-e297-4513-9f72-d2bba2981874",
            "device_id": "ccc-333333",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {"value": 1.76, "unit": "C", "connection": "pin:4"},
                "humidity": {
                    "value": 8.54,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592870400,
        },
        {
            "id": "7fc1757f-b885-400c-a4e6-96502344ef38",
            "device_id": "ddd-444444",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {"value": -9.46, "unit": "C", "connection": "pin:4"},
                "humidity": {
                    "value": -45.79,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592870400,
        },
        {
            "id": "786d63fa-ef77-4014-a89a-52b67c11370c",
            "device_id": "eee-555555",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {"value": -11.99, "unit": "C", "connection": "pin:4"},
                "humidity": {
                    "value": -58.01,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592870400,
        },
        {
            "id": "b787a0b7-1b9e-4820-a61e-83ddf4500382",
            "device_id": "fff-666666",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {"value": -3.49, "unit": "C", "connection": "pin:4"},
                "humidity": {
                    "value": -16.9,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592870400,
        },
    ]
