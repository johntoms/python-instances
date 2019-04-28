#!/usr/bin/env python
# coding=utf-8
"""
__Author__ = 'JohnToms'
__CreateTime__ = '2019/4/28'
"""

from celery import Celery

app = Celery()
print(app)
