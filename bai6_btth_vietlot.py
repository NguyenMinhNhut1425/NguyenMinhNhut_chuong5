# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 17:55:44 2024

@author: MINH NHUT
"""

import random
so_ve = int(input("Bạn muốn bao nhiêu vé số Vietlot: "))
tien_ve = 0
ds_cac_ve = []
for _ in range(1, so_ve + 1):
    tien_ve += 10000
    ve = []
    while len(ve) < 6:
        so = str(random.randint(1, 45))
        if so not in ve:
            ve += [so]
    ds_cac_ve += [ve]
n = 1
for i in ds_cac_ve:
    print(f"Vé thứ {n}: {'-'.join(i)}")
    n += 1
print(f"Tổng tiền mua vé số là: {tien_ve:,} đ")

ve_trung = []
while len(ve_trung) < 6:
    so_trung = str(random.randint(1, 45))
    if so_trung not in ve_trung:
        ve_trung += [so_trung]
print("\nVé số trúng thưởng là:",'-'.join(ve_trung))

giai_ba = 0
giai_hai = 0
giai_mot = 0
giai_db = 0
tien_trung_thuong = 0
for a in ds_cac_ve:
    
    so_giong_ve_trung = 0
    for e in range(6):
        if a[e] == ve_trung[e]:
            so_giong_ve_trung += 1
    
    if so_giong_ve_trung == 3:
        tien_trung_thuong += 300001
        giai_ba += 1
    elif so_giong_ve_trung == 4:
        tien_trung_thuong += 300000
        giai_hai += 1
    elif so_giong_ve_trung == 5:
        tien_trung_thuong += 10000000
        giai_mot += 1
    elif so_giong_ve_trung == 6:
        tien_trung_thuong += 10000000000
        giai_db += 1
print(f"Bạn trúng {giai_ba} giải ba, {giai_hai} giải hai, {giai_mot} giải một, {giai_db} giải đặc biệt")
print(f"Tổng số tiền trúng thưởng bạn nhận được: {tien_trung_thuong:,} đ")
    
    
    
    
    