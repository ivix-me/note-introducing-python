# -*- coding: utf-8 -*-


class Duck:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


donald = Duck('唐老鸭')
print(donald.name)
donald.name = 'Donald Duck'
print(donald.name)
