# /usr/bin/env python
"""
__Author__ = 'johntoms'
__CreateTime__ = '2019/1/25'
"""

"""
1. 在python2默认编码是ASCII, python3里默认是unicode.
2. unicode 分为 utf-32(占4个字节),utf-16(占两个字节)，utf-8(占1-4个字节)
   so utf-16就是现在最常用的unicode版本， 不过在文件里存的还是utf-8，因为utf8省空间
3. 在py3中encode,在转码的同时还会把string 变成bytes类型，decode在解码的同时还会把bytes变回string
"""


"""
我们的代码中存在中文字符,一般需要在文件首行或者第二行加入`# coding=utf-8`
在 python3中你不需要加入 `coding=utf-8`
"""
print("hello world")


"""
python2
如果你的变量中存在中文,一般你还会加入
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
在 python3 中已经移除 reload()函数和 sys.setdefultencoding()
在 python3中你无须太担心关于中文的问题.
"""


"""
改变文件的字符集编码格式:
默认情况下，Python 3 源码文件以 UTF-8 编码，所有字符串都是 unicode 字符串。 当然你也可以为源码文件指定不同的编码：
`# -coding=cp-1252 `
"""
