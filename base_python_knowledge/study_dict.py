# /usr/bin/env python
# coding=utf-8
"""
__Author__ = 'johntoms'
__CreateTime__ = '2019/1/23'
"""



# python 字典 详细信息： http://www.runoob.com/python/python-dictionary.html

# 字典常用的内置函数
# dict.popitem() 随机返回并删除字典中的一对键和值
# dict.pop(key[,default]) 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
# dict.update(age=100, sex='female') 更新键age：100， sex：female
# dict.get(key, default=None) 返回指定键的值，如果值不在字典中返回default值
# dict.clear() 删除字典内所有元素 # dict1.clear() dict.clear(dict1)
# dict.copy() 返回一个字典的浅复制
# dict.fromkeys(seq[, val]) 创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值
def fromkeys():
    seq = ('Google', 'Runoob', 'Taobao')

    dict_new_1 = dict.fromkeys(seq)
    print("新字典为 : %s" % str(dict_new_1))

    dict_new_2 = dict.fromkeys(seq, 10)
    print("新字典为 : %s" % str(dict_new_2))


# dict.items() 以列表返回可遍历的(键, 值) 元组数组
# dict.keys() 以列表返回一个字典所有的键
# dict.values() 以列表返回字典中的所有值
# dict.setdefault(key, default=None) 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default


dict1 = {'name': 'kong', 'age': 10, 'sex': 'men'}
dict1.setdefault('class', 'female')
print('$$$$$$$$$$$$$$')
print(dict1)
# 访问dict内的值
print('name:', dict1['name'], 'age: ', dict1['age'], 'sex: ', dict1['sex'])

# 修改字典里的值
dict1['name'] = 'Hua'
dict1.update(age=100, sex='female')
print(dict1)
dict1.setdefault('class')
print('*****************')
print(dict1)
# 删除 字典里的 建值
x = dict1.pop('name1', 'NoKey')  # 如果不存在，设置一个默认的返回值，如果不设置则会报错
print(x)

y = dict1.pop('name')  # 如果删除成功，返回对应的值
print(y)
# del dict1['sex']
print(dict1)
print(dict1.popitem())  # 随机删除一个键值对
print(dict1)
# dict1.clear()
dict.clear(dict1)
print(dict1)
del dict1   # 删除整个变量 再次打印会报错


# 字典键的特性
# 字典值可以没有限制地取任何python对象，既可以是标准的对象，也可以是用户定义的，但键不行。
#
# 两个重要的点需要记住：
#
# 1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住。


def func1():
    dict2 = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}

    print("dict2['Name']: ", dict2['Name'])
    # result ==> dict['Name']: Manni

# 2）键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行。


def func2():
    dict3 = {['Name']: 'Zara', 'Age': 7}

    print("dict['Name']: ", dict3['Name'])
    # result ==> TypeError: list objects are unhashable


if __name__ == '__main__':
    fromkeys()

