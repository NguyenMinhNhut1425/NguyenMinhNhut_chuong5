# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:39:48 2024

@author: MINH NHUT
"""

so_km = int(input("Nhập vào số km TAXI đi được: "))
so_tien = 0
for km in range(1, so_km + 1):
    if km == 1:
        so_tien += 15000
    elif 2 <= km <= 5:
        so_tien += 13500
    elif km >= 6:
        so_tien += 11000
if so_km > 120:
    so_tien = so_tien * 0.9
print(f"Tiền cước TAXI phải trả là: {so_tien} đồng")
