from sqlalchemy import select

from schemas import ThingPayload
from database import async_session
from models import ThingPayloadModel


async def find_thing_payloads_by_timestamps(
    start_timestamp: int, end_timestamp: int
) -> list[ThingPayload]:
    async with async_session() as session:
        async with session.begin():
            stmt = (
                select(ThingPayloadModel)
                .filter(
                    ThingPayloadModel.payload_timestamp.between(
                        start_timestamp, end_timestamp
                    )
                )
                .limit(300)
            )
            result = await session.execute(stmt)
            await session.close()

            return result.scalars().all()
