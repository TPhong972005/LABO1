# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 22:04:36 2024

@author: ADMIN
"""

a=str(input("nhap 1 ki tu di:"))
if len(a)>1 or not a.isalpha():
    print("nhap mot ki tu khac so ma")
else:
    print(a.upper())