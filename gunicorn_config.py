# -*- coding: utf-8 -*-
# @Time    : 2021/1/26 8:56
# @Author  : ztwu4
# @Email   : ztwu4@iflytek.com
# @File    : gunicorn_config.py
# @Software: PyCharm

import os
import gevent.monkey
gevent.monkey.patch_all()
import multiprocessing
# backlog = 512    #监听队列
# debug = True  # debug开启
# threads = 2 # 指定每个进程开启的线程数
# daemon = True # 表示开启后台运行,默认False
loglevel = 'debug'
bind = "0.0.0.0:5001" # 绑定的ip和端口号
# /var/log/WEB_APP 目录必须存在
pidfile = "/var/log/WEB_APP/gunicorn.pid"
accesslog = "/var/log/WEB_APP/access.log"
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"' #设置gunicorn访问日志格式，错误日志无法设置
errorlog = "/var/log/WEB_APP/debug.log"
# 启动的进程数
#workers = multiprocessing.cpu_count() # 这里取的是CPU的数量
workers = 4   # 进程数，
worker_class = 'gevent'   # worker_class是指开启的每个工作进程的模式类型，默认为sync模式，这里使用gevent模式
x_forwarded_for_header = 'X-FORWARDED-FOR'