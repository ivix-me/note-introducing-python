# -*- coding: utf-8 -*-


short_list = [1, 2, 3]

while True:
    value = input('索引[q退出]:')
    if value == 'q':
        break
    try:
        pos = int(value)
        print(short_list[pos])
    except IndexError as err:
        print('错误的索引：', pos)
    except Exception as other:
        print('错误：', other)
