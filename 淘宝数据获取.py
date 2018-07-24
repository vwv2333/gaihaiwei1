# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 10:15:03 2018

@author: 盖海炜
"""

url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&style=grid&loc=%E7%A6%8F%E5%B7%9E&ajax=true'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ignore')
##import json#将字符串转换为字典
##data=json.loads(data)


f=open('temp3.txt','w',encoding='utf-8')
f.write(data)
f.close()
for s in range(0,4400,44):
    try:
        url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&style=grid&loc=%E7%A6%8F%E5%B7%9E&ajax=true&s={}'
        import urllib.request as r
        data=r.urlopen(url.format(s)).read().decode('utf-8','ignore')
        f=open('temp3.txt','a',encoding='utf-8')
        f.write(data+'\n')
        f.close()
        print('第{}页已完成'.format(s/44))    
    except Exception as err:
        print('爬取异常')
        
'''
练习8：保存淘宝数据(小组项目)
1.每个组员爬取某个商品的100页数据 每个组员爬取的不同的城市，上海 北京 成都 郑州 组间城市不重复
2.保存淘宝商品信息(同练习题6)，并且保存为csv格式
3.每组组长合并各组员的数据  -后续班级合并数据
'''























        
    