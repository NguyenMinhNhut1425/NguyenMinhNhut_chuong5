# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:10:10 2024

@author: MINH NHUT
"""

a = int(input("Nhập vào số nguyên dương a: "))
b = int(input("Nhập vào số nguyên dương b: "))
c = int(input("Nhập vào số nguyên dương c: "))
cac_loai = [(a == b == c, "Đây là tam giác đều."),
    (a == b or b == c or a == c, "Đây là tam giác cân."),
    (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2, "Đây là tam giác vuông."),
    (a + b > c and a + c > b and b + c > a, "Đây là tam giác thường.")]
for dieu_kien, tam_giac in cac_loai:
    if dieu_kien:
        print(tam_giac)
        break
else:
    print("Đây không phải là tam giác")