#!/usr/bin/env python
# coding=utf-8
"""
__Author__ = 'JohnToms'
__CreateTime__ = '2019/6/2'
"""

import json
import requests
url = "http://www.eywedu.net/xiaowangzi/index.htm"
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 " \
             "(KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
headers = {"User-Agent": user_agent}


response = requests.request('GET', url=url, headers = headers)
print(response.text)


