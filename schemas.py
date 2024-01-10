from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Str(dump_only = True)
    email = fields.Str(required = True)
    username = fields.Str(required = True)
    password = fields.Str(required = True, load_only = True)
    first_name = fields.Str()
    last_name = fields.Str()
    # pizza =fields.list()

class PizzaSchema(Schema):
    id = fields.Str (dump_only =True)
    body = fields.Str(required = True)
    timestamp = fields.DateTime(dump_only = True)
    user_id = fields.Str(required = True)
    user = fields.Nested(UserSchema, dumps_only = True)

    class PizzaSchemaNested(PizzaSchema):
        user = fields.Nested(UserSchema, dump_only = True)
    
    class UserSchemaNested(UserSchema):
        user = fields.List(fields.Nested(PizzaSchema), dump_only = True)