#!/usr/bin/env python
# coding=utf-8
"""
__Author__ = 'JohnToms'
__CreateTime__ = '2019/5/29'
"""
import requests


from retry import retry
from retry.api import retry_call

from base_python_knowledge.study_logging.logging1 import set_logging
logging = set_logging()

retry_requests = retry(exceptions=Exception, tries=3, delay=1,max_delay=5, backoff=2, jitter=1, logger=logging.getLogger('simpleExample'))
# retry_call_requests = retry_call()

@retry_requests
def test_func():
    # 注意此处请不要使用try except ，如果用 try，则不会进行重试操作。
    division = 1/0


def make_trouble(service, info=None):
    if not info:
        info = ''
    r = requests.get(service + info)
    return r.text


def what_is_my_ip(approach=None):
    if approach == "optimistic":
        tries = 1
    elif approach == "conservative":
        tries = 3
    else:
        # skeptical
        tries = -1
    result = retry_call(make_trouble, fargs=["http://ipinfo.io/"], fkwargs={"info": "ip"}, tries=tries)
    print(result)


if __name__ == '__main__':
    test_func()
    what_is_my_ip("conservative")


