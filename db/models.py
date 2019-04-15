# -*- coding:utf-8 -*-
import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, VARCHAR

from database import Base


class NginxLog(Base):

    __tablename__ = 't_nginx_log'

    id = Column(Integer, primary_key=True, autoincrement=True)
    dst_ip = Column(String(50)) # 10.255.252.4
    request_time = Column(DateTime()) # 16/Mar/2018:20:29:57 +0800
    request_line = Column(VARCHAR(2048)) # GET /zh-CN/baby_credits?baby_id=761756&v=2&page=0 HTTP/1.1
    request_method = Column(String(32))
    request_url = Column(VARCHAR(1024))
    request_url_origin = Column(VARCHAR(1024))
    http_version = Column(String(128))
    host = Column(String(128)) # api.shiguangxiaowu.cn
    http_status = Column(String(128)) # 200
    size = Column(String(128)) # 1238
    referrer = Column(VARCHAR(1024)) #'https://www.baidu.com/link?url=-YzFM4p2GLR8g_&wd=&eqid=e5c101dd0007cbed0000000
    user_agent = Column(VARCHAR(2048)) # com.liveyap.timehut/5.2.2.1 (android 6.0.1, OPPO A57) (SOURCE/oppostore, VERSION_CODE/255)
    phone_type = Column(String(16))
    phone_os_version = Column(String(32))
    phone_model = Column(String(128))
    src_ip = Column(String(128)) # 58.53.78.68
    backend_address = Column(String(128)) # unix:///tmp/saturn.sock
    backend_status = Column(String(128)) # 200
    backend_time = Column(String(128)) # 0.077
    response_time = Column(String(128)) # 0.077
    phone_brand = Column(String(32))
    create_time = Column(DateTime())
    phone_os_type = Column(String(16))

    def __init__(self, dst_ip, request_time, request_line, request_method, request_url, http_version, host,
                 http_status, size, referrer, user_agent, phone_type, src_ip, backend_address, backend_status,
                 backend_time, response_time, phone_os_version, phone_model, request_url_origin, phone_brand,
                 phone_os_type):
        self.dst_ip = dst_ip
        self.request_time = request_time
        self.request_line = request_line
        self.request_method = request_method
        self.request_url = request_url
        self.http_version = http_version
        self.host = host
        self.http_status = http_status
        self.size = size
        self.referrer = referrer
        self.user_agent = user_agent
        self.phone_type = phone_type
        self.src_ip = src_ip
        self.backend_address = backend_address
        self.backend_status = backend_status
        self.backend_time = backend_time
        self.response_time = response_time
        self.phone_os_version = phone_os_version
        self.phone_model = phone_model
        self.request_url_origin = request_url_origin
        self.phone_brand = phone_brand
        self.phone_os_type = phone_os_type
        self.create_time = datetime.datetime.now()

