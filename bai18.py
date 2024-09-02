# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 23:41:45 2024

@author: ADMIN
"""

def giothanhgiay(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds
def giaythanhgio(tong_seconds):
    hours = tong_seconds // 3600
    tong_seconds %= 3600
    minutes = tong_seconds // 60
    seconds = tong_seconds % 60
    return hours, minutes, seconds
print("nhập giờ thứ nhất")
hours1 = int(input("Nhập giờ của thời gian thứ nhất: "))
minutes1 = int(input("Nhập phút của thời gian thứ nhất: "))
seconds1 = int(input("Nhập giây của thời gian thứ nhất: "))
print("nhập giờ thứ hai")
hours2 = int(input("Nhập giờ của thời gian thứ hai: "))
minutes2 = int(input("Nhập phút của thời gian thứ hai: "))
seconds2 = int(input("Nhập giây của thời gian thứ hai: "))
tong_seconds1 = giothanhgiay(hours1, minutes1, seconds1)
tong_seconds2 = giothanhgiay(hours2, minutes2, seconds2)
#tinhtonggiay
sum_seconds = tong_seconds1 + tong_seconds2
sum_hours, sum_minutes, sum_seconds = giaythanhgio(sum_seconds)
#tinhhieugiay
diff_seconds=abs(tong_seconds1 - tong_seconds2)
diff_hours, diff_minutes, diff_seconds= giaythanhgio(diff_seconds)
#ketqua
print(f"cong hai thoi gian: {sum_hours}h{sum_minutes}p{sum_seconds}s")
print(f"tru hai thoi gian: {diff_hours}h{diff_minutes}p{diff_seconds}s")

