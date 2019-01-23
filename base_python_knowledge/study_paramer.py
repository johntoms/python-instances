# /usr/bin/env python
# coding=utf-8
"""
__Author__ = 'johntoms'
__CreateTime__ = '2019/1/24'
"""


def func1(*host):
    print(host)


def func2(**kwargs):
    print(kwargs)


def func4(*args):
    print('args:', args)


def func6(x):
    print('*******************')
    print(x)
    for key, value in x.items():
        print(key, value)
    if 'name' in x:
        print('name:', 'yes')
    else:
        print('error')


# * 解包列表
def func3(list1):
    *args, list2 = list1
    print(args, list2)
    list2, *args = list1
    print(args, list2)
    list3, *args, list2 = list1
    print(args, list2, list3)
    print(*list1)
    func4(*list1)


def func5(dict1):
    print(dict1)
    func6(dict1)


if __name__ == '__main__':
    sequence = [1, 2, 3, 'hello']
    dict_1 = {'name': 'kong', 'age': '10'}
    func1(sequence)
    func2(name='kong', age='10')
    func3(sequence)
    func5({'name': 'kong', 'age': '10'})
