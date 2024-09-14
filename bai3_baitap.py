# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 01:35:51 2024

@author: MINH NHUT
"""

n = int(input("Nhập giá trị n: "))
dic = {i:i**i for i in range(1, n+1)}
print(dic)