# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 17:20:37 2024

@author: MINH NHUT
28. **Ước chung lớn nhất:** Viết chương trình nhận hai số nguyên x và y từ dòng lệnh và tìm và in ra ước chung lớn nhất (gcd) của x và y bằng cách sử dụng thuật toán Euclid.

"""

# Nhập hai số nguyên x và y
x = int(input("Nhập số nguyên x: "))
y = int(input("Nhập số nguyên y: "))
while y != 0:
    x, y = y, x % y
print(f"Ước chung lớn nhất (gcd) của hai số là: {x}")
