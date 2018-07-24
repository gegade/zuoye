# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 09:57:27 2018

@author: Me
"""
import urllib.request as r#导入联网工具包，名为为r
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