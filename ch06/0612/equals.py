# -*- coding: utf-8 -*-


class Word:
    def __init__(self, text):
        self.text = text

    def __eq__(self, w):
        return self.text.lower() == w.text.lower()


first = Word('ha')
second = Word('HA')
third = Word('eh')

# print(first.equals(second))
# print(first.equals(third))

print(first == second)
print(first == third)
