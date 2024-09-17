# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:37:10 2024

@author: MINH NHUT
"""

n = int(input("Nhập vào số lẻ dương n để tính(1 * 2 * 3 * ... * n) "))
tinh = 1
while n <= 0:
    n = int(input("Nhập lại n là số nguyên dương: "))
for i in range (1, n + 1):
    tinh = tinh * i
print("Kết quả là: ",tinh)