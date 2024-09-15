# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 15:18:36 2024

@author: MINH NHUT
"""

#12. **Dãy Fibonacci:** Viết chương trình in 100 số đầu tiên của dãy số fibonacci ra màn hình.

so_truoc = 0
so_sau = 1

print(so_truoc, so_sau, end=" ")
for i in range(98):
    so_ke = so_truoc + so_sau
    print(so_ke, end=" ")
    so_truoc = so_sau
    so_sau = so_ke