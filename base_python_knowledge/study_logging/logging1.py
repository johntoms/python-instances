#!/usr/bin/env python
# coding=utf-8
"""
__Author__ = 'JohnToms'
__CreateTime__ = '2019/5/28'
"""
import logging.config
import yaml
import os


def set_logging():
    # 检查是否存在 日志 存放的目录
    if not os.path.exists('./logs'):
        os.mkdir('logs')

    # 检查配置文件是否存在
    config_dir = './config.yaml'
    if not os.path.exists(config_dir):
        raise FileNotFoundError

    # 读取配置文件
    with open(config_dir, 'r') as f:
        config = yaml.safe_load(f.read())

    if config:
        logging.config.dictConfig(config=config)
    else:
        raise IOError("config.yaml file doesn't exist")

    return logging
