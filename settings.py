# -*- coding:utf-8 -*-
import os

SUCCESS = 1
ERROR = 0

MYSQL_URI = 'mysql+pymysql://root:admin123@10.91.3.37:3306/log_analysis'

ROOT_PATH = os.path.dirname(__file__)

# 项目根路径
PROJECT_ROOT_PATH = os.path.join(ROOT_PATH, "bda")

TASK_JSON_PATH = os.path.join(ROOT_PATH, "task.json")

CONFIGS_DIR_PATH = os.path.join(ROOT_PATH, "configs")

BACKUP_DIR_PATH = os.path.join(ROOT_PATH, "backup")

SCRIPTS_DIR_PATH = os.path.join(ROOT_PATH, "scripts")

LOGS_DIR_PATH = os.path.join(ROOT_PATH, "logs")

IPHONE = "iphone"
ANDROID = "android"
IOS = "ios"
