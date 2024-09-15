# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 02:26:54 2024

@author: MINH NHUT
"""
#8. **Số ngẫu nhiên:** Viết chương trình nhận một số nguyên n làm tham số dòng lệnh, sử dụng `random.random()` để tạo ra n số ngẫu nhiên đều trong khoảng từ 0 đến 1, sau đó in ra giá trị trung bình, giá trị nhỏ nhất và giá trị lớn nhất của chúng.

import random
n = int(input("Nhập một số nguyên n: "))
so_ngau_nhien = [random.random() for i in range(n)]
trung_binh = sum(so_ngau_nhien) / n
nho_nhat = min(so_ngau_nhien)
lon_nhat = max(so_ngau_nhien)
print(f"Các số ngẫu nhiên: {so_ngau_nhien}")
print(f"Trung bình: {trung_binh}")
print(f"Giá trị nhỏ nhất: {nho_nhat}")
print(f"Giá trị lớn nhất: {lon_nhat}")
