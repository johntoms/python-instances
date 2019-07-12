# centos 安装 redis

## 下载安装包

```
wget http://download.redis.io/releases/redis-5.0.5.tar.gz
```

## 安装依赖包

```
yum install tcl
```

## 编译
```
$ make
####################################### 
#  报错
#######################################

[root@VM_0_2_centos redis-5.0.5]# make
cd src && make all
make[1]: Entering directory `/root/redis-5.0.5/src'
    CC adlist.o
In file included from adlist.c:34:0:
zmalloc.h:50:31: fatal error: jemalloc/jemalloc.h: No such file or directory
 #include <jemalloc/jemalloc.h>
                               ^
compilation terminated.
make[1]: *** [adlist.o] Error 1
make[1]: Leaving directory `/root/redis-5.0.5/src'
make: *** [all] Error 2


# 加入参数
$ make MALLOC=libc
ok

```

