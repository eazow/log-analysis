# -*- coding:utf-8 -*-
import json
import logging
# from db.models import ConfigFile
import os
import time

from db.models import NginxLog
from sqlalchemy import func, desc


class NginxLogService(object):
    def __init__(self, db_session):
        self.db_session = db_session

    def get_topn_urls(self, n):
        """
        获取访问量top n的url
        :param n:
        :return:
        """
        url_count_map = self.db_session.query(NginxLog.request_url, func.count(NginxLog.request_url).label("count"))\
            .group_by(NginxLog.request_url).order_by(desc("count")).limit(n).all()
        topn_urls = []
        for url, count in url_count_map:
            # topn_urls.append({
            #     "url": url,
            #     "count": count
            # })
            topn_urls.append([url, count])
        return topn_urls

    def get_topn_src_ips(self, n):
        """
        获取访问次数top n的源ip
        :param n:
        :return:
        """
        src_ip_count_map = self.db_session.query(NginxLog.src_ip, func.count(NginxLog.src_ip).label("count")) \
            .group_by(NginxLog.src_ip).order_by(desc("count")).limit(n).all()
        topn_src_ips = []
        for src_ip, count in src_ip_count_map:
            # topn_src_ips.append({
            #     "src_ip": src_ip,
            #     "count": count
            # })
            topn_src_ips.append([src_ip, count])
        return topn_src_ips

    def get_android_ios_count(self):
        """
        获取andrid ios以及各个版本的数量
        :return:
        """
        phone_os_types_count = self.db_session \
            .query(NginxLog.phone_os_type, func.count(NginxLog.phone_os_type).label("count")) \
            .filter(NginxLog.phone_os_type != 'other').group_by(NginxLog.phone_os_type).all()
        phone_os_types_count_return = []
        for phone_type, count in phone_os_types_count:
            phone_os_types_count_return.append({
                "name": phone_type,
                "y": count
            })

        return phone_os_types_count_return

    def get_os_versions_count(self, os_type):
        """
        获取操作系统版本统计
        :param os_type: android | iphone
        :return:
        """
        phone_os_versions_count = self.db_session \
            .query(NginxLog.phone_os_version, func.count(NginxLog.phone_os_version).label("count")) \
            .filter(NginxLog.phone_os_type == os_type).group_by(NginxLog.phone_os_version).all()
        phone_os_versions_count_return = []
        for os_version, count in phone_os_versions_count:
            phone_os_versions_count_return.append({
                "name": os_version,
                "y": count
            })

        return phone_os_versions_count_return

    def get_phone_brands_count(self):
        """
        获取手机各个品牌数量
        :return
        """
        phone_brands_count = self.db_session \
            .query(NginxLog.phone_brand, func.count(NginxLog.phone_brand).label("count")) \
            .group_by(NginxLog.phone_brand).all()
        phone_brands_count_return = []
        for phone_brand, count in phone_brands_count:
            phone_brands_count_return.append({
                "name": phone_brand,
                "y": count
            })

        return phone_brands_count_return
