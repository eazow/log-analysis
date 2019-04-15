# nginx 日志分析

#### 1. 准备
需要安装python, flask, sqlalchemy, pymysql, mysql

#### 2. 配置数据库
- 执行sqls文件夹中的init_db.sql
- 修改setings.py中MYSQL_URI的用户名密码

#### 3. 启动日志分析平台
```
python runserver.py
```
此时会监听127.0.0.1:5000, 并创建所需的数据库表t_nginx_log

#### 4. 运行日志分析程序
```
python log_analysis.py
```

#### 5. 访问日志分析平台
http://127.0.0.1:5000

#### 6. UI
![image.png](https://upload-images.jianshu.io/upload_images/1425939-62418cb40a5e4576.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### 7. 说明
- main.py: 数据库操作业务层，调用service提供的接口
- service.py: 数据库操作服务层
- runserver.py: 日志展示平台启动脚本
- log_analysis.py: 日志处理脚本，将nginx日志处理后存入数据库

#### 8. Todo
- 通过ip geo关系，获取源ip的地理位置，可展示源ip的城市分布情况
- 若处理的是nginx的实时日志，可按天、或小时分割nginx日志至logs目录，并将log_analysis改为守护进程运行，实时处理日志文件
- 分析请求响应时间最慢的Top 10 url, 并优化接口