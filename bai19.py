# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 10:10:59 2024

@author: ADMIN
"""

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))
d = int(input("Nhập số nguyên d: "))

nn=a
if b<nn:
    nn=b
elif c<nn:
    nn=c
elif d<nn:
    nn=d
print(f"gia tri nho nhat la {nn}")
    