# -*- coding: utf-8 -*-


import multiprocessing as mp


def 洗碗工(一堆碗, 输出):
    for 碗 in 一堆碗:
        print('正在洗', 碗, '的碗')
        输出.put(碗)


def 烘干员(输入):
    while True:
        碗 = 输入.get()
        print('正在烘干', 碗, '的碗')
        输入.task_done()


碗队列 = mp.JoinableQueue()
烘干进程 = mp.Process(target=烘干员, args=(碗队列,))
烘干进程.daemon = True
烘干进程.start()

一堆碗 = ['色拉', '面包', '主菜', '甜点']
洗碗工(一堆碗, 碗队列)
碗队列.join()
