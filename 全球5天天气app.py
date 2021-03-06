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
url='http://api.openweathermap.org/data/2.5/forecast?q=beijing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)
print('第一天18:00的天气状况')
print('温度：'+str(data['list'][2]['main']['temp']))
print('气压：'+str(data['list'][2]['main']['pressure']))
print('状况：'+str(data['list'][2]['weather'][0]['description']))
print('最高气温：'+str(data['list'][2]['main']['temp_max']))
print('最低气温：'+str(data['list'][2]['main']['temp_min']))

print('第二天18:00的天气状况')
print('温度：'+str(data['list'][10]['main']['temp']))
print('气压：'+str(data['list'][10]['main']['pressure']))
print('状况：'+str(data['list'][10]['weather'][0]['description']))
print('最高气温：'+str(data['list'][10]['main']['temp_max']))
print('最低气温：'+str(data['list'][10]['main']['temp_min']))


print('第三天18:00的天气状况')
print('温度：'+str(data['list'][18]['main']['temp']))
print('气压：'+str(data['list'][18]['main']['pressure']))
print('状况：'+str(data['list'][18]['weather'][0]['description']))
print('最高气温：'+str(data['list'][18]['main']['temp_max']))
print('最低气温：'+str(data['list'][18]['main']['temp_min']))



print('第四天18:00的天气状况')
print('温度：'+str(data['list'][26]['main']['temp']))
print('气压：'+str(data['list'][26]['main']['pressure']))

print('状况：'+str(data['list'][26]['weather'][0]['description']))
print('最高气温：'+str(data['list'][26]['main']['temp_max']))
print('最低气温：'+str(data['list'][26]['main']['temp_min']))


print('第五天18:00的天气状况')
print('温度：'+str(data['list'][34]['main']['temp']))
print('气压：'+str(data['list'][34]['main']['pressure']))
print('状况：'+str(data['list'][34]['weather'][0]['description']))
print('最高气温：'+str(data['list'][34]['main']['temp_max']))
print('最低气温：'+str(data['list'][34]['main']['temp_min']))
print('the first day:','-'*int(data['list'][2]['main']['temp']))
print('the second day:','-'*int(data['list'][10]['main']['temp']))
print('the third day:','-'*int(data['list'][18]['main']['temp']))
print('the forth day:','-'*int(data['list'][26]['main']['temp']))
print('the fifth day:','-'*int(data['list'][34]['main']['temp']))
temps=[data['list'][2]['main']['temp'],data['list'][10]['main']['temp'],
data['list'][18]['main']['temp'],data['list'][26]['main']['temp'],data['list'][34]['main']['temp']]
print('排序后的温度为:')
print(sorted([temps[0:5]]))