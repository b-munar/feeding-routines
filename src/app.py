from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from src.controllers.ping_controller import Ping
from src.controllers.feed_profile_controller import FeedProfileController, FeedProfilesController
from src.controllers.food_plan_controller import FoodPlanController

def create_app():
    app = Flask(__name__)
    CORS(app)
    api = Api(app)
    api.add_resource(Ping, '/feeding-routines/ping')
    api.add_resource(FeedProfileController, '/feeding-routines')
    api.add_resource(FeedProfilesController, '/feeding-routines/sportmen')
    api.add_resource(FoodPlanController, '/feeding-routines/foodplan')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=80, host='0.0.0.0')
else:
    gunicorn_app = create_app()