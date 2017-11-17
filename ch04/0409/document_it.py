# -*- coding: utf-8 -*-


def document_it(func):
    def new_function(*args, **kwargs):
        print('正在运行的函数：', func.__name__)
        print('位置参数：', args)
        print('关键字参数：', kwargs)
        result = func(*args, **kwargs)
        print('结果：', result)
        return result

    return new_function


@document_it
def add_ints(a, b):
    return a + b


if __name__ == '__main__':
    # ----- 手动调用。未加@document_it之前
    # cooler_add_ints = document_it(add_ints)
    # print(cooler_add_ints(3, 5))

    print(add_ints(5, 3))
