# /usr/bin/env python
# coding=utf-8
"""
__Author__ = 'JohnToms'
__CreateTime__ = '2019/1/30'

==========================
描述:学习迭代器与生成器的使用
==========================
"""

list1 = [1,2,3,4,5,6]
it = iter(list1)
print(next(it))
print(it.__next__())
for i in it:
    print(i, end=" ")


