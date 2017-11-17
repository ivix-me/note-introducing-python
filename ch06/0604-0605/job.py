# -*- coding: utf-8 -*-


class Person:
    def __init__(self, name):
        self.name = name


class Doctor(Person):
    def __init__(self, name):
        self.name = '都可·' + name


class Lawyer(Person):
    def __init__(self, name):
        self.name = name + ', 赖尔'


if __name__ == '__main__':
    person = Person('张三')
    doctor = Doctor('李四')
    lawyer = Lawyer('王五')
    print(person.name)
    print(doctor.name)
    print(lawyer.name)
