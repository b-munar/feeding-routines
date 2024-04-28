from marshmallow import Schema, fields

class MealsDeserializedSchema(Schema):
    breakfast = fields.String()
    dinner= fields.String()
    lunch= fields.String()
    amsnack= fields.String()
    pmsnack = fields.String()

class FoodPlanDaysDeserializedSchema(Schema):
    day = fields.String()
    meals = fields.Nested(MealsDeserializedSchema)
    
class FoodPlanDeserializedSchema(Schema):
    partner = fields.UUID()
    user = fields.UUID()
    days= fields.List(fields.Nested(FoodPlanDaysDeserializedSchema))
    
class MealsSerializedSchema(Schema):
    breakfast = fields.String()
    dinner= fields.String()
    lunch= fields.String()
    amsnack= fields.String()
    pmsnack = fields.String()

class FoodPlanDaysSerializedSchema(Schema):
    day = fields.String()
    meals = fields.List(fields.Nested(MealsDeserializedSchema))
    
class FoodPlanSerializedSchema(Schema):
    partner = fields.UUID()
    user = fields.UUID()
    days= fields.List(fields.Nested(FoodPlanDaysSerializedSchema))