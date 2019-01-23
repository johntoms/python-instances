# /usr/bin/env python
# coding=utf-8
"""
__Author__ = 'johntoms'
__CreateTime__ = '2019/1/24'
"""

# 创建列表
list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5, "hello", 9]
list3 = ["a", "b", "c", "d"]

# 访问列表中的值
print("list1[0] ==> ", list1[0])
# 前开后闭  类似于数学里的[1,5) 为1,2,3,4
print("list2[1:5] ==> ", list2[1:5])

# 更新列表
print("第三个元素为 ==> ", list1[2])
list1[2] = 2001
print("更新后的第三个元素为 ==> ", list1[2])

# 删除列表元素
print("原始列表 ==> ", list1)
del list1[2]
print("删除第三个元素 ==> ", list1)

# 计算元素
print("list1的元素个数 ==> ", len(list1))

# 两个列表组合,即相加
print("list1 和 list2 相加后的列表 ==> ", list1 + list2)

# 一个列表加到另一个列表里
list1.extend(list2)
print("list1 和 list2 相加后list1列表 ==> ", list1)

# 元素是否存在于列表中
if 'hello' in list2:
    print("'hello' 是 list1 的某一个元素")

# 列表截取
"""读取第三个元素,目前主流编程语言的起始值都为0,即第一个元素的 index 值都为0"""
print("list3 的第三个元素 ==> ", list3[2])
"""读取倒数第一元素"""
print("list3 的倒数第一个元素 ==> ", list3[-1])
"""读取第二个到最后的元素"""
print("list3 的第二到最后一个元素 ==> ", list3[1:])

# 嵌套列表
list4 = [1, ["hello", "shanghai"], [1, 2, 3], "world"]
"""list4的第二个元素的第二个元素"""
print("list4的第二个元素的第二个元素 ==> ", list4[1][1])

"""列表的方法
1   len(list)
列表元素个数
2   max(list)
返回列表元素最大值
3   min(list)
返回列表元素最小值
4   list(seq)
将元组转换为列表

"""

L1 = [1, 2, 3, 4]
L2 = ["hello", 2, 3, 4]
# 列表元素个数
print("L1的元素个数 ==> ", len(L1))
# 返回列表元素最大值
"""
如果列表不只有数字型数据,会抛出异常如下:
print(max(L2))
Traceback (most recent call last):
  File "/Users/johntoms/github/python-instances/base_python_knowledge/study_list.py", line 72, in <module>
    print(max(L2))
TypeError: '>' not supported between instances of 'int' and 'str'

"""
print("L1列表的最大值 ==> ", L1)
tuple1 = (1,2,34,)
print("tuple1 元组转列表 ==> ", list(tuple1))

"""
1   list.append(obj)
在列表末尾添加新的对象
2   list.count(obj)
统计某个元素在列表中出现的次数
3   list.extend(seq)
在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
4   list.index(obj)
从列表中找出某个值第一个匹配项的索引位置
5   list.insert(index, obj)
将对象插入列表
6   list.pop([index=-1])
移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
7   list.remove(obj)
移除列表中某个值的第一个匹配项
8   list.reverse()
反向列表中元素
9   list.sort(cmp=None, key=None, reverse=False)
对原列表进行排序
10  list.clear()
清空列表
11  list.copy()
复制列表
"""

