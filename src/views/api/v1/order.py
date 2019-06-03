# coding: utf-8

from __future__ import absolute_import, unicode_literals

from flask import jsonify, request, abort, g

from src.views.api.blueprint import create_blueprint
from src.views.schema.order import order_schema_data
from src.models.order import Order


bp = create_blueprint('order', 'v1', package_name=__name__, url_prefix='/order')


@bp.route('/plan')
def get_service_type_label():
    """
    **薪资支付计划**
    """
    order_id = request.args.get('order_id', None)
    if not order_id:
        abort(400, "请求参数不完整")
    order = Order.get(order_id)
    return jsonify(status='success', code=1, data=order_schema_data.dump(order).data)
