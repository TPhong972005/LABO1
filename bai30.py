# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 18:16:56 2024

@author: ADMIN
"""
def nhap_thang_nam():
  thang = int(input("Nhập tháng (1-12): "))
  nam = int(input("Nhập năm: "))
  if 1 <= thang <= 12 and nam > 0:
    return thang, nam
  else:
    print("Tháng phải nằm trong khoảng 1-12 và năm phải là số dương. Vui lòng nhập lại.")
def kiem_tra_nam_nhuan(nam):
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        return True
    return False
def so_ngay_trong_thang(thang, nam):
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thang in [4, 6, 9, 11]:
        return 30
    elif thang == 2:
        if kiem_tra_nam_nhuan(nam):
            return 29
        else:
            return 28
    else:
        return None
thang, nam = nhap_thang_nam()
ngay = so_ngay_trong_thang(thang, nam)
print(f" tháng {thang} năm {nam} có {ngay} ngày")


                