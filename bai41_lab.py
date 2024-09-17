# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 17:07:11 2024

@author: MINH NHUT
"""

n = int(input("Nhập vào số nguyên n để tính(1 + 1/3 + 1/5 + ... + 1/(2n+1)) "))
tinh = 0
while n <= 0:
    n = int(input("Nhập lại n là số nguyên dương: "))
for i in range (0, n + 1):
    tinh += 1 / ((2 * i) + 1)
print("Kết quả là: ",tinh)