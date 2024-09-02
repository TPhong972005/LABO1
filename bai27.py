# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 18:09:12 2024

@author: ADMIN
"""

import math

hinh = input("Nhập hình (v cho hình vuông, n cho hình chữ nhật, t cho hình tròn): ").lower()
if hinh == 'v':
        canh = float(input("Nhập chiều dài cạnh hình vuông: "))
        chu_vi = 4 * canh
        dien_tich = canh * canh
        print(f"Kết quả: P = {chu_vi} S = {dien_tich}")
elif hinh == 'n':
        chieu_rong = float(input("Nhập chiều rộng = "))
        chieu_dai = float(input("Nhập chiều dài = "))
        chu_vi = 2 * (chieu_rong + chieu_dai)
        dien_tich = chieu_rong * chieu_dai
        print(f"Kết quả: P = {chu_vi} S = {dien_tich}")

elif hinh == 't':
        ban_kinh = float(input("Nhập bán kính hình tròn: "))
        chu_vi = 2 * math.pi * ban_kinh
        dien_tich = math.pi * ban_kinh ** 2
        print(f"Kết quả: P = {chu_vi:.2f} S = {dien_tich:.2f}")
else:
        print("Hình không hợp lệ!")

