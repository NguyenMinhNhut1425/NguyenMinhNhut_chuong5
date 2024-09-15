# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 17:02:10 2024

@author: MINH NHUT
17. **Bàn cờ:** Viết chương trình nhận một tham số dòng lệnh là số nguyên n và in ra mô hình bàn cờ hai chiều n-by-n với các dấu cách và dấu sao xen kẽ, giống như mô hình 4-by-4 sau.

```
* * * *
 * * * *
* * * *
 * * * *
```
"""

n = int(input("Nhập một số nguyên dương n: "))
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print("*", end="")
        else:
            print(" ", end="")
    print()