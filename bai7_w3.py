# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 02:20:08 2024

@author: MINH NHUT
"""
# 7. **In số nguyên theo dòng:** Viết chương trình sử dụng một vòng lặp `for` và một câu lệnh `if` để in các số nguyên từ 1000 (bao gồm) đến 2000 (không bao gồm) với năm số nguyên trên mỗi dòng.

so_tren_dong = 0  
for i in range(1000, 2000):
    print(i, end=" ")  
    so_tren_dong += 1
    
    if so_tren_dong == 5:
        print()
        so_tren_dong = 0
