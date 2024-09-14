# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 01:13:10 2024

@author: MINH NHUT
"""

ds = [i for i in range(2020,3839) if i % 2 == 0]
new_ds = [x for x in ds if x % 9 == 0]
for e in new_ds:
    print(e, end='\t')