# /usr/bin/env python
# coding=utf-8
"""
__Author__ = 'JohnToms'
__CreateTime__ = '2019/1/30'
Title : 进制之间的转换
"""


"""
进制的写法不区分大小写
bin() 其他进制 转换为 二进制(ob)
hex() 其他进制 转换为 十六进制(0x)
int() 其他进制 转换为 十进制
oct() 其他进制 转换为 8进制(0o)
"""

print(bin(10))
print(bin(0xdcfe))
print(bin(0o721672))
print(bin(0b110101))

print(hex(15))
print(hex(0xadc21))
print(hex(0o2112))
print(hex(0B1010101))

print(oct(1019202))
print(oct(0X2121afd))
print(oct(0b10100101))
print(oct(0o112545))

print(int(1))
print(int(0x819afdf))
print(int(0O1267534))
print(int(0b100101))