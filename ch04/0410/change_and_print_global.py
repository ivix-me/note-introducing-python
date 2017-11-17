# -*- coding: utf-8 -*-


animal = 'dog'


def change_and_print_global():
    global animal
    print('change_and_print_global()之前: ', animal)
    animal = 'cat'
    print('change_and_print_global()之后: ', animal)


change_and_print_global()
print('全局命名空间：', animal)
