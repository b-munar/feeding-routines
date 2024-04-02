from flask_restful import Resource
from flask import request

from src.database.session import Session
from src.models.feed_profile_model import FeedProfileModel
from src.schemas.feed_profile_schema import FeedProfileDeserializedSchema, FeedProfileSerializedSchema
from src.utils.authorization import authorization

class NoteController(Resource):
    method_decorators = [authorization]
    def post(self, **kwargs):
        if(request.data):
            request_json = request.get_json()
        else:
            return "", 400
        
        feed_profile_create_schema = FeedProfileDeserializedSchema()
        
        errors = feed_profile_create_schema.validate(request_json)
        if errors:
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

        note_created_schema = FeedProfileSerializedSchema()
        note_created_dump = note_created_schema.dump(new_profile)
        return note_created_dump, 201
    
    def get(self, **kwargs):
        feed_profile_schema = FeedProfileSerializedSchema()

        session = Session()
        query = session.query(FeedProfileModel).filter(FeedProfileModel.user==kwargs["user"]["id"])
        session.close()
        
        profiles = [feed_profile_schema.dump(profile) for profile in query]
        return profiles, 200
