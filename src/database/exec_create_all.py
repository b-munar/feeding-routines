from src.database.base import Base
from src.database.engine import engine

from src.models.feed_profile_model import FeedProfileModel
from src.models.food_plan_model import FoodPlanModel, FoodPlanDaysModel, MealsModel

table_objects = [FeedProfileModel.__table__, FoodPlanModel.__table__, FoodPlanDaysModel.__table__, MealsModel.__table__]

if __name__ == "__main__":
    Base.metadata.create_all(
        bind = engine(), 
        tables=table_objects,
        checkfirst=True
    )