# coding=utf-8

from .filelogger import get_file_logger


__all__ = ['rsyslog']


class RsysLogger(object):
    """重写 rsyslog 日志写本地"""

    @classmethod
    def send(cls, message, tag=None):
        logger = get_file_logger(tag)
        if not tag:
            tag = 'notag'
        logger.info(message)


rsyslog = RsysLogger
