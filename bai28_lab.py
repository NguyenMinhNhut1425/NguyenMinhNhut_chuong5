# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 21:12:25 2024

@author: MINH NHUT
"""

while True:
    so = input("Nhập vào số nguyên dương: ")
    if so.isdigit() and int(so) > 0:
        so = int(so)
        break
    else:
        print("Vui lòng nhập một số nguyên dương.")
        continue
print(f"Các ước của {so} là:")
for i in range(1,so):
    if so % i == 0:
       print(i, end='\t')