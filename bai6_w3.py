# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 02:09:22 2024

@author: MINH NHUT
"""
8. **Số ngẫu nhiên:** Viết chương trình nhận một số nguyên n làm tham số dòng lệnh, sử dụng `random.random()` để tạo ra n số ngẫu nhiên đều trong khoảng từ 0 đến 1, sau đó in ra giá trị trung bình, giá trị nhỏ nhất và giá trị lớn nhất của chúng.8. **Số ngẫu nhiên:** Viết chương trình nhận một số nguyên n làm tham số dòng lệnh, sử dụng `random.random()` để tạo ra n số ngẫu nhiên đều trong khoảng từ 0 đến 1, sau đó in ra giá trị trung bình, giá trị nhỏ nhất và giá trị lớn nhất của chúng.
# In số nguyên từ 1000 đến 1999, 5 số trên mỗi dòng
count = 0  # Biến đếm để theo dõi số lượng số đã in ra trên mỗi dòng

for i in range(1000, 2000):
    print(i, end=" ")  # In số nguyên trên cùng một dòng, cách nhau bởi dấu cách
    count += 1
    
    # Nếu đã in ra 5 số, in xuống dòng mới và đặt lại biến đếm
    if count == 5:
        print()  # In xuống dòng
        count = 0
 in ra trên mỗi dòng

for i in range(1000, 2000):
    print(i, end=" ")  # In số nguyên trên cùng một dòng, cách nhau bởi dấu cách
    count += 1
    
    # Nếu đã in ra 5 số, in xuống dòng mới và đặt lại biến đếm
    if count == 5:
        print()  # In xuống dòng
        count = 0 in ra trên mỗi dòng

for i in range(1000, 2000):
    print(i, end=" ")  # In số nguyên trên cùng một dòng, cách nhau bởi dấu cách
    count += 1
    
    # Nếu đã in ra 5 số, in xuống dòng mới và đặt lại biến đếm
    if count == 5:
        print()  # In xuống dòng
        count = 0n dòng chữ "Hello" từ tham số nhập vào. Giả sử tham số nhỏ hơn 1000.
n = int(input("Nhập vào số lần in dòng chữ 'Hello' (nhỏ hơn 1000): "))
if n < 1000:
    for i in range(n):
        print("Hello")
else:
    print("Nhập số nhỏ hơn 1000.")