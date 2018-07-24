# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 16:29:46 2018
去电影院之前先买个票(占位置)
@author: Administrator
"""
#占位符
'今天的温度是:{}'.format(3)
'q={}'.format('北京')
a='2013年4月3日'#字符串===类似于list  
b=list(a)
print(b[0]+b[1]+b[2]+b[3])
#从哪里到哪里的方法....切片
b[0:4]#   [0,4)
b[0]
b[8]#等价于b[-1]     
b[-1]########逆序切片
b[0:]
b[-1:]

a[0:4]
###################专门字符串的一些操作
'aaapythonaaa'.index('python')#要么找到位置，要么崩溃
'83874@qq.com'.endswith('@qq.com')#bool True,False
'yuqqqqq'.startswith('yu')####以xxx开始或者以xxx结尾
len('aaa')#######获取长度
len([1,1,1])
#键盘输入
mima=input('请输入密码')
print(mima)

############数字的功能扩展到字符串当中会出现什么结果
'a'*999







