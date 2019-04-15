# -*- coding:utf-8 -*-

from error import CustomError
import os

from service import NginxLogService
from settings import IPHONE, IOS, ANDROID


class NginxLogMain(object):
    def __init__(self, db_session):
        self.nginx_log_service = NginxLogService(db_session)

    def get_topn_urls(self, n):
        return self.nginx_log_service.get_topn_urls(n)

    def get_topn_src_ips(self, n):
        """
        获取访问次数top n的源ip
        :param n:
        :return:
        """
        return self.nginx_log_service.get_topn_src_ips(n)

    def get_android_ios_count(self):
        """
        获取andrid ios以及各个版本的数量
        :return:
        """
        return self.nginx_log_service.get_android_ios_count()

    def get_android_ios_versions_count(self):
        """
        获取android ios各个版本占比
        :return:
        """
        return self.nginx_log_service.get_os_versions_count(ANDROID) + self.nginx_log_service.get_os_versions_count(IOS)

    def get_phone_brands_count(self):
        """
        获取手机各个品牌数量
        :return
        """
        return self.nginx_log_service.get_phone_brands_count()
