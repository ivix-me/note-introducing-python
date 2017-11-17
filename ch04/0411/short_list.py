# -*- coding: utf-8 -*-


short_list = [1, 2, 3]

pos = 5

try:
    print(short_list[pos])
except:
    print('位置需要在 0 和', len(short_list) - 1, '之间，但你传入的是：', pos)
