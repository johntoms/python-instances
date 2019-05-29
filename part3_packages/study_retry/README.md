# Project description
 
![https://pypip.in/d/retry/badge.png](https://pypip.in/d/retry/badge.png)
![https://pypip.in/v/retry/badge.png](https://pypip.in/v/retry/badge.png)
![https://pypip.in/license/retry/badge.png](https://pypip.in/license/retry/badge.png)


Easy to use retry decorator. 

[pypip.org源文地址](https://pypi.org/project/retry/)

## Features
- No external dependency (stdlib only).
- (Optionally) Preserve function signatures (pip install decorator).
- Original traceback, easy to debug. 


## Installation
```
$ pip install retry 
```
## API
### retry decorator
```
def retry(exceptions=Exception, tries=-1, delay=0, max_delay=None,backoff=1, jitter=0, logger=logging_logger): 
    """Return a retry decorator.
    
        :param exceptions: an exception or a tuple of exceptions to catch. default: Exception.
        :param tries: the maximum number of attempts. default: -1 (infinite).
        :param delay: initial delay between attempts. default: 0.
        :param max_delay: the maximum value of delay. default: None (no limit).
        :param backoff: multiplier applied to delay between attempts. default: 1 (no backoff).
        :param jitter: extra seconds added to delay between attempts. default: 0.
                       fixed if a number, random if a range tuple (min, max)
        :param logger: logger.warning(fmt, error, delay) will be called on failed attempts.
                       default: retry.logging_logger. if None, logging is disabled.
        """
        
    
    ## 中文翻译
    """
    返回一个重试装饰器。

    :捕获的异常信息:要捕获的异常或异常元组。默认值:Excpeption。
    :重试的次数:最大尝试次数。默认值:-1(无限)。
    :延迟时间:尝试之间的初始延迟。默认值:0。
    :最大延迟时间:延迟的最大值。默认值:None(没有限制)。
    :延迟之间的时间差距:用于尝试之间延迟的乘数。默认值:1(没有时间间隔差距)。
    :抖动时间:在两次尝试之间增加额外的延迟秒。默认值:0。
    如果是一个数字，则为固定值，如果为一个范围元组(最小，最大)，则采用范围内的随机数。
    :日志配置参数:记录器。失败尝试时将发出警告(fmt、错误、延迟)。
    默认值:retry.logging_logger。如果没有，则禁用日志记录。
"""
```
Various retrying logic can be achieved by combination of arguments.

### Examples 
```
from retry import retry @retry()
def make_trouble():
    '''Retry until  succeed'''
```

```
@retry(ZeroDivisionError, tries=3, delay=2)
def make_trouble():
    '''Retry on ZeroDivisionError, raise error after 3 attempts, sleep 2
seconds between attempts.'''
```

```
 @retry((ValueError, TypeError), delay=1, backoff=2)
 def make_trouble():
    '''Retry on ValueError or TypeError, sleep 1, 2, 4, 8,
... seconds between attempts.'''
```


```
@retry((ValueError, TypeError), delay=1, backoff=2, max_delay=4)
def make_trouble(): '''Retry on ValueError or TypeError, sleep 1, 2,
   4, 4, ... seconds between attempts.'''
```


```
@retry(ValueError, delay=1,jitter=1) def make_trouble():
    '''Retry on ValueError, sleep 1, 2, 3, 4, ... seconds between attempts.'''

```
```
# If you enable logging, you can get warnings like 'ValueError, retrying in
# 1 seconds'
if __name__ == '__main__':
    import logging
    logging.basicConfig()
    make_trouble()
```
## retry_call
```
def retry_call(f, fargs=None, fkwargs=None, exceptions=Exception,tries=-1, delay=0, max_delay=None, backoff=1, jitter=0,logger=logging_logger):
    """ Calls a function and re-executes it if it failed.

    :param f: the function to execute.
    :param fargs: the positional arguments of the function to execute.
    :param fkwargs: the named arguments of the function to execute.
    :param exceptions: an exception or a tuple of exceptions to catch. default: Exception.
    :param tries: the maximum number of attempts. default: -1 (infinite).
    :param delay: initial delay between attempts. default: 0.
    :param max_delay: the maximum value of delay. default: None (no limit).
    :param backoff: multiplier applied to delay between attempts. default: 1 (no backoff).
    :param jitter: extra seconds added to delay between attempts. default: 0.
                   fixed if a number, random if a range tuple (min, max)
    :param logger: logger.warning(fmt, error, delay) will be called on failed attempts.
                   default: retry.logging_logger. if None, logging is disabled.
    :returns: the result of the f function.
    """
    
    
    ## 中文翻译
    """
    调用函数并在函数失败时重新执行它。
    
    :参数f:要执行的函数。
    :param fargs:要执行的函数的位置参数。
    :param fkwargs:要执行的函数的命名参数。
    :param exceptions:要捕获的异常或异常元组。默认值:例外。
    :param try:最大尝试次数。默认值:1(无限)。
    :param delay:尝试之间的初始延迟。默认值:0。
    :param max_delay:延迟的最大值。默认值:None(没有限制)。
    :param backoff:用于尝试之间延迟的乘数。默认值:1(没有后退)。
    :param jitter:在两次尝试之间增加额外的延迟秒。默认值:0。
    固定如果一个数字，随机如果一个范围元组(最小，最大)
    :param logger:记录器。失败尝试时将发出警告(fmt、错误、延迟)。
    默认值:retry.logging_logger。如果没有，则禁用日志记录。
    :returns:f函数的结果。
    """
```


This is very similar to the decorator, except that it takes a function and its arguments as parameters. The use case behind it is to be able to dynamically adjust the retry arguments.

这与decorator非常相似，只是它接受一个函数及其参数作为参数。它背后的用例是能够动态调整重试参数。

```
import requests

from retry.api import retry_call


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

what_is_my_ip("conservative")
```