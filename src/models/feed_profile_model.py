from sqlalchemy import Column, String, DateTime, Integer
from src.database.base import Base
from datetime import datetime, timezone
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID

class FeedProfileModel(Base):
    __tablename__ = 'feed_profile'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user = Column(UUID(as_uuid=True), nullable=False)
    meals_per_day = Column(Integer(), nullable=False)
    alergies = Column(String(), nullable=False)
    health_issues = Column(String(), nullable=False)
    time_to_cook = Column(String(), nullable=False)
