# coding: utf-8

from marshmallow import Schema, fields, validates, validate, ValidationError
from src.views.schema.fields import LocalDateTimeField


fields.Field.default_error_messages = {
    'required': u'缺少必填数据.',
    'type': u'数据类型不合法.',
    'null': u'数据不能为空.',
    'validator_failed': u'非法数据.'
}


class UserSchema(Schema):
    """用户"""

    id = fields.Integer()
    name = fields.String()
    create_time = LocalDateTimeField()


order_schema_data = UserSchema(strict=True, many=True)

