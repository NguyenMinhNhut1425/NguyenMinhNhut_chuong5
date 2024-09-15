# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 15:45:35 2024

@author: MINH NHUT

15. **Chuyển đổi cơ số:** Tạo chương trình nhận i và k làm tham số dòng lệnh và chuyển đổi i sang cơ số k. Giả sử k là một số nguyên từ 2 đến 16. Đối với cơ số lớn hơn 10, sử dụng các chữ cái từ A đến F để biểu thị các chữ số từ 11 đến 16. Với số nhập vào từ người dùng.
"""

i = int(input("Nhập số nguyên i (cơ số 10): "))
k = int(input("Nhập cơ số k (từ 2 đến 16): "))

if k < 2 or k > 16:
    print("Cơ số k phải từ 2 đến 16.")
else:

    digits = "0123456789ABCDEF"

    result = ""
    num = i 

    while num > 0:
        remainder = num % k
        result = digits[remainder] + result
        num = num // k

    if result == "":
        result = "0"  
    print(f"Số {i} trong cơ số {k} là: {result}")
