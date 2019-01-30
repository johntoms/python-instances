# /usr/bin/env python
# coding=utf-8
"""
__Author__ = 'JohnToms'
__CreateTime__ = '2019/1/29'
"""

import cmath

"""
Python 数字数据类型用于存储数值。

数据类型是不允许改变的,这就意味着如果改变数字数据类型的值，将重新分配内存空间。

del 语句删除单个或多个对象的引用
del var_a, var_b
"""

# 藏在 python 中常见的数学数字 π 和 自然数
print("e = ", cmath.e, cmath.pi)

"""
整型(Int)             通常被称为是整型或整数，是正或负整数，不带小数点。Python3 整型是没有限制大小的
                    可以当作 Long 类型使用，所以 Python3 没有 Python2 的 Long 类型。
浮点型(float)        浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）
复数((complex))      复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示,
                    复数的实部a和虚部b都是浮点型。
"""
a= '1'
print(int(a), type(int(a)))
number1 = 12
number2 = complex(10, 1)
number3 = complex(1, 10)
print(10 * (pow(16, 3)) + 12 * (pow(16, 2)) + 7 * 16 + 8)

# 默认会转换为十进制类型的数据输出
# 数据强制转换输出
print("十六进制 number1=", number1)
print("二进制的 number1=", bin(number1))
print("八进制的 number1=", oct(number1))

# 复数
print(number2 + number3)
print(1 + 2j)
a = 10 + 1j
b = 1 + 10j
print(a + b, type(a + b))

"""
int     float       complex
10      0.0         3.14j
100     15.20       45.j
-786    -21.9       9.322e-36j
080     32.3+e18    .876j
-0490   -90.        -.6545+0J
-0x260  -32.54e100  3e+26J
0x69    70.2-E12    4.53e-7j
"""

print("2+2=", 2+2)
print("2*2=", 2*2)
print("2/2=", 2/2)  # 整数除法返回浮点型 在 python2中为整除取整
print("2.0/2=", 2.0/2)
print("3/2=", 3/2)  # 在 python2中/代表整除,相当于 python3 中的//,整数除法返回向下取整后的结果
print("3//2=", 3//2)
# 注意：// 得到的并不一定是整数类型的数，它与分母分子的数据类型有关系。
print("10.0/3=", 10.0//3)
print("10/3.0=", 10//3.0)
print("10/3=", 10//3)


# 幂运算
print("5**2=", 5**2)
print("5**3=", 5**3)

print("pow(5,2)=", pow(5,2))
print("5^2=", 5^2)

"""
数学函数
函数	                返回值 ( 描述 )
abs(x)          返回数字的绝对值，如abs(-10) 返回 10
ceil(x)         返回数字的上入整数，如math.ceil(4.1) 返回 5
cmp(x, y)       如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。 Python 3 已废弃 。
exp(x)          返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
fabs(x)         返回数字的绝对值，如math.fabs(-10) 返回10.0
floor(x)        返回数字的下舍整数，如math.floor(4.9)返回 4
log(x)          如math.log(math.e)返回1.0,math.log(100,10)返回2.0
log10(x)        返回以10为基数的x的对数，如math.log10(100)返回 2.0
max(x1, x2,...) 返回给定参数的最大值，参数可以为序列。
min(x1, x2,...) 返回给定参数的最小值，参数可以为序列。
modf(x)         返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
pow(x, y)       x**y 运算后的值。
round(x [,n])   返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
sqrt(x)         返回数字x的平方根。
"""


"""
随机数函数
随机数可以用于数学，游戏，安全等领域中，还经常被嵌入到算法中，用以提高算法效率，并提高程序的安全性。
Python包含以下常用随机数函数：
函数                                  描述
choice(seq)             从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
randrange ([start,] stop [,step])   从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
random()                随机生成下一个实数，它在[0,1)范围内。
seed([x])               改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
shuffle(lst)            将序列的所有元素随机排序
uniform(x, y)           随机生成下一个实数，它在[x,y]范围内。
"""


"""
三角函数
Python包括以下三角函数：

函数	描述
acos(x)             返回x的反余弦弧度值。
asin(x)             返回x的反正弦弧度值。
atan(x)             返回x的反正切弧度值。
atan2(y, x)         返回给定的 X 及 Y 坐标值的反正切值。
cos(x)              返回x的弧度的余弦值。
hypot(x, y)         返回欧几里德范数 sqrt(x*x + y*y)。
sin(x)              返回的x弧度的正弦值。
tan(x)              返回x弧度的正切值。
degrees(x)          将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
radians(x)          将角度转换为弧度
"""








