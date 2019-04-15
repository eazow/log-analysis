# nginx 日志处理

### 1. 准备
需要安装python, flask, sqlalchemy, pymysql, mysql

### 2. 创建数据库
* 执行sqls文件夹中的init_db.sql

### 3. 启动日志分析平台
```
python runserver.py
```
此时会监听127.0.0.1:5000

### 4. 运行日志分析程序
```
python log_analysis.py
```

### 5. 访问日志分析平台
http://127.0.0.1:5000

### 6. 展示图
![image.png](https://upload-images.jianshu.io/upload_images/1425939-ced724648f22c8eb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![image.png](https://upload-images.jianshu.io/upload_images/1425939-b3fd5058a1289e01.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![image.png](https://upload-images.jianshu.io/upload_images/1425939-95afc919f428ea4f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![image.png](https://upload-images.jianshu.io/upload_images/1425939-8b1f882457e03801.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)