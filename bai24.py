# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 10:25:46 2024

@author: ADMIN
"""

gio = int(input("Nhập giờ: "))
phut = int(input("Nhập phút: "))
giay = int(input("Nhập giây: "))
if 0 <= gio < 24 and 0 <= phut < 60 and 0 <= giay < 60:
    print("Thời gian hợp lệ.")
    print(f"{gio}h{phut}p{giay}s")
else:
    print("Thời gian không hợp lệ.")
