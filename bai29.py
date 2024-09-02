# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 18:27:46 2024

@author: ADMIN
"""

chuoi_so=input("nhập chuỗi số của bạn:")
if not chuoi_so.isdigit():
    print("Không hợp lệ nhập chuỗi số thôi!")
else:
    tong=sum(int(digit) for digit in chuoi_so)
    print(f"tổng các phần tử trong chuỗi số của bạn là {tong}")
    
    
    