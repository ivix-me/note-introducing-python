# -*- coding: utf-8 -*-


class Car:
    def exclaim(self):
        print('我是一辆车')


class Toyota(Car):
    def exclaim(self):  # 覆盖父类的方法
        print('我是丰田，我是一辆车，有丰田特色的车')

    def need_a_push(self):  # 添加新方法
        print('需要帮助？')


if __name__ == '__main__':
    give_me_a_car = Car()
    give_me_a_toyota = Toyota()

    give_me_a_car.exclaim()
    give_me_a_toyota.exclaim()

    give_me_a_toyota.need_a_push()
