## Dockerfile 指令详解
1. COPY 复制文件
```
格式：
COPY [--chown=<user>:<group>] <源路径>... <目标路径>
COPY [--chown=<user>:<group>] ["<源路径1>",... "<目标路径>"]
和 RUN 指令一样，也有两种格式，一种类似于命令行，一种类似于函数调用。

COPY 指令将从构建上下文目录中 <源路径> 的文件/目录复制到新的一层的镜像内的 <目标路径> 位置。比如：
COPY package.json /usr/src/app/
<目标路径> 可以是容器内的绝对路径，也可以是相对于工作目录的相对路径（工作目录可以用 WORKDIR 指令来指定）。
目标路径不需要事先创建，如果目录不存在会在复制文件前先行创建缺失目录。
```

2. ADD 更高级的复制文件

3. CMD 容器启动命令
```
CMD 指令的格式和 RUN 相似，也是两种格式：

shell 格式：CMD <命令>
exec 格式：CMD ["可执行文件", "参数1", "参数2"...]
参数列表格式：CMD ["参数1", "参数2"...]。在指定了 ENTRYPOINT 指令后，用 CMD 指定具体的参数。
```

4. ENTRYPOINT 入口点

5. ENV 设置环境变量
```
格式有两种：
ENV <key> <value>
ENV <key1>=<value1> <key2>=<value2>...

ENV VERSION=1.0 DEBUG=on \
    NAME="Happy Feet"
```

6. ARG 构建参数
`格式：ARG <参数名>[=<默认值>]`

7. VOLUME 定义匿名卷
```
格式为：
VOLUME ["<路径1>", "<路径2>"...]
VOLUME <路径>

之前我们说过，容器运行时应该尽量保持容器存储层不发生写操作，
对于数据库类需要保存动态数据的应用，其数据库文件应该保存于卷(volume)中，后面的章节我们会进一步介绍 Docker 卷的概念。
为了防止运行时用户忘记将动态文件所保存目录挂载为卷，在 Dockerfile 中，我们可以事先指定某些目录挂载为匿名卷，
这样在运行时如果用户不指定挂载，其应用也可以正常运行，不会向容器存储层写入大量数据。

VOLUME /data
这里的 /data 目录就会在运行时自动挂载为匿名卷，任何向 /data 中写入的信息都不会记录进容器存储层，从而保证了容器存储层的无状态化。
当然，运行时可以覆盖这个挂载设置。比如：
docker run -d -v mydata:/data xxxx
在这行命令中，就使用了 mydata 这个命名卷挂载到了 /data 这个位置，替代了 Dockerfile 中定义的匿名卷的挂载配置。
```

8. EXPOSE 声明端口

9. WORKDIR 指定工作目录

10. USER 指定当前用户



