# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 09:45:24 2018

@author: Me
"""
try:
    3/1
    3/0
except Exception as err:  
    print('发生了异常')
print('end')   
#*****************************
# =============================================================================
# 异常处理机制语法:
try:
    指令集合(可能会发生异常的指令)
except Exception as err:
    指令集合
# =============================================================================
    