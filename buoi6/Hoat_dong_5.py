print("Bai5.1:\n")
danh_sach_so = [1, 2, 3, 4, 5]
binh_phuong = list(map(lambda x: x ** 2, danh_sach_so))
print(binh_phuong)

print("\nBai5.2:\n")
so_chan = list(filter(lambda x: x % 2 == 0, danh_sach_so))
print(so_chan)

print("\nBai5.3:\n")
danh_sach_sv = [
    {"ten": "An", "diem": 8.5},

    {"ten": "Binh", "diem": 7.0},
    {"ten": "Chi", "diem": 9.2},
]
sap_xep_theo_diem = sorted(danh_sach_sv, key=lambda sv: sv["diem"])
sap_xep_giam_dan = sorted(danh_sach_sv, key=lambda sv: sv["diem"], reverse=True)
for sv in sap_xep_theo_diem:
    print(sv["ten"], "-", sv["diem"])
print("--- Giam dan ---")
for sv in sap_xep_giam_dan:
    print(sv["ten"], "-", sv["diem"])