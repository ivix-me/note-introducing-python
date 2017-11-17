# -*- coding: utf-8 -*-


class Person:
    def __init__(self, name):
        self.name = name


class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email


if __name__ == '__main__':
    baoyu = EmailPerson('宝玉', 'baoyu@ivix.me')

    print('「姓名」', baoyu.name, '「邮箱」', baoyu.email)
