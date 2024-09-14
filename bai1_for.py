# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 18:11:13 2024

@author: MINH NHUT
"""

n = int(input("Nhập vào số n (nguyên dương) tính giai thừa: "))
S = 1
for i in range(1, n + 1):
    S *= i
print(f"{n} giai thừa là {n}! = {S}")