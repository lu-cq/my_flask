# coding: utf-8

"""
    API Schema Fields
    ~~~~~~~~~~~~~~~~~

    This module includes a numbers of fields which is compatible with schema
    classes defined in :class:`marshmallow.Schema`.
"""

from __future__ import absolute_import, unicode_literals

from marshmallow.fields import DateTime
from dateutil.tz import tzlocal


class LocalDateTimeField(DateTime):

    localtime = True

    def _serialize(self, value, *args, **kwargs):
        if value is not None and value.tzinfo is None:
            value = value.replace(tzinfo=tzlocal())
        return super(LocalDateTimeField, self)._serialize(
            value, *args, **kwargs)
