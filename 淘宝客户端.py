# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 14:03:08 2018
3.获取所有价格并从高到低排序
4.按照销量排序
5.商品过滤，只要15天退款或者包邮，显示
@author: 盖海炜
"""

url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&ajax=true'
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)

for a in range(0,36):
    print('title:'+data['mods']['itemlist']['data']['auctions'][a]['raw_title'])
    print('price:'+data['mods']['itemlist']['data']['auctions'][a]['view_price'])
    print('loc:'+data['mods']['itemlist']['data']['auctions'][a]['item_loc'])
    print('nick:'+data['mods']['itemlist']['data']['auctions'][a]['nick'])
    print('sales:'+data['mods']['itemlist']['data']['auctions'][a]['view_sales'])
    if (a+1)%4==0:
        print('-'*60)
    while a==50:
        continue
    if a==35:
        break



























'''
ls=[]
for i in range(0,36):
    x=float(data['mods']['itemlist']['data']['auctions'][i]['view_price'])
    ls.append(x)
    b=sorted(ls)
    c=list(reversed(b))
print('商品价格从高到低排序为：'+str(c))

ls1=[]
for e in range(0,36):
    y=float(data['mods']['itemlist']['data']['auctions'][e]['view_sales'])
    ls1.append(y)
    f=sorted(ls1)
    g=list(reversed(f))
print('商品销量从高到低排序为：'+str(g))
    
    
    
    
    
    
    
    
    
    
    
    
