import logging

import pytest

log = logging.getLogger("test_things_report_job_service")


class TestException:
    @pytest.mark.skip
    def test_consume_exception(self):
        pass

    @pytest.mark.skip
    def test_produce_exception(self):
        pass
