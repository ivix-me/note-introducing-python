# -*- coding: utf-8 -*-


class Word:
    def __init__(self, text):
        self.text = text

    def __eq__(self, w):
        return self.text.lower() == w.text.lower()

    def __str__(self):
        return self.text

    def __repr__(self):
        return 'Word("' + self.text + '")'

    def __add__(self, other):
        return self.text + other.text

    def __mul__(self, other):
        try:
            num = int(other)
            return self.text * num
        except:
            return self.text


first = Word('ha')
second = Word('HA')
third = Word('eh')

print(first, second, third)
print(first + third)
print(first * 8)
