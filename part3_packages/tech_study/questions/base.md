# 基础知识题

1. 考点：
 - 列表的使用
 - 迭代
 - 包的导入
 - python3 和 python2 的简单区别

题目1
```markdown
# ==================================
# 1. is 和 == 的区别？
# ==================================

# result
is判断的是ID的地址
==判断的是数值

```
题目2
```markdown
# ===========================
# 2. 输出 10-100 的所有正整数并且每次打印暂停 1 秒。
# ===========================

# result

import time

for i in range(10, 100):
    print(i)
    time.sleep(1)

```

题目3
```markdown
# =====================================
# 3. 使用 lambda 写一个求 x的6方的函数，求 234 的结果并保存到当前目录的 results.txt 文件下。
# =====================================

# result
func = lambda x: pow(x, 6)
result = func(234)
with open("./result.txt", "a") as f:
    f.write(result)

```

题目4
```markdown
# ======================================
# 4. 简述函数传递变量时 *args 和 **kwargs 的作用，写出一个循环打印所有变量的示例。
# ======================================

# result
1. 单个星号，如：*args是用来接受任意多个参数并将其放在一个数组中，它的本质是一个tuple。
2. 如：**kwargs 用于接收类似于关键参数一样赋值的形式的多个实参放入字典中（即把该函数的参数转换为字典），它的本质是一个dict。
3. 将不定数量的参数传递给一个函数


def func(*args, **kwargs):
    for i in args():
        print(i)
    for key, value in kwargs.items():
        # print(key, value)
        # 下方最好
        print("key: {key}, value: {value}".format(key=key, value=value))
```


题目2
```markdown

# =========================
# 在运维中你用过哪些 python 库或方法并简明该库或方法的作用？
# =========================

# result
基础库：sys、os（os.path、os.stat）、time、logging、prarmiko、re、random

csv：对于读取 csv 文件来说非常便利
collections：常见数据类型的实用扩展，包括 OrderedDict、defaultdict 和 namedtuple
random：生成假随机数字，随机打乱序列并选择随机项
string：关于字符串的更多函数。此模块还包括实用的字母集合，例如 string.digits（包含所有字符都是有效数字的字符串）
re：通过正则表达式在字符串中进行模式匹配
math：一些标准数学函数
os：与操作系统交互
os.path：os 的子模块，用于操纵路径名称
sys：直接使用 Python 解释器
json：适用于读写 json 文件（面向网络开发）


Python运维常用的20个库

1、psutil是一个跨平台库（https://github.com/giampaolo/psutil）
能够实现获取系统运行的进程和系统利用率（内存，CPU,磁盘，网络等），主要用于系统监控，分析和系统资源及进程的管理。

2、IPy（http://github.com/haypo/python-ipy）,辅助IP规划。

3、dnspython(http://dnspython.org)Python实现的一个DNS工具包。

4、difflib：difflib作为Python的标准模块，无需安装，作用是对比文本之间的差异。

5、filecmp:系统自带，可以实现文件，目录，遍历子目录的差异，对比功能。

6、smtplib：发送电子邮件模块

7、pycurl(http://pycurl.sourceforge.net)是一个用C语言写的libcurl Python实现，功能强大，支持的协议有：FTP,HTTP,HTTPS,TELNET等，可以理解为Linux下curl命令功能的Python封装。（PS：PycURL在前几天的文章里有提及过）

8、XlsxWriter:操作Excel工作表的文字，数字，公式，图表等。

9、rrdtool:用于跟踪对象的变化，生成这些变化的走走势图

10、scapy(http://www.wecdev.org/projects/scapy/)是一个强大的交互式数据包处理程序，它能够对数据包进行伪造或解包，包括发送数据包，包嗅探，应答和反馈等功能。

11、Clam Antivirus免费开放源代码防毒软件，pyClamad,可以让Python模块直接使用ClamAV病毒扫描守护进程calmd。

12、pexpect:可以理解成Linux下expect的Python封装，通过pexpect我们可以实现对ssh,ftp,passwd,telnet等命令行进行自动交互，而无需人工干涉来达到自动化的目的。

13、paramiko是基于Python实现的SSH2远程安装连接，支持认证及密钥方式。可以实现远程命令执行，文件传输，中间SSH代理等功能。相对于Pexpect,封装的层次更高，更贴近SSH协议的功能，官网地址：http://paramiko.org(依赖：Crypto,Ecdsa,Python开发包python-devel)

14、fabric是基于Python实现的SSH命令行工具，简化了SSH的应用程序部署及系统管理任务，它提供了系统基础的操作组件，可以实现本地或远程shell命令，包括命令执行，文件上传，下载及完整执行日志输出等功能。Fabric在paramiko的基础上做了更高一层的封装，操作起来更加简单。官网地址：http://www.fabfile.org(依赖setuptools,Crypto,paramiko包支持)

15、CGIHTTPRequestHandler实现对CGI的支持。

16、ansible(http://www.ansibleworks.com/)一种集成IT系统的配置管理，应用部署，执行特定任务的开源平台。基于Python实现，由Paramiko和PyYAML两个关键模块构建。Ansibl与Saltstack最大的区别是Ansible无需在被控主机上部署任何客户端，默认直接通过SSH通道进行远程命令执行或下发功能。

17、YAML:是一种用来表达数据序列的编程语言。

18、playbook：一个非常简单的配置管理和多主机部署系统。

19、saltstack(http://saltstack.com)是一个服务器基础架构集中化管理平台，一般可以理解为简化版的puppet和加强版的func。Saltstack基于Python语言实现，结合轻量级消息队列ZeroMQ,与Python每三方模块（Pyzmq,PyCrypto,Pyjinja2,python-msgpack和PyYAML等）构建。

20、func，为解决集群管理，监控问题需设计开发的系统管理基础框架。


原文地址: https://www.cnblogs.com/LouisZJ/p/10781675.html
```

