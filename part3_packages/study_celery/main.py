#!/usr/bin/env python
# coding=utf-8
"""
__Author__ = 'JohnToms'
__CreateTime__ = '2019/4/28'
"""

from celery import Celery

app = Celery('test-task', broker='redis://:dqhid1jida@31@172.81.235.244:6379/1', backend="redis://:dqhid1jida@31@172.81.235.244:6379/2")


@app.task
def add_test(x, y):
    return x + y
