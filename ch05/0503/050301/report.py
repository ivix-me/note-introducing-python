# -*- coding: utf-8 -*-


def get_description():
    """返回随机的天气"""
    from random import choice
    possibilities = ['雨', '雪', '雨夹雪', '雾', '晴', '谁知道呢']
    return choice(possibilities)