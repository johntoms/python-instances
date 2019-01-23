# README

> 该环境为 python3 .
## test_timeit.py
> 虽然 python 是一个脚本语言,相对于现在的电脑硬件已不成问题,但当数据量较大的时候一些方法的选择也会影响整体的性能,为了验证某一些方法的快慢,所以
,研究了一下一些简单的方法的快慢.

**起因**

> 为什么是模块timeit ，而不用time模块/timing模块？

模块timeit （而不用time模块/timing模块）time.clock() 精度高，还是使用 time.time() 精度更高，要视乎所在的平台来决定。

总概来讲，在 Unix 系统中，建议使用 time.time()，在 Windows 系统中，建议使用 time.clock()。

python提供timeit.default_timer()默认基于平台选择精度高的记录时间的方法。

**IDLE具体方法**

```markdown
1. timeit
import timeit
timeit.timeit(stmt='pass', setup='pass', timer=<default timer>, number=1000000)

2. repeat

timeit.repeat(stmt='pass', setup='pass', timer=<default timer>, repeat=3, number=1000000)

stmt='pass'  # 要测试时间的语句， 比如“"test()”

setup='pass'  # 测试语句需要的前提环境：“from __main__ import test”

 timer=<default timer>  # 选择时间计时器，默认是timeit.default_timer()；

 repeat=3  # 需要timieit的次数；int

number=1000000  # 测试语句需要循环的次数（算timieit一次）；

详细写法见<code> test_timeit.py </code>
```

**ipython**

```shell
####################################################################
# 测试字典的取值速度快慢
# 解释：可以发现 get 取值方法最慢，[] 取值方式速度是 get 取值的 2 倍左右，
# 没有键的时候次之，但[]取一个不存在的值得时候 python 会抛出异常
# 比较隐晦的写法是加入 try 来处理抛出的异常。
####################################################################

In [2]: a = {"a":"a"}

In [3]: timeit(a.get("a")
101 ns ± 1.01 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

In [4]: timeit(a.get("b"))
104 ns ± 7.57 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

In [5]: timeit(a["a"])
48.6 ns ± 0.763 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)


####################################################################
# 列表表达式取值和调用函数取值的快慢
# 解释：通过比较两种方法的速度基本一致
####################################################################

In [3]: def test():
   ...:     for i in range(10):
   ...:         xx.append(i)
   ...:

In [4]: yy = []

In [5]: xx
Out[5]: []

In [6]: yy
Out[6]: []

In [7]: timeit(test())
1.46 µs ± 20.6 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

In [8]: timeit([yy.append(i) for i in range(10)])
1.78 µs ± 21.2 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

```

## base_python_knowledge

> 该包下为学习和记录常用 python 基础知识



