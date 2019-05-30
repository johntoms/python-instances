#!/usr/bin/env bash

##############################################
# version: 1.0.0
# 0. python version 3.7.3
# 1. 仅支持 CentOs 系统
# 2. 安装根目录在 /usr/local/cloudcare/
#
##############################################


# 安装依赖包
yum -y install zlib-devel bzip2 bzip2-devel openssl openssl-static openssl-devel \
ncurses ncurses-devel sqlite sqlite-devel readline readline-devel tk tk-devel lzma gdbm \
gdbm-devel db4-devel libpcap-devel xz xz-devel libffi-devel gcc

#检测 cloudcare 是否存在
if [[ ! -f "usr/local/cloudcare/" ]];then
mkdir /usr/local/cloudcare/
echo "Created /usr/local/cloudcare/"
fi

# 下载安装包 python 3.7.3
if [[ ! -f "./Python-3.7.3.tgz" ]];then
curl -O https://cloud-software.oss-cn-hangzhou.aliyuncs.com/linux%20%E8%BD%AF%E4%BB%B6/Python-3.7.3.tgz
fi

# 解压文件
tar -xvf Python-3.7.3.tgz && cd Python-3.7.3/

# 编译 python 包
./configure --prefix=/usr/local/cloudcare/python3
make && make install && echo "### Python3 install success!"

# 创建软连接
if [[ -f "/usr/bin/python3" ]]; then
rm -rf /usr/bin/python3
fi
ln -s /usr/local/cloudcare/python3/bin/python3 /usr/bin/python3 && echo "### Add python3 link Done!"

if [[ -f "/usr/bin/pip3" ]];then
rm -rf /usr/bin/pip3
fi
ln -s /usr/local/cloudcare/python3/bin/pip3 /usr/bin/pip3 && echo "### Add pip3 link Done!"
