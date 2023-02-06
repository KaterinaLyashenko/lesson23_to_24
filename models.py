from marshmallow import Schema, fields, validates_schema, ValidationError

VALID_CMD_COMMANDS = ('filter', 'limit', 'map', 'sort', 'unique')

class RequestSchema(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str(required=True)

    @validates_schema
    def check_all_cmd_valid(self, values: dict[str, str], *args, **kwargs):
        if values['cmd'] not in VALID_CMD_COMMANDS:
            raise ValidationError('"cmd" contains invalid error')

class BatchRequest(Schema):
    queries = fields.Nested(RequestSchema, many=True)
    file_name = fields.Str(required=True)