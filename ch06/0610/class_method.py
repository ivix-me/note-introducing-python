# -*- coding: utf-8 -*-


class A:
    count = 0  # 类特性

    def __init__(self):
        A.count += 1

    def exclaim(self):
        print("I'm an A!")

    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.") # cls.count与A.count的作用一样


if __name__ == '__main__':
    a1 = A()
    a2 = A()
    a3 = A()
    A.kids()
