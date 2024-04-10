from sqlalchemy import select

from .schemas import ThingPayload
from .database import async_session
from .models import ThingPayloadsModel


async def find_thing_payloads() -> list[ThingPayload]:
    async with async_session() as session:
        async with session.begin():
            stmt = select(ThingPayloadsModel)
            result = await session.execute(stmt)
            await session.close()

            return result.scalars().all()


# async def find_thing_payloads_by_timestamps(start_timestamp: str, end_timestamp: str) -> list[ThingPayload]:
#     async with async_session() as session:
#         async with session.begin():
#             stmt = (
#                 select(ThingPayloadsModel)
#                 .filter(
#                     ThingPayloadsModel.start_timestamp >= start_timestamp and
#                     ThingPayloadsModel.end_timestamp <= end_timestamp
#                 )
#                 .limit(300)
#             )
#             result = await session.execute(stmt)
#             await session.close()
#
#             return result.scalars()
