#!/usr/bin/env python
# coding=utf-8
"""
__Author__ = 'JohnToms'
__CreateTime__ = '2019/5/28'
"""
import time
from functools import wraps
"""
修饰器：可以在不修改目标函数代码的前提下, 在目标函数执行前后增加一些额外功能。
"""


def time_it(fn):
    print('time_it is executed')

    @wraps(fn)
    def new_fn(*args):
        start = time.time()
        result = fn(*args)
        end = time.time()
        duration = end - start
        print('%s seconds are consumed in executing function:%s%r' % (duration, fn.__name__, args))
        return result
    return new_fn


def time_it_args(keep_meta=True):
    def real_func(fn):
        if not isinstance(keep_meta, bool):
            raise KeyError('should be bool')
        if keep_meta :

            @wraps(fn)
            def new_fn(*args):
                start = time.time()
                result = fn(*args)
                end = time.time()
                duration = end - start
                print('%s seconds are consumed in executing function:%s%r' % (duration, fn.__name__, args))
                return result
        else:
            def new_fn(*args):
                start = time.time()
                result = fn(*args)
                end = time.time()
                duration = end - start
                print('%s seconds are consumed in executing function:%s%r' % (duration, fn.__name__, args))
                return result
        return new_fn
    return real_func


@time_it
def acc1(start, end):
    s = 0
    for i in range(start, end):
        s += i
    return s


def acc2(start, end):
    s = 0
    for i in range(start, end):
        s += i
    return s


print("------------------ keep_meta = True ----------------------")


@time_it_args(keep_meta=True)
def print_t():
    print("hello")


print("------------------ keep_meta = False ---------------------")


@time_it_args(keep_meta=False)
def print_t_args():
    print("world")

#print(acc1)
#print(acc2)

print(acc2)
print(acc1)
print_t()
print_t_args()
"""
关键字：函数，不对函数的返回结果做修改，在模块加载时执行修饰器函数
结论：
可以看出, 修饰器是一个函数, 它需要返回一个新的function(示例中的new_fn). 

作用：
函数通常在被修饰函数(示例中的acc1)执行前后进行一些额外的操作, 例如计时. 这个新的函数一般不会修改被修饰函数的返回结果.

执行时机
在模块加载时就会执行修饰器函数, 生成一个个被修饰的新的函数
```
>>> import base_python_knowledge.study_decorator
time_it is executed
<function acc2 at 0x10ecce2f0>
<function time_it.<locals>.new_fn at 0x10ecce268>
```
---------------------------------------------------
第二和第三行的输出可以看出被修饰后的函数已经不是原来的函数了.
实际上, acc1=time_it(acc1). 这样带来的坏处时屏蔽了原函数的元信息, 
例如__name__, __doc__. 如果要保留原函数的信息, 可使用标准库中的修饰器`functools.wrap`:
def time_it(fn):
    print ('time_it is executed')
    @functools.wraps(fn) #########################
    def new_fn(*args, **kws):
        start = time.time()
        result = fn(*args, **kws)
        end = time.time()
        duration = end - start
        print('%s seconds are consumed in executing function:%s%r'\
              %(duration, fn.__name__, args))
        return result

    return new_fn
--------------------------------------------------
作者：Daniel2333 
来源：CSDN 
原文：https://blog.csdn.net/weixin_35653315/article/details/78052023 


再次执行：
```
>>> import base_python_knowledge.study_decorator
time_it is executed
<function acc2 at 0x108cea840>
<function acc1 at 0x108cea7b8>
```


目前看的比较浅，有更深入的理解再来更新。
"""
