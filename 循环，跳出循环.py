# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 21:25:02 2018

@author: Me
"""
url='https://s.taobao.com/search?spm=a21bo.2017.201856-fline.8.5af911d9k5kVge&q=%E5%A2%99%E7%BA%B8&refpid=430148_1006&source=tbsy&style=grid&tab=all&pvid=d0f2ec2810bcec0d5a16d5283ce59f70&ajax=true'
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')
import json#将字符串转换为字典
data=json.loads(data)
#打印第一页所有商品的价格
ls=[]
b=[]
def price():
     for i in range(0,36):      
         a=data['mods']['itemlist']['data']['auctions'][i]['view_price']       
         if (str(a[i])<=20):
             print('价格太低，不予考虑')
             price()
            continue
            elif(a<=50):
            print('价格合理，查找自己喜欢的壁纸即可')
            price()       
        elif(a>50):
            print('有点小贵，不予考虑')
            price()
            break
 #查找价格在20~50的墙纸

