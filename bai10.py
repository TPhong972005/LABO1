# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:22:58 2024

@author: ADMIN
"""

biensoxe_input=input("nhap bien so xe cua ban:")
if len(biensoxe_input) != 4 or not biensoxe_input.isdigit():
    print("Vui lòng nhập chính xác 4 chữ số!")
else:
    tong = sum(int(digit) for digit in biensoxe_input)
    sonut=tong%10
    print("so nut cua ban la", sonut)


