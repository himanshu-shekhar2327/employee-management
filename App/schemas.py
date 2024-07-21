from marshmallow import Schema,fields,validate
class EmployeeSchema(Schema):
    # id=fields.Int(dump_only=True)
    name=fields.Str(required=True,validate=validate.Length(min=1))
    department=fields.Str(requires=True,validate=validate.Length(min=1))
    age=fields.Int(required=True,validate=validate.Range(min=1))