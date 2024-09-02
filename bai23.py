# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:32:51 2024

@author: ADMIN
"""
import math

print("giai phuong trinh bac 2,ax^2+bx+c=0")
a=float(input("nhap a:"))
b=float(input("nhap b:"))
c=float(input("nhap c:"))
denta=float()
x1=float()
x2=float()
x=float()
if a==0:
    print("khong duoc dau nhap lai a")
if a>0 or a<0:
    denta=b**2-4*a*c
    if denta>0:
        x1=(-(b)+math.sqrt(denta))/(2*a)
        x2=(-(b)-math.sqrt(denta))/(2*a)
        print("x1=",x1) 
        print("x2=",x2)
    elif denta==0:
        x=-(b)/2*a
        print("x=",x)
    elif denta<0:
        print("phuong trinh vo nghiem")
else:
    print("khong xac dinh")
    
    
    
    
