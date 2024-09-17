# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 17:13:17 2024

@author: MINH NHUT
"""

n = int(input("Nhập vào số nguyên n để tính(1/2 + 2/3 + ... + n/(n+1) "))
tinh = 0
while n <= 0:
    n = int(input("Nhập lại n là số nguyên dương: "))
for i in range (1, n + 1):
    tinh += i / (i + 1)
print("Kết quả là: ",tinh)