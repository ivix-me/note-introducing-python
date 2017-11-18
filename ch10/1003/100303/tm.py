# -*- coding: utf-8 -*-


import multiprocessing
import time
import os


def whoami(name):
    print('我是 %s，在 #%s 进程里' % (name, os.getpid()))


def loopy(name):
    whoami(name)
    start = 1
    stop = 1000000
    for num in range(start, stop):
        print('\t#%s of %s.' % (num, stop))
        time.sleep(1)


if __name__ == '__main__':
    whoami('主程序')
    p = multiprocessing.Process(target=loopy, args=('loopy',))
    p.start()
    time.sleep(5)
    p.terminate()
