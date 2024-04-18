import asyncio
import logging

from things_report_job_service.service import ThingsReportJobService

log = logging.getLogger("things_report_job_service")


async def main() -> None:
    log.info("Starting service")

    service = ThingsReportJobService()
    await service.poll()


if __name__ == "__main__":
    asyncio.run(main())
