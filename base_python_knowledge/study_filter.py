# /usr/bin/env python
# coding=utf-8
"""
__Author__ = 'johntoms'
__CreateTime__ = '2019/1/24'
"""


# filter()函数是 Python 内置的另一个有用的高阶函数，filter()函数接收一个函数 f 和一个list，这个函数 f 的作用是对每个元素进行判断，
# 返回 True或 False，filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list,和map函数一样，
# 在python3中要返回list列表，那么必须用list作用于filter。


############
#  多到少  ##
############


list_1 = [
    {'name': 'kona', 'age': 10, 'sex': 'men'},
    {'name': 'konb', 'age': 11, 'sex': 'men'},
    {'name': 'konc', 'age': 9, 'sex': 'female'},
    {'name': 'kond', 'age': 20, 'sex': 'men'},
    {'name': 'kone', 'age': 1, 'sex': 'female'}
]


# 统计男性的姓名
# 如果返回值为非空，则返回整个元素
def count_sex(data):
    if data['sex'] == 'men':
        return True

# 过滤为空的名字


if __name__ == '__main__':
    men_amount = list(filter(count_sex, list_1))
    print(men_amount)
    print(len(men_amount))
