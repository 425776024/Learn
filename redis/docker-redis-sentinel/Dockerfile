# 基于最新的镜像centos
FROM centos:latest
# 构建该镜像的作者
MAINTAINER yc
# 添加redis用户和用户组
RUN groupadd -r redis && useradd  -r -g redis redis
# 更新yum源 && 安装Linux的epel的yum源的命令 && 安装redis && 安装工具
RUN yum -y update &&  yum -y install epel-release && yum -y install redis && yum -y install net-tools

## 在容器中创建config目录，并改变config的用户和用户组
RUN mkdir -p /config && chown -R redis:redis /config
## 把redis-master.conf文件拷贝到当前容器的config目录中
COPY ./conf/redis-sentinel.conf /config
COPY ./conf/redis-master.conf /config
COPY ./conf/redis-slave.conf /config
# ADD与COPY一样都是具有拷贝的功能，具体两者的差异自己去查下第二节篇幅的内容吧
#ADD ./conf/redis-slave.conf /config
## 把外部的config挂载到容器里，达成文件的共享
#VOLUME /usr/docker/redis/config
#WORKDIR /config

# 定义端口
EXPOSE 6379