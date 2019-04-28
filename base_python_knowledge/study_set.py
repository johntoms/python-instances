# /usr/bin/env python
# coding=utf-8
"""
__Author__ = 'JohnToms'
__CreateTime__ = '2019/1/29'
"""


"""
集合（set）是一个无序的不重复元素序列。
可以使用大括号 { } 或者 set() 函数创建集合 . 
注意：1. 创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
     2. 集合内不可包含具有 没有 hash 属性的数据,即不可包含字典,列表; 元组可以包含,因为元组属于 hash 数据类型
        TypeError: unhashable type: 'set'/'dict'/'list'

"""

tuple = ('1','2','3')
egg_dict1 = {'value0', 'value1', 'value2'}
egg_dict2 = set(['value1', 'value2', 'value3'])
set1 = set(['1',2,3])
print(type(set1))
print(set1)
print(type(egg_dict1))
print(type(egg_dict2))

print(egg_dict1)
print(egg_dict2)


assert 'value1' in egg_dict1, 'value1 ==> egg_dict1'


basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana', tuple}

print(len(basket), basket)

a = set('hello world')
b = set('hello shanghai')
print(a)
print(b)

# 集合的基本运算

# 集合 a 中包含而集合b中不包含的元素, a 中的特殊元素
print("两个集合的差集: a-b ==> ", a - b)  # 两个集合的差集

# 集合 a 或 b 中包含的所有元素
print("两个集合的合集: a|b ==> ", a | b) # 两个集合的合集

# 集合 a 和 b 中都包含了的元素
print("两个集合的并集: a&b ==> ", a & b)  # 两个集合的并集

# 不同时包含于 a 和 b 的元素
print("两个集合的异或: a^b ==> ", a ^ b)  # 两个集合的异或

# 列表表达式
aaa = {x for x in a if x not in 'aeiou'}
print("列表表达式: aaa ==> ", aaa)


# 集合基本操作


location = {'shanghai', 'beijing', 'hangzhou'}
print("location 的原始值 ==> ", location)
# 1. 一: 添加元素
location.add("guangzhou")
print("location 添加一个广州的元素 ==> ", location)
#    二: 更新元素 ,也可以添加元素，且参数可以是列表，元组，字典等,
#       注意:字典 python 会只取字典的键,不会获取到键所对应的值
location.update(['1', '2'], {"hello": 'how', "a": "b", "location":"hello_yellow_color"})
print("update after: ==> ", location)


name = {'KangKang', 'JohnToms', 'Maria', 'JohnDon'}
print("name 的原始值 ==> ", name)
# 2. 一: 移除元素.remove
name.remove('KangKang')  # 不存在会发生错误
print("name 移除 `KangKang` 元素后 ==> ", name)
#    二: 移除元素.discard
name.discard('Blues')  # 不存在不会发生错误
print("移除 Blues 元素后(Blues 不存在不会报错) ==> ",name)
# 随机删除集合中的一个元素.pop  注意:在脚本模式下删除的元素是随机的,在交互模式下删除的元素,
# 是删除集合的第一个元素(排序后的集合的第一个元素).
name.pop()
print("name 随机删除一个元素后", name)
"""
交互式模式的.pop
>>> name = {'KangKang', 'JohnToms', 'Maria', 'JohnDon'}
>>> name
{'KangKang', 'Maria', 'JohnToms', 'JohnDon'}
>>> name.pop()
'KangKang'
>>> name
{'Maria', 'JohnToms', 'JohnDon'}
>>> name.pop()
'Maria'
>>> name
{'JohnToms', 'JohnDon'}
"""


# 计算集合的元素个数
DB = {'mysql', 'mongodb', 'hbase', 'mariadb', 'sqlserver'}
print('DB中元素原始值 ==> ', DB)
print('DB 集合中元素的个数 ==> ', len(DB))


# 清空集合
DB.clear()
print("清除 DB 中的元素 ==> ",DB, "**** DB 的数据类型 ==> ", type(DB))

"""
方法                              描述
add()                           为集合添加元素
clear()                         移除集合中的所有元素
copy()                          拷贝一个集合
difference()                    返回多个集合的差集
difference_update()             移除集合中的元素，该元素在指定的集合也存在。
discard()                       删除集合中指定的元素
intersection()                  返回集合的交集
intersection_update()           删除集合中的元素，该元素在指定的集合中不存在。
isdisjoint()                    判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
issubset()                      判断指定集合是否为该方法参数集合的子集。
issuperset()                    判断该方法的参数集合是否为指定集合的子集
pop()                           随机移除元素
remove()                        移除指定元素
symmetric_difference()          返回两个集合中不重复的元素集合。
symmetric_difference_update()   移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
union()                         返回两个集合的并集
update()                        给集合添加元素
"""

# 尝试一个比较表难理解的函数 symmetric_difference_update() 是集合对象的函数
xxx = {'hello', 'world', 'shanghai'}
yyy = {'hello', 'Maria', 'John', 'Toms'}
xxx.symmetric_difference_update(yyy)
print("xxx.symmetric_difference_update(yyy) 之后 ==> ", xxx)


