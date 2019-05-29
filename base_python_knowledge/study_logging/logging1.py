#!/usr/bin/env python
# coding=utf-8
"""
__Author__ = 'JohnToms'
__CreateTime__ = '2019/5/28'
"""
import logging.config
import yaml
import os
import pprint
base_path = os.path.abspath(os.path.dirname(__file__))

def set_logging():
    # 检查是否存在 日志 存放的目录
    if not os.path.exists('./logs'):
        os.mkdir('logs')

    # 检查配置文件是否存在
    config_dir = base_path + '/config.yaml'
    if not os.path.exists(config_dir):
        raise FileNotFoundError

    # 读取配置文件
    with open(config_dir, 'r') as f:
        config = yaml.safe_load(f.read())

    if config:
        # 设置默认配置日志文件位置 默认位置为：/tmp/debug.log && /tmp/warning.log
        if not config.get('handlers').get('debug_file_handler').get('filename'):
            config['handlers']['debug_file_handler']['filename'] = '/tmp/debug.log'
        if not config.get('handlers').get('warning_file_handler').get('filename'):
            config['handlers']['warning_file_handler']['filename'] = '/tmp/warning.log'

        # 配置文件载入 logging 模块
        logging.config.dictConfig(config=config)
    else:
        raise IOError("config.yaml file doesn't exist")

    return logging
