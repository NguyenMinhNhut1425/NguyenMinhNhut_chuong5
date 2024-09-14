# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:04:46 2024

@author: MINH NHUT
"""

chuoi = input("Nhập vào một chuỗi: ")
len(chuoi)
ky_tu_db = '!@#$%^&*()-=+./'
day_ky_tu_db = [i for i in chuoi if i in ky_tu_db]
print(day_ky_tu_db)
print(len(day_ky_tu_db))
       
ky_tu_thuong = [e for e in chuoi if e.islower()]
print(ky_tu_thuong)
print(len(ky_tu_thuong))

ky_tu_so = [s for s in chuoi if s.isdigit()]
print(ky_tu_so)
print(len(ky_tu_so))
    
ky_tu_hoa = [h for h in chuoi if h.isupper()]
print(ky_tu_hoa)
print(len(ky_tu_hoa))