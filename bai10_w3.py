# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 02:51:10 2024

@author: MINH NHUT
"""

#10. **Bảng giá trị hàm:** Viết chương trình in ra bảng giá trị của log n, n, n log n, n<sup>2</sup> và n<sup>3</sup> với n = 2, 4, 8, 16, 32, 64, 128. Sử dụng tab (`\t`) để căn chỉnh các cột.

import math

ds_n = [2, 4, 8, 16, 32, 64, 128]

print("n\t\tlog(n)\t\tn*log(n)\t\tn^2\t\t\tn^3")

for n in ds_n:
    log_n = math.log(n)
    n_log_n = n * log_n
    n_mu2 = n ** 2
    n_mu3 = n ** 3
    if n >= 32:
        print(f"{n}\t\t{log_n:.2f}\t\t{n_log_n:.2f}\t\t\t{n_mu2}\t\t{n_mu3}")
    else:
        print(f"{n}\t\t{log_n:.2f}\t\t{n_log_n:.2f}\t\t\t{n_mu2}\t\t\t{n_mu3}")


