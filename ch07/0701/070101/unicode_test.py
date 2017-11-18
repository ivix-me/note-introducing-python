# -*- coding: utf-8 -*-


def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s", name="%s", value2="%s"' % (value, name, value2))


unicode_test('A')
unicode_test('宝')
unicode_test('玉')
unicode_test('\u00a2')
unicode_test('\u2603')
unicode_test('\u7389')
