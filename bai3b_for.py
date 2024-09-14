# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 23:40:47 2024

@author: MINH NHUT
"""

import random
so_luong = 0
for i in range(random.randrange(1,83)):
    so = random.uniform(18, 99)
    binh_phuong = so ** 2
    so_luong += 1
    print(so,"\u00B2 = ", binh_phuong, end=',\t')
print("\nCó tất cả ", so_luong, "số bình phương")   