from typing import Any

import logging

from schemas import ThingPayload

log = logging.getLogger("test_things_report_job_service")


def create_thing_payloads_data() -> list[ThingPayload]:
    return [
        # {
        #     "device_id": "aaa-111111",
        #     "payload_timestamp": 1712650196,
        #     "payload": {
        #         "cadence": {"value": 1800, "unit": "seconds"},
        #         "battery": {"value": 50, "unit": "%"},
        #         "temperature": {"value": 0, "unit": "C", "connection": "pin:4"},
        #         "humidity": {
        #             "value": 0,
        #             "unit": "%",
        #             "connection": "pin:6",
        #             "precipitation": False,
        #         },
        #     },
        # },
        # {
        #     "device_id": "bbb-222222",
        #     "payload_timestamp": 1712650196,
        #     "payload": {
        #         "cadence": {"value": 1800, "unit": "seconds"},
        #         "battery": {"value": 50, "unit": "%"},
        #         "temperature": {"value": 0, "unit": "C", "connection": "pin:4"},
        #         "humidity": {
        #             "value": 0,
        #             "unit": "%",
        #             "connection": "pin:6",
        #             "precipitation": False,
        #         },
        #     },
        # },
        # {
        #     "device_id": "ccc-333333",
        #     "payload_timestamp": 1712650196,
        #     "payload": {
        #         "cadence": {"value": 1800, "unit": "seconds"},
        #         "battery": {"value": 50, "unit": "%"},
        #         "temperature": {"value": 0, "unit": "C", "connection": "pin:4"},
        #         "humidity": {
        #             "value": 0,
        #             "unit": "%",
        #             "connection": "pin:6",
        #             "precipitation": False,
        #         },
        #     },
        # },
        # {
        #     "device_id": "ddd-444444",
        #     "payload_timestamp": 1712650196,
        #     "payload": {
        #         "cadence": {"value": 1800, "unit": "seconds"},
        #         "battery": {"value": 50, "unit": "%"},
        #         "temperature": {"value": 0, "unit": "C", "connection": "pin:4"},
        #         "humidity": {
        #             "value": 0,
        #             "unit": "%",
        #             "connection": "pin:6",
        #             "precipitation": False,
        #         },
        #     },
        # },
        # {
        #     "device_id": "eee-555555",
        #     "payload_timestamp": 1712650196,
        #     "payload": {
        #         "cadence": {"value": 1800, "unit": "seconds"},
        #         "battery": {"value": 50, "unit": "%"},
        #         "temperature": {"value": 0, "unit": "C", "connection": "pin:4"},
        #         "humidity": {
        #             "value": 0,
        #             "unit": "%",
        #             "connection": "pin:6",
        #             "precipitation": False,
        #         },
        #     },
        # },
        # {
        #     "device_id": "fff-666666",
        #     "payload_timestamp": 1712650196,
        #     "payload": {
        #         "cadence": {"value": 1800, "unit": "seconds"},
        #         "battery": {"value": 50, "unit": "%"},
        #         "temperature": {"value": 0, "unit": "C", "connection": "pin:4"},
        #         "humidity": {
        #             "value": 0,
        #             "unit": "%",
        #             "connection": "pin:6",
        #             "precipitation": False,
        #         },
        #     },
        # },
        # {
        #     "device_id": "aaa-111111",
        #     "payload_timestamp": 1712651996,
        #     "payload": {
        #         "cadence": {"value": 1800, "unit": "seconds"},
        #         "battery": {"value": 50, "unit": "%"},
        #         "temperature": {
        #             "value": 5.992819232552538,
        #             "unit": "C",
        #             "connection": "pin:4",
        #         },
        #         "humidity": {
        #             "value": 29.005245085554282,
        #             "unit": "%",
        #             "connection": "pin:6",
        #             "precipitation": False,
        #         },
        #     },
        # },
        # {
        #     "device_id": "bbb-222222",
        #     "payload_timestamp": 1712651996,
        #     "payload": {
        #         "cadence": {"value": 1800, "unit": "seconds"},
        #         "battery": {"value": 50, "unit": "%"},
        #         "temperature": {
        #             "value": 5.992819232552538,
        #             "unit": "C",
        #             "connection": "pin:4",
        #         },
        #         "humidity": {
        #             "value": 29.005245085554282,
        #             "unit": "%",
        #             "connection": "pin:6",
        #             "precipitation": False,
        #         },
        #     },
        # },
        # {
        #     "device_id": "ccc-333333",
        #     "payload_timestamp": 1712651996,
        #     "payload": {
        #         "cadence": {"value": 1800, "unit": "seconds"},
        #         "battery": {"value": 50, "unit": "%"},
        #         "temperature": {
        #             "value": 5.992819232552538,
        #             "unit": "C",
        #             "connection": "pin:4",
        #         },
        #         "humidity": {
        #             "value": 29.005245085554282,
        #             "unit": "%",
        #             "connection": "pin:6",
        #             "precipitation": False,
        #         },
        #     },
        # },
        # {
        #     "device_id": "ddd-444444",
        #     "payload_timestamp": 1712651996,
        #     "payload": {
        #         "cadence": {"value": 1800, "unit": "seconds"},
        #         "battery": {"value": 50, "unit": "%"},
        #         "temperature": {
        #             "value": 5.992819232552538,
        #             "unit": "C",
        #             "connection": "pin:4",
        #         },
        #         "humidity": {
        #             "value": 29.005245085554282,
        #             "unit": "%",
        #             "connection": "pin:6",
        #             "precipitation": False,
        #         },
        #     },
        # },
        # {
        #     "device_id": "eee-555555",
        #     "payload_timestamp": 1712651996,
        #     "payload": {
        #         "cadence": {"value": 1800, "unit": "seconds"},
        #         "battery": {"value": 50, "unit": "%"},
        #         "temperature": {
        #             "value": 5.992819232552538,
        #             "unit": "C",
        #             "connection": "pin:4",
        #         },
        #         "humidity": {
        #             "value": 29.005245085554282,
        #             "unit": "%",
        #             "connection": "pin:6",
        #             "precipitation": False,
        #         },
        #     },
        # },
        # {
        #     "device_id": "fff-666666",
        #     "payload_timestamp": 1712651996,
        #     "payload": {
        #         "cadence": {"value": 1800, "unit": "seconds"},
        #         "battery": {"value": 50, "unit": "%"},
        #         "temperature": {
        #             "value": 5.992819232552538,
        #             "unit": "C",
        #             "connection": "pin:4",
        #         },
        #         "humidity": {
        #             "value": 29.005245085554282,
        #             "unit": "%",
        #             "connection": "pin:6",
        #             "precipitation": False,
        #         },
        #     },
        # },
        {
            "device_id": "aaa-111111",
            "payload_timestamp": 1712653796,
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {
                    "value": 10.518387310098706,
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": 50.90899458087774,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
        },
        {
            "device_id": "bbb-222222",
            "payload_timestamp": 1712653796,
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {
                    "value": 10.518387310098706,
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": 50.90899458087774,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
        },
        {
            "device_id": "ccc-333333",
            "payload_timestamp": 1712653796,
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {
                    "value": 10.518387310098706,
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": 50.90899458087774,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
        },
        {
            "device_id": "ddd-444444",
            "payload_timestamp": 1712653796,
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {
                    "value": 10.518387310098706,
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": 50.90899458087774,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
        },
        {
            "device_id": "eee-555555",
            "payload_timestamp": 1712653796,
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {
                    "value": 10.518387310098706,
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": 50.90899458087774,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
        },
        {
            "device_id": "fff-666666",
            "payload_timestamp": 1712653796,
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {
                    "value": 10.518387310098706,
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": 50.90899458087774,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
        },
        {
            "device_id": "aaa-111111",
            "payload_timestamp": 1712655596,
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {
                    "value": 12.468687332550681,
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": 60.34844668954529,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
        },
        {
            "device_id": "bbb-222222",
            "payload_timestamp": 1712655596,
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {
                    "value": 12.468687332550681,
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": 60.34844668954529,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
        },
        {
            "device_id": "ccc-333333",
            "payload_timestamp": 1712655596,
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {
                    "value": 12.468687332550681,
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": 60.34844668954529,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
        },
        {
            "device_id": "ddd-444444",
            "payload_timestamp": 1712655596,
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {
                    "value": 12.468687332550681,
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": 60.34844668954529,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
        },
        {
            "device_id": "eee-555555",
            "payload_timestamp": 1712655596,
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {
                    "value": 12.468687332550681,
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": 60.34844668954529,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
        },
        {
            "device_id": "fff-666666",
            "payload_timestamp": 1712655596,
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {
                    "value": 12.468687332550681,
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": 60.34844668954529,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
        },
        {
            "device_id": "aaa-111111",
            "payload_timestamp": 1712657396,
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {
                    "value": 11.366217835321022,
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": 55.01249432295374,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
        },
        {
            "device_id": "bbb-222222",
            "payload_timestamp": 1712657396,
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {
                    "value": 11.366217835321022,
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": 55.01249432295374,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
        },
        {
            "device_id": "ccc-333333",
            "payload_timestamp": 1712657396,
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {
                    "value": 11.366217835321022,
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": 55.01249432295374,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
        },
        {
            "device_id": "ddd-444444",
            "payload_timestamp": 1712657396,
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {
                    "value": 11.366217835321022,
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": 55.01249432295374,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
        },
        {
            "device_id": "eee-555555",
            "payload_timestamp": 1712657396,
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {
                    "value": 11.366217835321022,
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": 55.01249432295374,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
        },
        {
            "device_id": "fff-666666",
            "payload_timestamp": 1712657396,
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {
                    "value": 11.366217835321022,
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": 55.01249432295374,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
        },
        # {
        #     "device_id": "aaa-111111",
        #     "payload_timestamp": 1712659196,
        #     "payload": {
        #         "cadence": {"value": 1800, "unit": "seconds"},
        #         "battery": {"value": 50, "unit": "%"},
        #         "temperature": {
        #             "value": 7.4809018012994555,
        #             "unit": "C",
        #             "connection": "pin:4",
        #         },
        #         "humidity": {
        #             "value": 36.20756471828936,
        #             "unit": "%",
        #             "connection": "pin:6",
        #             "precipitation": False,
        #         },
        #     },
        # },
        # {
        #     "device_id": "bbb-222222",
        #     "payload_timestamp": 1712659196,
        #     "payload": {
        #         "cadence": {"value": 1800, "unit": "seconds"},
        #         "battery": {"value": 50, "unit": "%"},
        #         "temperature": {
        #             "value": 7.4809018012994555,
        #             "unit": "C",
        #             "connection": "pin:4",
        #         },
        #         "humidity": {
        #             "value": 36.20756471828936,
        #             "unit": "%",
        #             "connection": "pin:6",
        #             "precipitation": False,
        #         },
        #     },
        # },
        # {
        #     "device_id": "ccc-333333",
        #     "payload_timestamp": 1712659196,
        #     "payload": {
        #         "cadence": {"value": 1800, "unit": "seconds"},
        #         "battery": {"value": 50, "unit": "%"},
        #         "temperature": {
        #             "value": 7.4809018012994555,
        #             "unit": "C",
        #             "connection": "pin:4",
        #         },
        #         "humidity": {
        #             "value": 36.20756471828936,
        #             "unit": "%",
        #             "connection": "pin:6",
        #             "precipitation": False,
        #         },
        #     },
        # },
        # {
        #     "device_id": "ddd-444444",
        #     "payload_timestamp": 1712659196,
        #     "payload": {
        #         "cadence": {"value": 1800, "unit": "seconds"},
        #         "battery": {"value": 50, "unit": "%"},
        #         "temperature": {
        #             "value": 7.4809018012994555,
        #             "unit": "C",
        #             "connection": "pin:4",
        #         },
        #         "humidity": {
        #             "value": 36.20756471828936,
        #             "unit": "%",
        #             "connection": "pin:6",
        #             "precipitation": False,
        #         },
        #     },
        # },
        # {
        #     "device_id": "eee-555555",
        #     "payload_timestamp": 1712659196,
        #     "payload": {
        #         "cadence": {"value": 1800, "unit": "seconds"},
        #         "battery": {"value": 50, "unit": "%"},
        #         "temperature": {
        #             "value": 7.4809018012994555,
        #             "unit": "C",
        #             "connection": "pin:4",
        #         },
        #         "humidity": {
        #             "value": 36.20756471828936,
        #             "unit": "%",
        #             "connection": "pin:6",
        #             "precipitation": False,
        #         },
        #     },
        # },
        # {
        #     "device_id": "fff-666666",
        #     "payload_timestamp": 1712659196,
        #     "payload": {
        #         "cadence": {"value": 1800, "unit": "seconds"},
        #         "battery": {"value": 50, "unit": "%"},
        #         "temperature": {
        #             "value": 7.4809018012994555,
        #             "unit": "C",
        #             "connection": "pin:4",
        #         },
        #         "humidity": {
        #             "value": 36.20756471828936,
        #             "unit": "%",
        #             "connection": "pin:6",
        #             "precipitation": False,
        #         },
        #     },
        # },
        # {
        #     "device_id": "aaa-111111",
        #     "payload_timestamp": 1712660996,
        #     "payload": {
        #         "cadence": {"value": 1800, "unit": "seconds"},
        #         "battery": {"value": 50, "unit": "%"},
        #         "temperature": {
        #             "value": 1.7640001007483401,
        #             "unit": "C",
        #             "connection": "pin:4",
        #         },
        #         "humidity": {
        #             "value": 8.537760487621966,
        #             "unit": "%",
        #             "connection": "pin:6",
        #             "precipitation": False,
        #         },
        #     },
        # },
        # {
        #     "device_id": "bbb-222222",
        #     "payload_timestamp": 1712660996,
        #     "payload": {
        #         "cadence": {"value": 1800, "unit": "seconds"},
        #         "battery": {"value": 50, "unit": "%"},
        #         "temperature": {
        #             "value": 1.7640001007483401,
        #             "unit": "C",
        #             "connection": "pin:4",
        #         },
        #         "humidity": {
        #             "value": 8.537760487621966,
        #             "unit": "%",
        #             "connection": "pin:6",
        #             "precipitation": False,
        #         },
        #     },
        # },
        # {
        #     "device_id": "ccc-333333",
        #     "payload_timestamp": 1712660996,
        #     "payload": {
        #         "cadence": {"value": 1800, "unit": "seconds"},
        #         "battery": {"value": 50, "unit": "%"},
        #         "temperature": {
        #             "value": 1.7640001007483401,
        #             "unit": "C",
        #             "connection": "pin:4",
        #         },
        #         "humidity": {
        #             "value": 8.537760487621966,
        #             "unit": "%",
        #             "connection": "pin:6",
        #             "precipitation": False,
        #         },
        #     },
        # },
        # {
        #     "device_id": "ddd-444444",
        #     "payload_timestamp": 1712660996,
        #     "payload": {
        #         "cadence": {"value": 1800, "unit": "seconds"},
        #         "battery": {"value": 50, "unit": "%"},
        #         "temperature": {
        #             "value": 1.7640001007483401,
        #             "unit": "C",
        #             "connection": "pin:4",
        #         },
        #         "humidity": {
        #             "value": 8.537760487621966,
        #             "unit": "%",
        #             "connection": "pin:6",
        #             "precipitation": False,
        #         },
        #     },
        # },
        # {
        #     "device_id": "eee-555555",
        #     "payload_timestamp": 1712660996,
        #     "payload": {
        #         "cadence": {"value": 1800, "unit": "seconds"},
        #         "battery": {"value": 50, "unit": "%"},
        #         "temperature": {
        #             "value": 1.7640001007483401,
        #             "unit": "C",
        #             "connection": "pin:4",
        #         },
        #         "humidity": {
        #             "value": 8.537760487621966,
        #             "unit": "%",
        #             "connection": "pin:6",
        #             "precipitation": False,
        #         },
        #     },
        # },
        # {
        #     "device_id": "fff-666666",
        #     "payload_timestamp": 1712660996,
        #     "payload": {
        #         "cadence": {"value": 1800, "unit": "seconds"},
        #         "battery": {"value": 50, "unit": "%"},
        #         "temperature": {
        #             "value": 1.7640001007483401,
        #             "unit": "C",
        #             "connection": "pin:4",
        #         },
        #         "humidity": {
        #             "value": 8.537760487621966,
        #             "unit": "%",
        #             "connection": "pin:6",
        #             "precipitation": False,
        #         },
        #     },
        # },
        # {
        #     "device_id": "aaa-111111",
        #     "payload_timestamp": 1712662796,
        #     "payload": {
        #         "cadence": {"value": 1800, "unit": "seconds"},
        #         "battery": {"value": 50, "unit": "%"},
        #         "temperature": {
        #             "value": -4.384790346120248,
        #             "unit": "C",
        #             "connection": "pin:4",
        #         },
        #         "humidity": {
        #             "value": -21.222385275222,
        #             "unit": "%",
        #             "connection": "pin:6",
        #             "precipitation": False,
        #         },
        #     },
        # },
        # {
        #     "device_id": "bbb-222222",
        #     "payload_timestamp": 1712662796,
        #     "payload": {
        #         "cadence": {"value": 1800, "unit": "seconds"},
        #         "battery": {"value": 50, "unit": "%"},
        #         "temperature": {
        #             "value": -4.384790346120248,
        #             "unit": "C",
        #             "connection": "pin:4",
        #         },
        #         "humidity": {
        #             "value": -21.222385275222,
        #             "unit": "%",
        #             "connection": "pin:6",
        #             "precipitation": False,
        #         },
        #     },
        # },
        # {
        #     "device_id": "ccc-333333",
        #     "payload_timestamp": 1712662796,
        #     "payload": {
        #         "cadence": {"value": 1800, "unit": "seconds"},
        #         "battery": {"value": 50, "unit": "%"},
        #         "temperature": {
        #             "value": -4.384790346120248,
        #             "unit": "C",
        #             "connection": "pin:4",
        #         },
        #         "humidity": {
        #             "value": -21.222385275222,
        #             "unit": "%",
        #             "connection": "pin:6",
        #             "precipitation": False,
        #         },
        #     },
        # },
        # {
        #     "device_id": "ddd-444444",
        #     "payload_timestamp": 1712662796,
        #     "payload": {
        #         "cadence": {"value": 1800, "unit": "seconds"},
        #         "battery": {"value": 50, "unit": "%"},
        #         "temperature": {
        #             "value": -4.384790346120248,
        #             "unit": "C",
        #             "connection": "pin:4",
        #         },
        #         "humidity": {
        #             "value": -21.222385275222,
        #             "unit": "%",
        #             "connection": "pin:6",
        #             "precipitation": False,
        #         },
        #     },
        # },
        # {
        #     "device_id": "eee-555555",
        #     "payload_timestamp": 1712662796,
        #     "payload": {
        #         "cadence": {"value": 1800, "unit": "seconds"},
        #         "battery": {"value": 50, "unit": "%"},
        #         "temperature": {
        #             "value": -4.384790346120248,
        #             "unit": "C",
        #             "connection": "pin:4",
        #         },
        #         "humidity": {
        #             "value": -21.222385275222,
        #             "unit": "%",
        #             "connection": "pin:6",
        #             "precipitation": False,
        #         },
        #     },
        # },
        # {
        #     "device_id": "fff-666666",
        #     "payload_timestamp": 1712662796,
        #     "payload": {
        #         "cadence": {"value": 1800, "unit": "seconds"},
        #         "battery": {"value": 50, "unit": "%"},
        #         "temperature": {
        #             "value": -4.384790346120248,
        #             "unit": "C",
        #             "connection": "pin:4",
        #         },
        #         "humidity": {
        #             "value": -21.222385275222,
        #             "unit": "%",
        #             "connection": "pin:6",
        #             "precipitation": False,
        #         },
        #     },
        # },
    ]


def assert_thing_payload(
    actual_result: ThingPayload, expected_result: ThingPayload
) -> None:
    # assert str(actual_result.id) == expected_result["id"]
    assert actual_result.device_id == expected_result["device_id"]
    assert actual_result.payload_timestamp == expected_result["payload_timestamp"]
    assert actual_result.payload == expected_result["payload"]


def assert_thing_payloads(actual_result: Any, expected_result: Any) -> None:
    assert len(actual_result) == len(expected_result)

    for index in range(len(actual_result) - 1):
        assert_thing_payload(actual_result[index], expected_result[index])
