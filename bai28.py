# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 18:12:15 2024

@author: ADMIN
"""

N = int(input("Nhập vào số nguyên dương N: "))
if N > 0:
   print("Giá trị được chấp nhận")
elif not N.isdigit:
    print("Dữ liệu nhập vào không phải là số nguyên. Vui lòng thử lại.")
else:
    print("Số nhập vào phải là số nguyên dương. Vui lòng thử lại.")

print(f"Các ước số của {N} là:")
for i in range(1, N + 1):
    if N % i == 0:
            print(i, end=" ")
    
    