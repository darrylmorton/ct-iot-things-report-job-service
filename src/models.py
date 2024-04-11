from datetime import datetime

from sqlalchemy import Column, String, DATETIME
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import MappedColumn, Mapped

from .database import Base


# mutable_json_type(dbtype=JSONB, nested=True)
class ThingPayloadsModel(Base):
    __tablename__ = "thing_payloads"

    id = Column(String, primary_key=True, index=True)
    device_id = Column(String, nullable=False)
    payload = Column(JSON, nullable=False)
    payload_timestamp = Column(DATETIME, nullable=False)
    # start_timestamp = Column(DATETIME, nullable=False)
    # end_timestamp = Column(DATETIME, nullable=False)
    # updated_at = Column(DATETIME, nullable=False, default=datetime.now())
    # created_at = Column(DATETIME, nullable=False, default=datetime.now())


# updated_at: Mapped[datetime] = MappedColumn(nullable=False, default=datetime.now())
