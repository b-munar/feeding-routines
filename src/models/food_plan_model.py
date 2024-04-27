from sqlalchemy import Column, String, DateTime, Float, ForeignKey
from src.database.base import Base
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.postgresql import ARRAY

class MealsModel(Base):
    __tablename__ = 'meals'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    breakfast = Column(String(), nullable=False)
    dinner= Column(String(), nullable=False)
    lunch= Column(String(), nullable=False)
    amsnack= Column(String(), nullable=True)
    pmsnack = Column(String(), nullable=True)
    food_play_days_id = Column(UUID(as_uuid=True),ForeignKey("food_plan_days.id"))
    
class FoodPlanDaysModel(Base):
    __tablename__ = 'food_plan_days'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    food_plan_id = Column(UUID(as_uuid=True),ForeignKey("food_plan.id"))
    day= Column(String(), nullable=False)
    meals = relationship("MealsModel")
    
class FoodPlanModel(Base):
    __tablename__ = 'food_plan'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    partner = Column(UUID(as_uuid=True), nullable=False)
    user=Column(UUID(as_uuid=True), nullable=False)
    days = relationship("FoodPlanDaysModel")
    

