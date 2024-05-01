import asyncio

from config import get_logger
from things_report_job_service.service import ThingsReportJobService

log = get_logger()


async def main() -> None:
    log.info("Starting service")

    service = ThingsReportJobService()
    await service.poll()


if __name__ == "__main__":
    asyncio.run(main())
