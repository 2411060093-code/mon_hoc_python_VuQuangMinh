so = 29
la_so_nguyen_to = True
if so < 2:
    la_so_nguyen_to = False
else:
    for i in range(2, so):

     if so % i == 0:
        la_so_nguyen_to = False
        break # thoat ngay khi tim thay uoc so, khong can kiem tra tiep
print(f"{so} co phai so nguyen to khong? {la_so_nguyen_to}")