# coding=utf-8
import logging
import os
from datetime import date
from logging import Formatter, handlers


def get_file_logger(name):
    logger = logging.getLogger(name)
    # 单例模式，如果已经注册了filehandler，直接返回logger
    if logger.handlers:
        return logger

    formatter = Formatter('%(asctime)s\t%(message)s', '%Y-%m-%d %H:%M:%S')
    log_dir = os.path.join('/var/log/flask', name)
    if not os.path.isdir(log_dir):
        os.makedirs(log_dir)

    filename = os.path.join(log_dir, '{}.log'.format(str(date.today())))
    handler = handlers.TimedRotatingFileHandler(
        filename, when='D', backupCount=7, delay=False, encoding='utf-8')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger


event_logger = get_file_logger('event')
