# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 15:16:35 2024

@author: MINH NHUT
"""

#13. **Lũy thừa của 2:** Viết chương trình nhận một tham số dòng lệnh n và in ra tất cả các lũy thừa của 2 nhỏ hơn hoặc bằng n. Đảm bảo rằng chương trình của bạn hoạt động chính xác cho tất cả các giá trị của n. (Chương trình của bạn sẽ không in ra gì nếu n là số âm hoặc bằng 0).

n = int(input("Nhập vào số nguyên dương n: "))
if n > 0:
    i = 1
    while i <= n:
        print(i)
        i = i*2