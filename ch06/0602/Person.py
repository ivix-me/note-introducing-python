# -*- coding: utf-8 -*-


class Person:
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    hunter = Person('埃尔默·福特')
    print('牛X的猎人：', hunter.name)
