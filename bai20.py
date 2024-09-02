# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 10:14:41 2024

@author: ADMIN
"""

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))

ln=0.0
if a>=b and a>=c:
    ln=a
elif b>=a and b>=c:
    ln=b
else:
    ln=c
print(f"giá trị lớn nhẩt là: {ln}")

