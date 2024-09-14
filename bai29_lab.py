# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:29:20 2024

@author: MINH NHUT
"""

N = int(input("Nhập vào số nguyên dương N: "))
tong = 0
for i in str(N):
    tong += int(i)
print(f"Tổng các chữ số của N là: {tong}")