# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 11:35:33 2018

@author: Me
"""
url='https://s.taobao.com/search?spm=a21bo.2017.201856-fline.8.5af911d9k5kVge&q=%E5%A2%99%E7%BA%B8&refpid=430148_1006&source=tbsy&style=grid&tab=all&pvid=d0f2ec2810bcec0d5a16d5283ce59f70&ajax=true'
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')
import json#将字符串转换为字典
data=json.loads(data)
for i in range(0,4):
    print('第'+str(i+1)+'件商品的信息：')
    #print('第{}件商品的信息：'.format(i+1))
    print(data['mods']['itemlist']['data']['auctions'][i]['title'])
    print(data['mods']['itemlist']['data']['auctions'][i]['view_price'])
    print(data['mods']['itemlist']['data']['auctions'][i]['item_loc'])
    print(data['mods']['itemlist']['data']['auctions'][i]['view_sales'])
    print(data['mods']['itemlist']['data']['auctions'][i]['nick'])
def descs():
        for i in range(0,36):
           print('第'+str(i+1)+'件商品的信息：')
           #print('第{}件商品的信息：'.format(i+1))
           print(data['mods']['itemlist']['data']['auctions'][i]['title'])
           print(data['mods']['itemlist']['data']['auctions'][i]['view_price'])
           print(data['mods']['itemlist']['data']['auctions'][i]['item_loc'])
           print(data['mods']['itemlist']['data']['auctions'][i]['view_sales'])
           print(data['mods']['itemlist']['data']['auctions'][i]['nick'])
           if((i+1)%4==0):
               print('*'*50)
               continue
           elif(i>=36):
               break
descs()
p=[]
s=[]
for i in range (0,36):
    a=data['mods']['itemlist']['data']['auctions'][i]['view_price'] 
    p.append(a)    
ascend=sorted(p)
descend=list(reversed(ascend))
print('第一页商品价格从高到低的顺序为：')
print(descend)
for i in range (0,36):
    b=str(data['mods']['itemlist']['data']['auctions'][i]['view_sales'])
    d=int(b[0:-3])
s.append(d)
asc=sorted(s)
des=list(reversed(asc))
print('第一页商品销售从高到低的顺序为：')
print(des)
for i in range(36):
    if (float(data['mods']['itemlist']['data']['auctions'][i]['view_fee'])==0.00):
        print('第{}件商品包邮'.format(i+1))
        
        