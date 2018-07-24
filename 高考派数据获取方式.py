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

import urllib.request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'}
req=r.Request(url,data='id=3319&type=2&city=34&state=1'.encode(),headers=headers)
data=r.urlopen(req).read().decode('utf-8','ignore')
print(data)











