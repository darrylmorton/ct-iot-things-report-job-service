import logging

from things_report_job_service.service import ThingsReportJobService

log = logging.getLogger("things_report_job_service")


def main() -> None:
    log.info("Starting service")

    service = ThingsReportJobService()
    service.poll()


if __name__ == "__main__":
    main()
