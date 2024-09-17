# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:17:56 2024

@author: MINH NHUT
"""

n = int(input("Nhập vào số nguyên dương n để tính(1 + 2 + 3 + ... + n) "))
tinh = 0
while n <= 0:
    n = int(input("Nhập lại n là số nguyên dương: "))
for i in range (1, n + 1):
    tinh += i
print("Kết quả là: ",tinh)