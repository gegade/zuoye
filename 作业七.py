# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 20:20:59 2018

@author: Me
"""
url='http://api.openweathermap.org/data/2.5/forecast?q=chongqing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)
def weather(i,b):   
    print('第{}天18:00的天气状况'.format(i+1))
    print('温度：'+str(data['list'][b]['main']['temp']))
    print('状况：'+str(data['list'][b]['weather'][0]['description']))
    print('最高气温：'+str(data['list'][b]['main']['temp_max']))
    print('最低气温：'+str(data['list'][b]['main']['temp_min']))
for i in range(5):
    if (i%8==0):
            b=2
            weather(i,b) 
            if(data['list'][b]['weather'][0]['main']=='Rain'):
                print('You ''d better take your umbrella.')
            elif(data['list'][b]['weather'][0]['main']=='Clouds'):
                print('It’s a nice day')
            elif(data['list'][b]['weather'][0]['main']=='Clear'):
               print('Do a good job of sun protection') 
    elif(i%8==1):
            b=10
            weather(i,b)
            if(data['list'][b]['weather'][0]['main']=='Rain'):
                print('You ''d better take your umbrella.')
            elif(data['list'][b]['weather'][0]['main']=='Clouds'):
                print('It’s a nice day')
            elif(data['list'][b]['weather'][0]['main']=='Clear'):
               print('Do a good job of sun protection') 
    elif(i%8==2):
            b=18
            weather(i,b)
            if(data['list'][b]['weather'][0]['main']=='Rain'):
                print('You ''d better take your umbrella.')
            elif(data['list'][b]['weather'][0]['main']=='Clouds'):
                print('It’s a nice day')
            elif(data['list'][b]['weather'][0]['main']=='Clear'):
               print('Do a good job of sun protection') 
    elif(i%8==3):
            b=26
            weather(i,b)
            if(data['list'][b]['weather'][0]['main']=='Rain'):
                print('You ''d better take your umbrella.')
            elif(data['list'][b]['weather'][0]['main']=='Clouds'):
                print('It’s a nice day')
            elif(data['list'][b]['weather'][0]['main']=='Clear'):
               print('Do a good job of sun protection') 
    elif(i%8==4):
            b=34
            weather(i,b)
            if(data['list'][b]['weather'][0]['main']=='rain'):
                print('You ''d better take your umbrella.')
            elif(data['list'][b]['weather'][0]['main']=='clouds'):
                print('It’s a nice day')
            elif(data['list'][b]['weather'][0]['main']=='clear'):
               print('Do a good job of sun protection') 
    
    