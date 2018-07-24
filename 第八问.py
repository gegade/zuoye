# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 15:09:36 2018

@author: Me
"""

def page(i):  
        import urllib.request as r#导入联网工具包，名为为r
        url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&type=p&tmhkh5=&spm=a21wu.241046-global.a2227oh.d100&from=sea_1_searchbutton&catId=100&loc=%E6%B2%B3%E5%8C%97&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s={}&ajax=true'.format(44*i)
        data=r.urlopen(url).read().decode('utf-8','ignore')
        import json#将字符串转换为字典
        data=json.loads(data)       
        def tt(j):
            return  data['mods']['itemlist']['data']['auctions'][j]['title']
        def pri(j):
            return  data['mods']['itemlist']['data']['auctions'][j]['view_price']  
        def loc(j): 
            return  data['mods']['itemlist']['data']['auctions'][j]['item_loc']
        print('第{}页商品的信息：'.format(i+1)+'\n')
        try:  
           for j in range (36):       
               b=open('F:\大数据实训\数据信息.txt','a',encoding='utf-8')        
               b.write('商品名：'+str(tt(j))+'发货地：'+str(loc(j))+'价格'+str(pri(j)))
               print('正在写入第{}页第{}件商品的信息！'.format(i+1).format(j+1))
               b.close
        except Exception as err:
               print('写入第{}页第{}件商品的信息！'.format(i+1).format(j+1))            
for i in range(100):
    page(i)



'''
for i in range(100):
    try:
        url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&type=p&tmhkh5=&spm=a21wu.241046-global.a2227oh.d100&from=sea_1_searchbutton&catId=100&loc=%E6%B2%B3%E5%8C%97&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s={}&ajax=true'.format(44*i)
        data=r.urlopen(url.format(44*i)).read().decode('utf-8','ignore')
        f=open('taobaoshuju.csv','a',encoding='utf-8')
        print('正在进行第{}页的写入'.format(i+1))
        f.write(str(data)+'\n')  
        f.close
    except Exception as err:
        print('写入错误！')
'''