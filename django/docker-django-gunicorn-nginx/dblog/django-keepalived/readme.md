keepalived + nginx 高可用负载均衡集群配置。

web 服务器：（CPU性能）
192.168.52.128
192.168.52.131

keepalived + nginx服务器：（网卡性能）
152.168.52.129
152.168.52.130

虚拟IP: 192.168.52.133

nfs 服务器 （磁盘容量）
192.168.52.132


# ----------------------------
mysql: （CPU、网卡、磁盘整体性能）

redis(memcached): 内存容量

目前redis、mysql安装在 192.168.52.128



