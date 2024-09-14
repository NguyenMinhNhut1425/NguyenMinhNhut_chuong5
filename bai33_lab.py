# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:55:54 2024

@author: MINH NHUT
"""

n = int(input("Nhập vào số nguyên dương n: "))
for i in range(1, n + 1):
    if i * i == n:
        print(n,"là số chính phương")
        break
else:
    print(n,"không phải là số chính phương")