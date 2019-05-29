#!/usr/bin/env python
# coding=utf-8
"""
__Author__ = 'JohnToms'
__CreateTime__ = '2019/5/15'
"""

"""
类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
数据成员：类变量或者实例变量, 用于处理类及其实例对象的相关的数据。
方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
局部变量：定义在方法中的变量，只作用于当前实例的类。
实例变量：在类的声明中，属性是用变量来表示的。这种变量就称为实例变量，是在类声明的内部但是在类的其他成员方法之外声明的。
继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
实例化：创建一个类的实例，类的具体对象。
方法：类中定义的函数。
对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
特性：对象可以包含任意数量和类型的数据。

语法格式：
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
"""


# 创建类

# 1. 常用语配置信息的类
class Config:
    """类的帮助信息"""
    PORT = 1000
    HOST = "localhost"
    USER = "root"
    PASSWORD = "123"


aaa = Config
print(aaa.__dict__)
print(aaa.__doc__)
print(type(aaa))
print(aaa.PORT)

print("----------------- 分割线 ------------------")
bbb = Config()
print(bbb.__dict__)
print(bbb.__doc__)
print(type(bbb))
print(bbb.PORT)


"""
注意：
1、 类的实例化不一样有括号和无括号是不一样的。
2. 有括号则调用 init() 方法 类型为 <type 'instance'> ，无括号则不调用 init() 方法相当于类的设置别名，类型为<type 'classobj'>。


输出的信息如下：
{'__module__': '__main__', '__doc__': '类的帮助信息', 'PORT': 1000, 'HOST': 'localhost', 'USER': 'root', 'PASSWORD': '123', '__dict__': <attribute '__dict__' of 'Config' objects>, '__weakref__': <attribute '__weakref__' of 'Config' objects>}
类的帮助信息
<class 'type'>
1000
----------------- 分割线 ------------------
{}
类的帮助信息
<class '__main__.Config'>
1000
"""

print("-------------------- 分割线 -------------------")

a = 1


def hello(a):
    print("hello world")
    print(a)
    return True


ccc = hello(a)

print(ccc)


ddd = hello
print(ddd)

print(ddd(a))

"""
1. 带括号的（传参或者无参），直接执行函数体，返回结果。
2. 不带括号的，不执行函数体，相当于给该函数取了一个别名，是整个函数体的 copy 。
输出如下：
hello world
1
True
<function hello at 0x10c448378>
hello world
1
True
"""


print("-------------------- 分割线 ---------------------")

