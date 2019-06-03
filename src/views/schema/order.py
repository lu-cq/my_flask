# coding: utf-8

from marshmallow import Schema, fields, validates, validate, ValidationError
from src.views.schema.fields import LocalDateTimeField
from .user import UserSchema


fields.Field.default_error_messages = {
    'required': u'缺少必填数据.',
    'type': u'数据类型不合法.',
    'null': u'数据不能为空.',
    'validator_failed': u'非法数据.'
}


class OrderSchema(Schema):
    """订单"""

    id = fields.Integer()
    user_id = fields.Int()
    create_time = LocalDateTimeField()
    user = fields.Nested(UserSchema)


order_schema_data = OrderSchema(strict=True, many=True)

