# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 17:05:24 2024

@author: MINH NHUT
"""

n = int(input("Nhập vào số nguyên n để tính(1/2 + 1/4 + 1/6 + ... + 1/2n) "))
tinh = 0
for i in range (1, n + 1):
    tinh += 1 / (2 * i)
print("Kết quả là: ",tinh)