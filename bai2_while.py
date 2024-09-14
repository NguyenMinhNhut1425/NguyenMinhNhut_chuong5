# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 00:07:05 2024

@author: MINH NHUT
"""

so = float(input("Nhập vào số [-89.9; 88.8] : "))
while so < -89.9 or so > 88.8:
    so = float(input("Không đúng, nhập lại ik từ -89.9 đến 88.8 cơ: "))
    