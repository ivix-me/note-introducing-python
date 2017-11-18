# -*- coding: utf-8 -*-


from collections import namedtuple

Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')
print(duck)  # Duck(bill='wide orange', tail='long')
print(duck.bill, duck.tail)

parts = {'bill': 'wide orange', 'tail': 'long'}
duck2 = Duck(**parts)
print(duck2)
