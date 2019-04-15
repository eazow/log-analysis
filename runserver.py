# -*- coding:utf-8 -*-

import traceback
import os

from db.models import NginxLog
from flask import Flask, jsonify, request, url_for
from error import CustomError
from main import NginxLogMain
from settings import SUCCESS, ERROR, ROOT_PATH

from database import db_session, init_db
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import logging


app = Flask(__name__)


@app.route("/get_top10_urls", methods=["GET"])
def get_top10_urls():
    try:
        top10_urls = NginxLogMain(db_session).get_topn_urls(10)
    except Exception, e:
        traceback.print_exc()
        return jsonify({"code": 200, "status": ERROR, "data": [], "message": "error"})
    return jsonify({"code": 200, "status": SUCCESS, "data": top10_urls, "message": "success"})


@app.route("/get_top10_src_ips", methods=["GET"])
def get_top10_src_ips():
    try:
        top10_src_ips = NginxLogMain(db_session).get_topn_src_ips(10)
    except Exception, e:
        traceback.print_exc()
        return jsonify({"code": 200, "status": ERROR, "data": [], "message": "error"})
    return jsonify({"code": 200, "status": SUCCESS, "data": top10_src_ips, "message": "success"})


@app.route("/get_android_ios_count", methods=["GET"])
def get_android_ios_count():
    try:
        android_ios_count = NginxLogMain(db_session).get_android_ios_count()
    except Exception, e:
        traceback.print_exc()
        return jsonify({"code": 200, "status": ERROR, "data": [], "message": "error"})
    return jsonify({"code": 200, "status": SUCCESS, "data": android_ios_count, "message": "success"})


@app.route("/get_android_ios_versions_count", methods=["GET"])
def get_android_ios_versions_count():
    """
    获取android ios各个版本占比
    :return:
    """
    try:
        android_ios_versions_count = NginxLogMain(db_session).get_android_ios_versions_count()
    except Exception, e:
        traceback.print_exc()
        return jsonify({"code": 200, "status": ERROR, "data": [], "message": "error"})
    return jsonify({"code": 200, "status": SUCCESS, "data": android_ios_versions_count, "message": "success"})


@app.route("/", methods=["GET"])
def index():
    return app.send_static_file('index.html')



if __name__ == '__main__':
    init_db()
    logging.basicConfig(filename=os.path.join(ROOT_PATH, "runserver.log"), level=logging.DEBUG,
                        datefmt="%Y-%m-%d %H:%M:%S",
                        format="%(asctime)s-%(levelname)s-%(message)s")
    app.run(host="0.0.0.0")
