# /usr/bin/env python
# coding=utf-8
"""
__Author__ = 'johntoms'
__CreateTime__ = '2019/1/25'
"""

"""
Python2 的关键字
Python 2.7.10 (default, Aug 17 2018, 19:45:58)
[GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.0.42)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import keyword
>>> keyword.kwlist
['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> keyword.iskeyword("nonlocal")
False
>>>
python3 的关键字
import keyword
keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
keyword.iskeyword("as")
True
keyword.iskeyword("ass")
False
keyword.iskeyword("async")
True

"""

key_word2 = ['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']
key_word3 = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await','break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except','finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda','nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
print("key_word2 的个数 ==> ", len(key_word2))
print("key_word3 的个数 ==> ", len(key_word3))
all_key_words = set(key_word2).union(key_word3)
print(all_key_words, len(all_key_words))
print("python3 新增的关键字 ==> ", all_key_words - set(key_word2))
print("Python2 减少的关键字 ==> ", all_key_words - set(key_word3))


aa = None
if not aa:
    print("为空", aa)
    print(type(aa))


""" 1. python3 取消了关键字 print ,在 python2中的 print "hello world" 语法,在 python3中已无法使用.python3 中 print为内置函数出现.
    2. nonlocal 不是局部变量,调用全局变量,在闭包中使用较多,
    3. async await 作为异步和同步调用的方法
"""


# [out]
# ['nonlocal', 'async', 'True', 'False', 'print', 'exec', 'None', 'await']
