# -*- coding:utf-8 -*-
import os

SUCCESS = 1
ERROR = 0

MYSQL_URI = 'mysql+pymysql://root:admin123@10.91.3.37:3306/log_analysis'

ROOT_PATH = os.path.dirname(__file__)

CONFIGS_DIR_PATH = os.path.join(ROOT_PATH, "configs")

LOGS_DIR_PATH = os.path.join(ROOT_PATH, "logs")

IPHONE = "iphone"
ANDROID = "android"
IOS = "ios"
