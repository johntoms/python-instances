# /usr/bin/env python
# coding=utf-8
"""
__Author__ = 'johntoms'
__CreateTime__ = '2019/1/23'

===================================
描述:测试 python 的某一个方法所执行的时间
===================================
"""

import timeit


a = {"a": 1}
print("a.get('a') ==> time:", timeit.timeit('a.get("a")', setup="from __main__ import a", number=1000000))
print("a.get('b') ==> time:", timeit.timeit('a.get("b")', setup="from __main__ import a", number=1000000))
print("a['a'] ==> time:", timeit.timeit('a["a"]', setup="from __main__ import a", number=1000000))


"""
a.get('a') ==> time: 0.128667385
a.get('b') ==> time: 0.08460908200000003
a['a'] ==> time: 0.036344544000000034

结论: [] 取值方式较快,get 方式取值较慢,速度大约快3倍左右,但在 ipython 中操作时,时间大约快两倍左右.
"""

print(timeit.repeat("sum(range(1,100001))", repeat=5, number=1000))


"""
[2.4986444170000004, 2.465794775, 2.466312413, 2.466779659, 2.490320572]
"""

