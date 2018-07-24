# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 10:00:06 2018

@author: Me
"""
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 16:44:59 2018
练习题4：
1.打印每天18点的天气信息，温度，情况，气压，最高温度，最低温度
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
inputcity=input('请输入城市：')
url='http://api.openweathermap.org/data/2.5/forecast?q='+inputcity+',cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)

def weather(d:str,i):
    print('第',d,'天18:00的天气状况')
    print('温度：'+str(data['list'][i]['main']['temp']))
    print('气压：'+str(data['list'][i]['main']['pressure']))
    print('状况：'+str(data['list'][i]['weather'][0]['description']))
    print('最高气温：'+str(data['list'][i]['main']['temp_max']))
    print('最低气温：'+str(data['list'][i]['main']['temp_min']))
weather(1,2) 
weather(2,10) 
weather(3,18) 
weather(4,26) 
weather(5,34) 
def chart(a):
    return '-'*int(data['list'][a]['main']['temp'])
print('第1天的天气情况为：',chart(2))    
print('第2天的天气情况为：',chart(10))    
print('第3天的天气情况为：',chart(18))   
print('第4天的天气情况为：',chart(26))
print('第5天的天气情况为：',chart(34)) 

def lss(a):
    return data['list'][a]['main']['temp']
tem0=lss(0);
tem1=lss(1);
tem2=lss(2);
tem3=lss(3);
tem4=lss(4);
tems=[tem0,tem1,tem2,tem3,tem4]
print(sorted(tems))