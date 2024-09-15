# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 23:47:54 2024

@author: MINH NHUT
4. **Đếm số nguyên tố:** Viết chương trình nhận một tham số dòng lệnh n và in ra số lượng số nguyên tố nhỏ hơn n. Sử dụng nó để in ra số lượng số nguyên tố nhỏ hơn 10 triệu. Lưu ý: nếu bạn không cẩn thận để làm cho chương trình của mình hiệu quả, nó có thể sẽ không kết thúc trong một khoảng thời gian hợp lý.

"""

import math

n = int(input("Nhập vào n: "))
so_nguyen_to = [True] * n 
so_nguyen_to[0] = so_nguyen_to[1] = False 
for i in range(2, int(math.sqrt(n)) + 1):
    if so_nguyen_to[i] == True:
        for j in range(i * i, n, i):
            so_nguyen_to[j] = False 
so_luong = sum(so_nguyen_to)
print(f"Số lượng số nguyên tố nhỏ hơn {n} là: {so_luong}")