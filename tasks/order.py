# coding=utf8

from src.app import CELERY


@CELERY.task
def test(m, n):
    """celery test
    """
    print('m+n=', m+n)
    return None
