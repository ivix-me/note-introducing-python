# -*- coding: utf-8 -*-


import threading

def do_this(what):
    whoami(what)

def whoami(what):
    print('#%s 线程说：%s' % (threading.current_thread(), what))

if __name__ == '__main__':
    whoami('我是主程序')
    for n in range(4):
        p = threading.Thread(target=do_this, args=('我是 #%s 线程' % n,))
        p.start()
