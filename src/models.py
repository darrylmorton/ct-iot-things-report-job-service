from sqlalchemy import Column, String, DATETIME
from sqlalchemy.dialects.postgresql import JSON

from database import Base


class ThingPayloadModel(Base):
    __tablename__ = "thing_payloads"

    id = Column(String, primary_key=True, index=True)
    device_id = Column(String, nullable=False)
    payload = Column(JSON, nullable=False)
    payload_timestamp = Column(DATETIME, nullable=False)
    updated_at = Column(DATETIME, nullable=False)
    created_at = Column(DATETIME, nullable=False)
