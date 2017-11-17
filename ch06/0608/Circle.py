# -*- coding: utf-8 -*-


class Circle:
    """圆形"""

    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius


if __name__ == '__main__':
    c = Circle(5)
    print('半径：%d，直径：%d' % (c.radius, c.diameter))
