# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:33:51 2024

@author: ADMIN
"""

time_input = input("Nhập vào giờ, phút và giây theo định dạng hh:mm:ss: ")
hh, mm, ss = map(int, time_input.split(':'))
tonggiay = hh * 3600 + mm * 60 + ss
print("Tổng số giây:", tonggiay )
