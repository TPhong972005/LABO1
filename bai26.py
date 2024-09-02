# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 10:45:20 2024

@author: ADMIN
"""

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
d= 0
if a > b:
    d = a
    a = b
    b = d
if a > c:
    d = a
    a = c
    c = d
if b > c:
    d = b
    b = c
    c = d
print("Thứ tự tăng dần là:", a, b, c) 