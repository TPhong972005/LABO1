# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 10:36:32 2024

@author: ADMIN
"""

var = input("Nhập một chữ cái: ")
if var.islower():
    print(var.upper())
elif var.isupper():
    print(var.lower())
else:
    print("Đây không phải là một chữ cái hợp lệ.")