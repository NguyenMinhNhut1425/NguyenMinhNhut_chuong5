# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:41:36 2024

@author: MINH NHUT
"""

thang = int(input("Nhập vào tháng : "))
nam = int(input("Nhập vào năm: "))
ngay_trong_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]   
if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    ngay_trong_thang[1] = 29
for i in range(1, 13):
    if thang == i:
        print(f"Tháng {thang} năm {nam} có {ngay_trong_thang[i-1]} ngày.")
        break