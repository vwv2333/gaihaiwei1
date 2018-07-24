# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 10:00:50 2018

@author: 盖海炜
"""

ls=[5,9,3,8,1]
max(ls)#系统的内置函数或关键词
min(ls)#最小数
len(ls)#长度
a=sorted(ls)#排序，默认是升序，没有改变原来list的结构，重新生成了一个列表
ls.append(99)#追加
ls.remove(99)#remove元素
b=reversed(ls)#列表倒置——————》list（b）