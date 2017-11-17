# -*- coding: utf-8 -*-


def my_range(start=0, end=10, step=1):
    number = start
    while number < end:
        yield number
        number += step


if __name__ == '__main__':
    print(list(my_range()))
