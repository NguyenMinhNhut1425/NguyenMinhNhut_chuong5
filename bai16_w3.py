# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 16:46:47 2024

@author: MINH NHUT
16. **Biểu diễn nhị phân:** Viết chương trình nhận một tham số dòng lệnh là số nguyên dương n, đặt biểu diễn nhị phân của n vào một chuỗi và sau đó in chuỗi đó.

"""

n = int(input("Nhập một số nguyên dương n: "))
nhi_phan = ""
so = n
if so == 0:
    nhi_phan = "0"
else:
    while so > 0:
        ma = so % 2
        nhi_phan = str(ma) + nhi_phan
        so = so // 2
print(f"Biểu diễn nhị phân của {n} là: {nhi_phan}") 
