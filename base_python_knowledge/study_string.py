# /usr/bin/env python
# coding=utf-8
"""
__Author__ = 'johntoms'
__CreateTime__ = '2019/1/24'
"""

# 1. python 转义字符
# \ 在末尾时      续行符
# \'            单引号
# \"            双引号
# \a            响铃   在pycharm编译器内是无法响铃的，在系统内执行是可以响铃的
# \b            退格符
# \000          空
# \n            换行符
# \t            水平制表符（4个空格）
# \v            垂直制表符
# \r            回车
# \oyy          八进制数，yy代表的字符
# \xyy          十六进制数，yy代表的字符


def func1():
    print('单引号: ', '\'')
    print('双引号: ', '\"')
    print('响铃:', '\a')
    print('退格符: ', '\b')
    print(r'原始字符串\n, r/R，不转义')


# 2. python 字符串运算
# +              字符串的拼接
# *              重复输出字符串
# []             通过索引获取字符串
# [:]            截取字符串中的一部分，遵循   左闭右开  [) 原则，str[0,2] 是不包含第 3 个字符的。
# in / not in    成员运算符 - 判断 字符串/字符 是否在 某一字符串中


# 3. python 格式化输出字符串
# %c             格式化字符及其ASCII码
# %s             格式化字符串
# %d             格式化整数
# %u             格式化无符号整型
# %o             格式化无符号八进制数
# %x             格式化无符号十六进制数
# %X             格式化无符号十六进制数（大写）
# %f             格式化浮点数字，可指定小数点后的精度
# %e             用科学计数法格式化浮点数
# %E             作用同%e，用科学计数法格式化浮点数
# %p             用十六进制数格式化变量的地址


def func2():
    var = 'hello world'
    age = 10
    number = -100
    char_test = 'c'
    print('hello shanghai %s' % var)
    print('hello %c' % char_test)
    print('my age is %d' % age)
    print('number is %o' % number)
    print('number is %x' % number)
    print('e number is %e' % number)
    print('address is 0X%x' % id(number))


# 格式化输出的辅助命令
# *              定义宽度或者小数点精度
# -              用做左对齐
# +              在正数前面显示加号( + )
# <sp>(空格)      在正数前面显示空格
# #              在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
# 0              显示的数字前面填充'0'而不是默认的空格
# %              '%%'输出一个单一的'%'
# (var)          映射变量(字典参数)
# m.m.           m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)
# %[(name)][flags][width].[precision]typecode
#
# (name)为命名
#
# flags可以有+,-,' '或0。+表示在正数前面显示加号( + )。-表示左对齐。' '为一个空格，表示在正数的左侧填充一个空格，从而与负数对齐。0表示使用0填充。
#
# width表示显示宽度
#
# precision表示小数点后精度


def func3():
    var = 100
    var1 = -100000
    var2 = 0.0011212
    float_var = 2.3244324342342342
    name = {'name': 'kong', 'age': 10, 'sex': 'men'}
    print('* %+010.4f' % var2)
    print('* % d' % var)
    print('* %-d' % var1)
    print('* %+d' % float_var)
    print('my classmate name is %(name)s, age is %(age)d, sex is %(sex)s.' % name)
# python 字符串内置方法参考链接：http://www.runoob.com/python3/python3-string.html


if __name__ == '__main__':
    func3()

