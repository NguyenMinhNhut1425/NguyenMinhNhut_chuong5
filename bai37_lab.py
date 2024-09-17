# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:34:01 2024

@author: MINH NHUT
"""

n = int(input("Nhập vào số chẵn dương n để tính(2 + 4 + 6 + ... + n) "))
tinh = 0
while n <= 0 and n % 2 != 0:
    n = int(input("Nhập lại n là số chẵn dương: "))
for i in range (2, n + 1, 2):
    tinh += i
print("Kết quả là: ",tinh)