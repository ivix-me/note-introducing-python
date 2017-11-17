# -*- coding: utf-8 -*-


class Car:
    def exclaim(self):
        print('我是一辆车')


class Yugo(Car):
    pass


if __name__ == '__main__':
    give_me_a_car = Car()
    give_me_a_yugo = Yugo()

    give_me_a_car.exclaim()
    give_me_a_yugo.exclaim()
