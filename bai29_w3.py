# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 17:27:29 2024

@author: MINH NHUT
29. **Số nguyên tố cùng nhau:** Viết chương trình nhận một tham số dòng lệnh n và in ra bảng n-by-n sao cho có dấu * ở hàng i và cột j nếu gcd của i và j là 1 (i và j là số nguyên tố cùng nhau), và một khoảng trắng ở vị trí đó.

"""

n = int(input("Nhập một số nguyên dương n: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        a, b = i, j

        while b != 0:
            a, b = b, a % b
        if a == 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
