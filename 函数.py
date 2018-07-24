# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 10:01:28 2018

@author: 盖海炜
"""


def day(a,b):
    print('day'+str(a))
    print('description:'+str(data['list'][b]['weather'][0]['main']))
    print('temperature:'+str(data['list'][b]['main']['temp']))
    print('pressure:'+str(data['list'][b]['main']['pressure']))
    print('temp_max:'+str(data['list'][b]['main']['temp_max']))
    print('temp_min:'+str(data['list'][b]['main']['temp_min']))
day(1,2)
day(2,10)
day(3,18)
day(4,26)
day(5,34)

def chart(d):
    return '-'*int(data['list'][d]['main']['temp'])
print(chart(2))
print(chart(10))
print(chart(18))
print(chart(26))
print(chart(34))
