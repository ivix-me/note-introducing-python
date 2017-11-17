# -*- coding: utf-8 -*-


class Duck:
    def __init__(self, input_name):
        self.hidden_name = input_name

    def get_name(self):
        print('getter')
        return self.hidden_name

    def set_name(self, input_name):
        print('setter')
        self.hidden_name = input_name

    name = property(get_name, set_name)


donald = Duck('唐老鸭')
print(donald.name)
donald.name = 'Donald Duck'
print(donald.name)
