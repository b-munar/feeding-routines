from flask_restful import Resource
from flask import request

from src.database.session import Session
from src.models.feed_profile_model import FeedProfileModel
from src.schemas.feed_profile_schema import FeedProfileDeserializedSchema, FeedProfileSerializedSchema, FeedProfilesSerializedSchema
from src.utils.authorization import authorization

class FeedProfileController(Resource):
    method_decorators = [authorization]
    def post(self, **kwargs):
        if(request.data):
            request_json = request.get_json()
        else:
            return "", 400
        
        feed_profile_create_schema = FeedProfileDeserializedSchema()
        
        errors = feed_profile_create_schema.validate(request_json)
        if errors:
            print(errors)
            return "", 400
        
        feed_profile_create_dump = feed_profile_create_schema.dump(request_json)
        feed_profile_create_dump["user"] = kwargs["user"]["id"]
        
        # token = kwargs["token"]
        # If you need to use another microservice,
        # use this token with the request library,
        # remember to paste the Bearer before the token
        
        session = Session()
        new_profile = FeedProfileModel(**feed_profile_create_dump)
        session.add(new_profile)
        session.commit()

        feeding_routines_created_schema = FeedProfileSerializedSchema()
        feeding_routines_created_dump = feeding_routines_created_schema.dump(new_profile)
        return feeding_routines_created_dump, 201
    
    def get(self, **kwargs):
        feed_profile_schema = FeedProfileSerializedSchema()

        session = Session()
        query = session.query(FeedProfileModel).filter(FeedProfileModel.user==kwargs["user"]["id"])
        session.close()
        
        profiles = [feed_profile_schema.dump(profile) for profile in query]
        return {"profiles":profiles}, 200


class FeedProfilesController(Resource):
    method_decorators = [authorization]
    def get(self, **kwargs):
        feed_profile_schema = FeedProfilesSerializedSchema()
        if kwargs["user"]["role"] == 2:
            session = Session()
            query = session.query(FeedProfileModel)
            session.close()
            
            profiles = [feed_profile_schema.dump(profile) for profile in query]
            return {"profiles":profiles}, 200
        else:
            return "no eres partner", 401