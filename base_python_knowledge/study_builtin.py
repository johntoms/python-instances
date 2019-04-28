# /usr/bin/env python
# coding=utf-8
"""
__Author__ = 'JohnToms'
__CreateTime__ = '2019/1/30'
"""

# abs()
"""1. abs() 函数返回数字的绝对值"""
print("abs(-40) ==> ", abs(-40))
print("abs(100.40) ==> ", abs(100.40))
""" 拓展: fabs()和 abs() 的差异
    a. abs() 是一个内置函数，而 fabs() 在 math 模块中定义的。
    b. fabs() 函数只适用于 float 和 integer 类型，而 abs() 也适用于复数。
    >>> import math
    >>> math.fabs(-10)
        10.0
    >>> math.fabs(1+10j)
    Traceback (most recent call last):
    File "<input>", line 1, in <module>
    TypeError: can't convert complex to float
    >>> math.fabs(-1.233)
    >>> 1.233
    >>> abs(1-10j)
    10.04987562112089
    >>> abs(1+1j)   系统将复数转换为距离后取绝对值
    1.4142135623730951
"""


# all()
"""2. all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False"""
# 元素除了是 0、空、None、False 外都算 True。

def my_all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
"""
all() 函数等价于:
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

iterable -- 元组或列表
注意：1. 空元组、空列表返回值为True，这里要特别注意.
     2. 字符串会被转换为元组后,进行迭代,不是直接迭代字符串内的字符    
In [1]: name = ["kangkang", "maria", ""]

In [2]: all(name)
Out[2]: False

In [3]: name1 = ["kangkang", "maria"]

In [4]: all(name1)
Out[4]: True

In [5]: name2 = ["kangkang", "maria", "0"]

In [6]: all(name2)
Out[6]: True

In [7]: name3 = [0,1,2]

In [8]: all(name3)
Out[8]: False

In [9]: all({})
Out[9]: True

In [10]: all([])
Out[10]: True

In [11]: all(set())
Out[11]: True

In [12]: all('')
Out[12]: True

In [13]: all('hello')
Out[13]: True

In [14]: all('helo wsd')
Out[14]: True

In [15]: all('helo     wsd')
Out[15]: True

"""


# any()
"""3. any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True"""
# 元素除了是 0、空、FALSE 外都算 TRUE
def my_any(iterable):
    for element in iterable:
        if element:
            return True
    return False

"""
In [19]: any(['1',2])
Out[19]: True

In [21]: any((0,'',False))
Out[21]: False

In [22]: any(())
Out[22]: False

In [23]: any({})
Out[23]: False

In [24]: any([])
Out[24]: False
"""


# ascii()
"""4. ascii() 函数类似 repr() 函数, 返回一个表示对象的字符串,
    但是对于字符串中的非 ASCII 字符则返回通过 repr() 函数使用
     \\x, \\u 或 \\U 编码的字符。
     生成字符串类似 Python2 版本中 repr() 函数的返回值。
"""
print("你好")
print(ascii("你好"))
print("\u4f60\u597d")


# bin()
"""5. bin() 返回一个整数 int 或者长整数 long int 的二进制表示"""
print(bin(10))


# bool()
"""6. bool() 函数用于将给定参数转换为布尔类型，如果没有参数，返回 False"""
# bool 是 int 的子类
def my_bool(element):
    if element:
        return True
    else:
        return False


# bytearray()
"""7. bytearray() 方法返回一个新字节数组。这个数组里的元素是可变的，并且每个元素的值范围: 0 <= x < 256"""

"""
bytearray()方法
语法：
class bytearray([source[, encoding[, errors]]])
参数:
如果 source 为整数，则返回一个长度为 source 的初始化数组；
如果 source 为字符串，则按照指定的 encoding 将字符串转换为字节序列；
如果 source 为可迭代类型，则元素必须为[0 ,255] 中的整数；
如果 source 为与 buffer 接口一致的对象，则此对象也可以被用于初始化 bytearray。
如果没有输入任何参数，默认就是初始化数组为0个元素。
返回值:
返回新字节数组。

In [25]: bytearray()
Out[25]: bytearray(b'')

In [26]: bytearray("hello", "utf-8")
Out[26]: bytearray(b'hello')

In [27]: bytearray("hello")
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-27-6b948814525b> in <module>
----> 1 bytearray("hello")

TypeError: string argument without an encoding

In [28]: bytearray([1,2,3])
Out[28]: bytearray(b'\x01\x02\x03')

In [29]: byattr([{"a":"b"}, {1:2}])
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-29-2673bc6ca2b8> in <module>
----> 1 byattr([{"a":"b"}, {1:2}])

NameError: name 'byattr' is not defined

In [30]: bytearray([{"a":"b"}, {1:2}])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-30-353cfd8dceef> in <module>
----> 1 bytearray([{"a":"b"}, {1:2}])

TypeError: an integer is required
"""


# bytes()
"""8. bytes 函数返回一个新的 bytes 对象，该对象是一个 0 <= x < 256 区间内的整数不可变序列
      它是 bytearray 的不可变版本"""

"""
语法:
class bytes([source[, encoding[, errors]]])
参数:
如果 source 为整数，则返回一个长度为 source 的初始化数组；
如果 source 为字符串，则按照指定的 encoding 将字符串转换为字节序列；
如果 source 为可迭代类型，则元素必须为[0 ,255] 中的整数；
如果 source 为与 buffer 接口一致的对象，则此对象也可以被用于初始化 bytearray。
如果没有输入任何参数，默认就是初始化数组为0个元素。
返回值:
返回一个新的 bytes 对象。

In [31]: bytes([1,2,3,4])
Out[31]: b'\x01\x02\x03\x04'

In [32]: bytes()
Out[32]: b''

In [33]: bytes('hello', 'utf-8')
Out[33]: b'hello'

In [34]: bytes('hello', 'ascii')
Out[34]: b'hello'

In [35]: bytes([])
Out[35]: b''

"""
# callable()
"""9. callable() 函数用于检查一个对象是否是可调用的。如果返回 True，object 仍然可能调用失败；
      但如果返回 False，调用对象 object 绝对不会成功。
      对于函数、方法、lambda 函式、 类以及实现了 __call__ 方法的类实例, 它都返回 True。"""

"""
语法：
callable(object)
参数
object -- 对象
返回值:
可调用返回 True，否则返回 False。

>>>callable(0)
False
>>> callable("runoob")
False
 
>>> def add(a, b):
...     return a + b
... 
>>> callable(add)             # 函数返回 True
True
>>> class A:                  # 类
...     def method(self):
...             return 0
... 
>>> callable(A)               # 类返回 True
True
>>> a = A()
>>> callable(a)               # 没有实现 __call__, 返回 False
False
>>> class B:
...     def __call__(self):
...             return 0
... 
>>> callable(B)
True
>>> b = B()
>>> callable(b)               # 实现 __call__, 返回 True
True
"""
# chr()
# classmethod()
# compile()
# complex()
# delattr()
# dict()
# dir()
# divmod()
# enumerate()
# eval()
# exec()
# filter()
# float()
# format()
# frozenset()
# getattr()
# globals()
# hasattr()
# hash()
# help()
# hex()
# id()
# input()
# int()
# isinstance()
# issubclass()
# iter()
# len()
# list()
# locals()
# map()
# max()
# memoryview()
# min()
# next()
# object()
# oct()
# open()
# ord()
# pow()
# print()
# property()
# range()
# repr()
# reversed()
# round()
# set()
# setattr()
# slice()
# sorted()
# staticmethod()
# str()
# sum()
# super()
# tuple()
# type()
# vars()
# zip()
# __import__()
