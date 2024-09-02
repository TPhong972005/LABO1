# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 08:19:56 2024

@author: ADMIN
"""
a=str
print("============ MENU ============")
print("   1. Hu tieu")
print("   2. Chao long")
print("   3. Banh canh")
print("   4. Bun rieu")
print("   5. Pho bo")
print("==============================")
a=int(input("nhap lua chon"))
if a==1:
    print("Mons ban chon la hu tieu")
elif a==2:
    print("Mons ban chon la chao long")
elif a==3:
    print("Mons ban chon la banh canh")
elif a==4:
    print("Mons ban chon la bun rieu")
elif a==5:
    print("Mons ban chon la pho bo")
elif a>5 or a<1:
    print("an gi vay????")
print("==============================")
