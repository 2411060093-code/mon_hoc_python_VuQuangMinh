import math
diem_a = (2, 3)
diem_b = (7, 8)
xa, ya = diem_a
xb, yb = diem_b

khoang_cach = math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
print(f"Khoang cach giua {diem_a} va {diem_b} la: {round(khoang_cach, 2)}")

cac_diem = [(0, 0), (3, 4), (6, 8)]
goc_toa_do = (0, 0)
xg, yg = goc_toa_do

for diem in cac_diem:
    xd, yd = diem
    kc = math.sqrt((xd - xg) ** 2 + (yd - yg) ** 2)
    print(f"Khoang cach tu {diem} den goc toa do la: {round(kc, 2)}")