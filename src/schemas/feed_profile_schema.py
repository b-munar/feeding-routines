from marshmallow import Schema, fields

class FeedProfileDeserializedSchema(Schema):
    meals_per_day = fields.Integer(required=True)
    alergies = fields.String(required=True)
    health_issues = fields.String(required=True)
    time_to_cook = fields.Integer(required=True)

class FeedProfileSerializedSchema(Schema):
    id = fields.UUID()
    meals_per_day = fields.Integer()
    alergies = fields.String()
    health_issues = fields.String()
    time_to_cook = fields.Integer()
    