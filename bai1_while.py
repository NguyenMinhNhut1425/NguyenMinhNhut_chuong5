# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 01:05:34 2024

@author: MINH NHUT
"""

so = float(input("Nhập vào số [-99; 99] : "))
while so < -99 or so > 99:
    so = float(input("Không đúng, nhập lại ik từ -99 đến 99 cơ: "))