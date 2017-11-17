# -*- coding: utf-8 -*-


animal = 'dog'  # 全局变量


def change_local():
    animal = 'cat'  # 局部变量
    print('局部变量：', locals())


change_local()
print('全局变量：', globals())
