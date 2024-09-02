# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 07:41:00 2024

@author: ADMIN
"""
import math

a=float(input("nhap so co 2 chu so"))
if a<10 or a>=100:
    print("nhap lai di hihi")
else:
   b= a//10
   c= a%10
   print("tong hai chu so",b+c)
    
    