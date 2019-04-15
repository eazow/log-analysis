# -*- coding:utf-8 -*-

import os
import logging
import datetime
import re
import time
import traceback

from db.models import NginxLog
from settings import LOGS_DIR_PATH, MYSQL_URI, ANDROID, IPHONE, IOS

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

NGINX_LOG_PATH = os.path.join(LOGS_DIR_PATH, "nginx.log")

# 提取手机品牌，可扩展
PHONE_BRAND_REGEX = r"MI|HUAWEI|OPPO|VIVO|ZTE|REDMI|LG|LE"

IPHONE_REGEX = r"iPhone[\w\s]+"

ANDROID_VERSION_REGEX = r"android \d+\.\d+(\.\d+)?"

IOS_VERSION_REGEX = r"iOS \d+\.\d+(\.\d+)?"



def analysis(log_path):

    nginx_logs = parse_log_file(log_path)
    save_nginx_logs(nginx_logs)


def save_nginx_logs(nginx_logs):
    engine = create_engine(MYSQL_URI)
    DBSession = sessionmaker(bind=engine)

    session = DBSession()
    session.add_all(nginx_logs)
    session.commit()

    session.close()


def parse_log_file(log_path):
    """
    解析日志文件
    :param log_path:
    :return:
    """
    nginx_logs = []

    with open(log_path, 'r') as f:
        lines_count = 0
        for line in f.xreadlines():
            try:
                dst_ip, empty, request_time, request_line, host, http_status, size, referrer, user_agent, src_ip, \
                    backend_address, backend_status, backend_time, response_time = map(str.strip, line.split("|"))

                request_method, request_url, http_version = request_line.split(" ")

                request_url_origin = request_url
                # 如果url有请求参数，需去除请求参数
                if request_url.find("?") > 0:
                    request_url = request_url[0:request_url.find("?")]

                # 解析手机信息，返回手机类型、品牌、型号、os类型、os版本
                phone_type, phone_brand, phone_model, phone_os_type, phone_os_version = parse_phone_info(user_agent)

                # 处理request_time, 格式16/Mar/2018:20:29:59 +0800
                request_time = datetime.datetime.strptime(request_time, "%d/%b/%Y:%H:%M:%S +0800")

                nginx_log = NginxLog(dst_ip=dst_ip, request_time=request_time, request_line=request_line,
                                     request_method=request_method, request_url=request_url,
                                     http_version=http_version, host=host, http_status=http_status, size=size,
                                     referrer=referrer, user_agent=user_agent, phone_type=phone_type,
                                     src_ip=src_ip, backend_address=backend_address, backend_status=backend_status,
                                     backend_time=backend_time, response_time=response_time,
                                     phone_os_version=phone_os_version, phone_model=phone_model,
                                     request_url_origin=request_url_origin, phone_brand=phone_brand,
                                     phone_os_type=phone_os_type)

                nginx_logs.append(nginx_log)

            except Exception, e:
                traceback.print_exc()
                logging.warning(e)
                logging.warning("line num: %s; log is invalid: %s" % (lines_count, line))

            lines_count += 1

    return nginx_logs


def parse_phone_info(user_agent):
    # 提取android, iphone以及其他终端
    # (android 6.0.1, OPPO A57)
    # (Linux; Android 5.0.2; Redmi Note3 Build/LRX22G;wv)
    phone_type = "other"
    phone_brand = "other"
    phone_os_type = "other"
    phone_model = ""
    phone_os_version = ""
    user_agent_lower = user_agent.lower()
    if user_agent_lower.find(ANDROID) >= 0:
        phone_type = ANDROID
        phone_os_type = ANDROID
        phone_info_start_index = user_agent.find("(android")
        if phone_info_start_index > 0:
            phone_info_end_index = user_agent.find(")", phone_info_start_index)
            phone_info = user_agent[phone_info_start_index + 1: phone_info_end_index]
            phone_os_version, phone_model = map(str.strip, phone_info.split(","))
            # phone_model可以提取phone_brand
            phone_brand_match_obj = re.search(PHONE_BRAND_REGEX, phone_model.upper())
            if phone_brand_match_obj:
                phone_brand = phone_brand_match_obj.group(0)
        # (Linux; Android 5.0.2; Redmi Note3 Build/LRX22G;wv)
        else:
            phone_os_match_obj = re.search(ANDROID_VERSION_REGEX, user_agent_lower)
            if phone_os_match_obj:
                phone_os_version = phone_os_match_obj.group(0)
            else:
                logging.warning("can't find android version, user_agent: %s" % user_agent)

            phone_brand_match_obj = re.search(PHONE_BRAND_REGEX, user_agent)
            if phone_brand_match_obj:
                phone_brand = phone_brand_match_obj.group(0)

            # todo 提取手机型号
            phone_model = ""

    # (iPhone 6; iOS 8.1.1; Scale / 2.00)
    # (iPhone; CPU iPhone OS 11_2_5 like Mac OS X)
    # iPhone8,2归为iphone8
    elif user_agent_lower.find(IPHONE) >= 0:
        phone_type = IPHONE
        phone_os_type = IOS
        phone_os_version = ""
        # iphone型号
        phone_model_match_obj = re.search(IPHONE_REGEX, user_agent)
        if phone_model_match_obj:
            phone_model = phone_model_match_obj.group(0)
        # ios版本
        phone_os_match_obj = re.search(IOS_VERSION_REGEX, user_agent)
        if phone_os_match_obj:
            phone_os_version = phone_os_match_obj.group(0)
        # 其他ios版本信息格式：(iPhone; CPU iPhone OS 11_2_5 like Mac OS X)
        else:
            phone_os_version = "ios other"
        phone_brand = "APPLE"

    return phone_type, phone_brand, phone_model, phone_os_type, phone_os_version


if __name__ == "__main__":
    try:
        logging.basicConfig(filename="log_analysis.log", level=logging.DEBUG, datefmt="%Y-%m-%d %H:%M:%S",
                            format="%(asctime)s-%(levelname)s-%(lineno)d-%(message)s")
        start_time = time.time() * 1000
        analysis(NGINX_LOG_PATH)
        end_time = time.time() * 1000
        logging.debug("spend time: %s ms " % (end_time - start_time))
    except Exception, e:
        traceback.print_exc()
        logging.exception(e)