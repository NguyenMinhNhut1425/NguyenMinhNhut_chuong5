# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:11:43 2024

@author: MINH NHUT
"""

import random
so_luong = 0
for i in range(random.randrange(1,12)):
    so = random.randrange(20,31)
    print(so, end='\t')
    so_luong += 1
print("\nSố lượng phần tử đã in ra là: ", so_luong)