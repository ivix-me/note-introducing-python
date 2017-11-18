# -*- coding: utf-8 -*-


import multiprocessing
import os


def do_this(what):
    whoami(what)


def whoami(what):
    print("进程 %s 说： %s" % (os.getpid(), what))


if __name__ == '__main__':
    whoami('我是主程序')
    for n in range(4):
        p = multiprocessing.Process(target=do_this, args=("我是 #%s 进程" % n,))
        p.start()
