# /usr/bin/env python
# coding=utf-8
"""
__Author__ = 'johntoms'
__CreateTime__ = '2019/1/23'
"""

# map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回。


# egg-1

def func1(x):
    return x*x


def upper(x):
    return x['name'].upper()


# 转换成另一个 list
def map_test1():
    sequence = [1, 2, 3, 4, 5, 6]
    x = map(func1, sequence)
    print(list(x))  # 输出列表
    # print(tuple(x))  # 输出元组


# 对列表里的字典操作
# 函数一定要能够处理列表中的元素，该函数操作的对象应该是元素，着眼于元素的操作
def map_test2():
    people = [{'name': 'kong', 'age': 20}, {'name': 'john', 'age': 30}, {'name': 'toms', 'age': 40}]
    print(list(map(upper, people)))


if __name__ == '__main__':
    # map_test1()
    map_test2()

