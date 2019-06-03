# coding: utf-8

from __future__ import unicode_literals, absolute_import


class GBaseError(Exception):
    errno = 2000
    code = 0


class GNetworkTimeout(GBaseError):
    errno = 5001

class TokenExpiresError(GBaseError):
    errno = 4001

class UserNoExistError(GBaseError):
    errno = 4004

