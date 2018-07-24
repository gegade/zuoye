# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 14:09:53 2018
data1=[]
data2=[]
file2=open('招生信息.txt',encoding='gbk').readlines()
f2=open('学校.txt','a',encoding='gbk')
f3=open('人数.txt','a',encoding='gbk')
for  j in range(len(file2)): 
    data1.append('\''+file2[j].split('(')[1].split(',')[0]+'\''+',')
    data2.append(file2[j].split(',')[1].split(')')[0]+',')     
for i in data1:
    f2.write(i)
f2.close
for j in data2:
    f3.write(j)
f3.close


@author: Me
"""
