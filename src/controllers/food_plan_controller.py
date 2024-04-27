from flask_restful import Resource
from flask import request
import requests
import os

from src.database.session import Session
from src.models.food_plan_model import FoodPlanModel, FoodPlanDaysModel, MealsModel
from src.schemas.food_plan_schema import FoodPlanSerializedSchema, FoodPlanDeserializedSchema
from src.utils.authorization import authorization

class FoodPlanController(Resource):
    method_decorators = [authorization]
    def post(self, **kwargs):
        if(request.data):
            request_json = request.get_json()
        else:
            return "", 400
        
        food_plan_create_schema = FoodPlanDeserializedSchema()
        
        errors = food_plan_create_schema.validate(request_json)
        if errors:
            print(errors)
            return "", 400
        
        food_plan_create_dump = food_plan_create_schema.dump(request_json)
        food_plan_create_dump["partner"] = kwargs["user"]["id"]
        
        # token = kwargs["token"]
        # If you need to use another microservice,
        # use this token with the request library,
        # remember to paste the Bearer before the token
        
        session = Session()
        new_food_plan = FoodPlanModel(user=food_plan_create_dump["user"],partner=food_plan_create_dump["partner"] )
        session.add(new_food_plan)
        session.flush()
        print(food_plan_create_dump)
        for day in food_plan_create_dump["days"]:
            new_day = FoodPlanDaysModel(day=day["day"], food_plan_id = new_food_plan.id)
            session.add(new_day)
            session.flush() 
            new_meal = MealsModel(food_plan_days_id= new_day.id,breakfast=day["meals"]["breakfast"],lunch=day["meals"]["lunch"],dinner=day["meals"]["dinner"])
            session.add(new_meal)
            session.flush()
        session.commit()

        food_plan_created_schema = FoodPlanSerializedSchema()
        training_plan_created_dump = food_plan_created_schema.dump(new_food_plan)
        return training_plan_created_dump, 201
    
    def get(self, **kwargs):
        food_plan_schema = FoodPlanSerializedSchema()
        session = Session()
        if kwargs["user"]["role"] == 1:
            user = FoodPlanModel.user==kwargs["user"]["id"]
        else:
            user = FoodPlanModel.user==kwargs["user"]["id"]
        query = session.query(FoodPlanModel).filter(user)
        session.close()
        
        plans = [food_plan_schema.dump(plan) for plan in query]
        return {"plans":plans}, 200


class FeedProfilesController(Resource):
    method_decorators = [authorization]
    def get(self, **kwargs):
        feed_profile_schema = FoodPlanSerializedSchema()
        if kwargs["user"]["role"] == 1:
            session = Session()
            query = session.query(FoodPlanModel)
            session.close()
            
            profiles = [feed_profile_schema.dump(profile) for profile in query]

            for pro in profiles: 

                token = request.headers.get("Authorization").split(" ")[1]
                
                headers = {"Content-Type": "application/json", 
                           "Accept": "application/json",
                        "Authorization": f"Bearer {token}"
                        }

                reqUrl = os.getenv('SPORT_HOST')+":"+os.getenv('SPORT_PORT')+os.getenv('SPORT_PATH_GET')
                json_data = {"user": pro["user"]}
                response = requests.request("POST", reqUrl, json=json_data, headers=headers)
                pro["user_info"] = response.json()


            return {"profiles":profiles}, 200
        else:
            return "no eres partner", 401