# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:14:20 2024

@author: MINH NHUT
liệt kê tất cả bộ nghiệm nguyên của: 2x + 7y + 9z = 979 với x, y, z > 0 và x + y + z nhỏ nhất
"""

min_sum = float('inf')
for x in range(1, 490):
    for y in range(1, 140):
        for z in range(1, 110):         
            if 2*x + 7*y + 9*z == 979:
                tong = x + y + z
                if tong < min_sum:  
                    min_sum = tong
                    so_nho_nhat = (x, y, z)
print("Bộ nghiệm có tổng các nghiệm nhỏ nhất là",so_nho_nhat,"với tổng =",min_sum)