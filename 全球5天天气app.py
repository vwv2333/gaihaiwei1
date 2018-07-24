# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 16:44:59 2018
,0练习题4：
1.打印每天18点的天气信息，温度，程序，情况，气压，最高温度，最低温度
2.写出英文版的天气-天气情况，用户输入英文   application应用
3.打印温度折线图
    1----------
    2--------------------
    3-------
    4----------
4.获取所有的温度，并且排序（sorted([1,4,-1,8])##########使用此方法排序）
5.友情提示，根据温度提示穿衣，打伞，出门(可选)

全球5天天气
@author: Administrator
"""
url='http://api.openweathermap.org/data/2.5/forecast?q=yantai,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)


print('the weather at18:0 in the first day')
print('city:yantai')
print('description:'+str(data['list'][2]['weather'][0]['main']))
print('temperature:'+str(data['list'][2]['main']['temp']))
print('pressure:'+str(data['list'][2]['main']['pressure']))
print('temp_max:'+str(data['list'][2]['main']['temp_max']))
print('temp_min:'+str(data['list'][2]['main']['temp_min']))

print('the weather at18:0 in the second day')
print('city:yantai')
print('description:'+str(data['list'][10]['weather'][0]['main']))
print('temperature:'+str(data['list'][10]['main']['temp']))
print('pressure:'+str(data['list'][10]['main']['pressure']))
print('temp_max:'+str(data['list'][10]['main']['temp_max']))
print('temp_min:'+str(data['list'][10]['main']['temp_min']))


print('the weather at18:0 in the third day')
print('city:yantai')
print('description:'+str(data['list'][18]['weather'][0]['main']))
print('temperature:'+str(data['list'][18]['main']['temp']))
print('pressure:'+str(data['list'][18]['main']['pressure']))
print('temp_max:'+str(data['list'][18]['main']['temp_max']))
print('temp_min:'+str(data['list'][18]['main']['temp_min']))

print('the weather at18:0 in the fourth day')
print('city:yantai')
print('description:'+str(data['list'][26]['weather'][0]['main']))
print('temperature:'+str(data['list'][26]['main']['temp']))
print('pressure:'+str(data['list'][26]['main']['pressure']))
print('temp_max:'+str(data['list'][26]['main']['temp_max']))
print('temp_min:'+str(data['list'][26]['main']['temp_min']))

print('the weather at18:0 in the fifth day')
print('city:yantai')
print('description:'+str(data['list'][34]['weather'][0]['main']))
print('temperature:'+str(data['list'][34]['main']['temp']))
print('pressure:'+str(data['list'][34]['main']['pressure']))
print('temp_max:'+str(data['list'][34]['main']['temp_max']))
print('temp_min:'+str(data['list'][34]['main']['temp_min']))

print('-'*int(data['list'][2]['main']['temp']))
print('-'*int(data['list'][10]['main']['temp']))
print('-'*int(data['list'][18]['main']['temp']))
print('-'*int(data['list'][26]['main']['temp']))
print('-'*int(data['list'][34]['main']['temp']))

a=data['list'][2]['main']['temp']
b=data['list'][10]['main']['temp']
c=data['list'][18]['main']['temp']
d=data['list'][26]['main']['temp']
e=data['list'][34]['main']['temp']
print('the sorted tempreture is:')
print(sorted([a,b,c,d,e]))





'''
使用多项选一，完成天气的提醒，淘宝客户端
一定要多次使用佛如循环，偶尔使用while，在淘宝客户端中
使用break或者continue 在淘宝客户端中
'''
def day(a,b):
    print('description:'+str(data['list'][b]['weather'][0]['main']))
    print('temperature:'+str(data['list'][b]['main']['temp']))
    print('pressure:'+str(data['list'][b]['main']['pressure']))
    print('temp_max:'+str(data['list'][b]['main']['temp_max']))
    print('temp_min:'+str(data['list'][b]['main']['temp_min']))
    a=str(data['list'][b]['weather'][0]['main'])
    if a=='Clear':
        print('天气不错，出去走走吧')
    elif a=='Clouds':
        print('没有太阳，注意保暖')
    elif a=='Rain':
        print('下雨了，记得带伞')
day(1,2)
day(2,10)
day(3,18)
day(4,26)
day(5,34)









  
