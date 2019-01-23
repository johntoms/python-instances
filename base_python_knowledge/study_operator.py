# /usr/bin/env python
# coding=utf-8
"""
__Author__ = 'johntoms'
__CreateTime__ = '2019/1/24'
"""

import operator
from functools import reduce

# operator.concat(a, b) 合并a， b 两个对象
sequence = [1, 2, 4]  # 此为列表
sequence_2 = 10, 20, 40  # 此为元组
sequence_1 = [2, 32, 343]
print(sequence)
print(sequence_1)
print("add", "=>", reduce(operator.add, sequence))
print("sub", "=>", reduce(operator.sub, sequence))
print("mul", "=>", reduce(operator.mul, sequence))
print("concat", "=>", operator.concat("spam", "egg"))
# print("repeat", "=>", operator.repeat("spam", 1))
print("getitem", "=>", operator.getitem(sequence, 2))
print("indexOf", "=>", operator.indexOf(sequence_1, 2))
# print("sequenceIncludes", "=>", operator.sequenceIncludes(sequence, 3))
# 合并两个列表
list1 = [sequence, sequence_1, sequence]
content_sequences = reduce(operator.concat, list1)

print(content_sequences)
x = range(1, 5)
print(list(x))
