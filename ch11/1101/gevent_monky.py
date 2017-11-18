# -*- coding: utf-8 -*-
# 为所有标准库模块打补丁（C写成的库除外）

import gevent
from gevent import monkey;
import socket

monkey.patch_all()

hosts = ['ivix.me', 'github.com', 'golang.org', 'python.org']
jobs = [gevent.spawn(socket.gethostbyname, host) for host in hosts]
gevent.joinall(jobs, timeout=5)
for job in jobs:
    print(job.value)
