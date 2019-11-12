# 编译安装 `python3`时注意事项
## 如果 ssl 无法被调用，并且报错信息如下：
```shell
[root@localhost Python-3.6.3]# python3
Python 3.7.3 (default, Nov 19 2018, 14:18:18)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-28)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import ssl
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/python3/lib/python3.7/ssl.py", line 101, in <module>
    import _ssl             # if we can't import it, let the error propagate
ModuleNotFoundError: No module named '_ssl'
```
即：`ModuleNotFoundError: No module named '_ssl'`，ssl 模块安装有问题，需修改 ssl的编译配置文件，重新编译 `python` 环境。

## 修改 `Setup`和`Setup.dist`

### Setup
> 需要修改的文档位置大概在 207 行左右

```bash
vim python3.7.3/Modules/Setup +207
```

原文件
```shell
200 # Memory-mapped files (also works on Win32).
201 #mmap mmapmodule.c
202 
203 # CSV file helper
204 #_csv _csv.c
205 
206 # Socket module helper for socket(2)
207 #_socket socketmodule.c
208 
209 # Socket module helper for SSL support; you must comment out the other
210 # socket line above, and possibly edit the SSL variable:
211 #SSL=/usr/local/ssl
212 #_ssl _ssl.c \
213 #        -DUSE_SSL -I$(SSL)/include -I$(SSL)/include/openssl \
214 #        -L$(SSL)/lib -lssl -lcrypto
215 
216 # The crypt module is now disabled by default because it breaks builds
217 # on many systems (where -lcrypt is needed), e.g. Linux (I believe).
218 
219 #_crypt _cryptmodule.c # -lcrypt        # crypt(3); needs -lcrypt on some systems
220 
```
修改后的文件
```shell
200 # Memory-mapped files (also works on Win32).
201 #mmap mmapmodule.c
202 
203 # CSV file helper
204 #_csv _csv.c
205 
206 # Socket module helper for socket(2)
207 _socket socketmodule.c
208 
209 # Socket module helper for SSL support; you must comment out the other
210 # socket line above, and possibly edit the SSL variable:
211 SSL=/usr/local/ssl
212 _ssl _ssl.c \
213         -DUSE_SSL -I$(SSL)/include -I$(SSL)/include/openssl \
214         -L$(SSL)/lib -lssl -lcrypto
215 
216 # The crypt module is now disabled by default because it breaks builds
217 # on many systems (where -lcrypt is needed), e.g. Linux (I believe).
218 
219 #_crypt _cryptmodule.c # -lcrypt        # crypt(3); needs -lcrypt on some systems
220 
```

### Setup.dist
> 需要修改的文档位置大概在 207 行左右
```bash
vim python3.7.3/Modules/Setup.dist +207
```
修改前
```shell
200 # Memory-mapped files (also works on Win32).
201 #mmap mmapmodule.c
202 
203 # CSV file helper
204 #_csv _csv.c
205 
206 # Socket module helper for socket(2)
207 #_socket socketmodule.c
208 
209 # Socket module helper for SSL support; you must comment out the other
210 # socket line above, and possibly edit the SSL variable:
211 SSL=/usr/local/ssl
212 #_ssl _ssl.c \
213 #        -DUSE_SSL -I$(SSL)/include -I$(SSL)/include/openssl \
214 #       -L$(SSL)/lib -lssl -lcrypto
215 
216 # The crypt module is now disabled by default because it breaks builds
217 # on many systems (where -lcrypt is needed), e.g. Linux (I believe).
218 
219 #_crypt _cryptmodule.c # -lcrypt        # crypt(3); needs -lcrypt on some systems
220 
```
修改后
```shell
200 # Memory-mapped files (also works on Win32).
201 #mmap mmapmodule.c
202 
203 # CSV file helper
204 #_csv _csv.c
205 
206 # Socket module helper for socket(2)
207 _socket socketmodule.c
208 
209 # Socket module helper for SSL support; you must comment out the other
210 # socket line above, and possibly edit the SSL variable:
211 SSL=/usr/local/ssl
212 _ssl _ssl.c \
213         -DUSE_SSL -I$(SSL)/include -I$(SSL)/include/openssl \
214         -L$(SSL)/lib -lssl -lcrypto
215 
216 # The crypt module is now disabled by default because it breaks builds
217 # on many systems (where -lcrypt is needed), e.g. Linux (I believe).
218 
219 #_crypt _cryptmodule.c # -lcrypt        # crypt(3); needs -lcrypt on some systems
220 
```

重新编译
```bash
# 需在 `python` 的包内
# /../../Python-3.7.3/
./configure --prefix=/usr/local/cloudcare/python3
make && make install
# 如果编译的文件位置不变，软连接可以不用更改
```



