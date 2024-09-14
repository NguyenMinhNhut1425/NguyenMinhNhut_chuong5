# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:12:55 2024

@author: MINH NHUT
"""

n = int(input("Nhập vào số nguyên dương n: "))
for i in range(2, n):
    if n % i == 0:
        print(n,"không phải là số nguyên tố")
        break
else:
    print(n,"là số nguyên tố")