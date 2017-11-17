# -*- coding: utf-8 -*-


class Duck:
    def __init__(self, input_name, gender):
        self.hidden_name = input_name
        self.hidden_gender = gender

    @property
    def name(self):
        print('name getter')
        return self.hidden_name

    @name.setter
    def name(self, input_name):
        print('name setter')
        self.hidden_name = input_name

    @property
    def gender(self):
        return self.hidden_gender

    @gender.setter
    def gender(self, gender):
        self.hidden_gender = gender


donald = Duck('唐老鸭', '公')
print(donald.name, '是只欢乐的小', donald.gender, '鸭')
