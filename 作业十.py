# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 17:05:34 2018
请求的URL
http://www.gaokaopai.com/university-ajaxGetMajor.html
求情的数据
id=3319&type=2&city=34&state=1
学校编号   理科2        城市        正常
@author: Administrator
"""
ls=open('all_school.txt',encoding='utf-8').readlines()
schoolls=[]
for line in ls:
    schoolls.append(line.split('-jianjie-')[1].split('.')[0])
    
import urllib.request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
headers={'User-Agent':' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
         'X-Requested-With': 'XMLHttpRequest'}

f=open('广西理科招生人数1.txt','a+',encoding='utf-8')
for schoolid in schoolls[0:2400]:
    for kemu in [1,2]:
        try:
            req=r.Request(url,data='id={}&type={}&city=45&state=1'.format(schoolid,kemu).encode(),headers=headers)
            f.write(r.urlopen(req).read().decode('utf-8','ignore')+'\n')
            print('学校'+schoolid+'爬取成功')
        except Exception as err:
            print('学校'+schoolid+'爬取错误')
f.close()











