# -*- coding: utf-8 -*-


from sources import daily, weekly

print('今日天气：', daily.forecast())
print('本周天气：')
for number, outlook in enumerate(weekly.forecast(), 1):
    print(number, outlook)