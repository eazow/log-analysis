# nginx 日志处理

### 1. 准备
需要安装python, flask, sqlalchemy, pymysql, mysql

### 2. 配置数据库
* 执行sqls文件夹中的init_db.sql
* 修改setings.py中MYSQL_URI的用户名密码

### 3. 启动日志分析平台
```
python runserver.py
```
此时会监听127.0.0.1:5000, 并创建

### 4. 运行日志分析程序
```
python log_analysis.py
```

### 5. 访问日志分析平台
http://127.0.0.1:5000

### 6. UI
![image.png](https://upload-images.jianshu.io/upload_images/1425939-62418cb40a5e4576.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


### 7. 扩展
1. 可展示手机品牌分布
2. 通过ip geo关系，获取源ip的地理位置，可展示源ip的城市分布情况
2. 若ngxin.log持续写入，可按天、或小时分割nginx日志