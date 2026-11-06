import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

import csdl_sinhvien as db

class UngDungQuanLySinhVien(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quan ly Sinh vien")
        self.geometry("600x500")
        self.resizable(False, False)

        db.tao_bang_neu_chua_co()

        self.khoi_tao_giao_dien()
        self.tai_lai_danh_sach()

    def khoi_tao_giao_dien(self):
        khung_nhap = tk.Frame(self)
        khung_nhap.pack(pady=10, padx=10, fill="x")

        tk.Label(khung_nhap, text="Ma SV:").grid(row=0, column=0, sticky="w", pady=5)
        self.o_nhap_ma_sv = tk.Entry(khung_nhap, width=30)
        self.o_nhap_ma_sv.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Ho ten:").grid(row=1, column=0, sticky="w", pady=5)
        self.o_nhap_ho_ten = tk.Entry(khung_nhap, width=30)
        self.o_nhap_ho_ten.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Lop:").grid(row=2, column=0, sticky="w", pady=5)
        self.o_nhap_lop = tk.Entry(khung_nhap, width=30)
        self.o_nhap_lop.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Diem TB:").grid(row=3, column=0, sticky="w", pady=5)
        self.o_nhap_diem = tk.Entry(khung_nhap, width=30)
        self.o_nhap_diem.grid(row=3, column=1, padx=10, pady=5)

        tk.Button(khung_nhap, text="Them sinh vien", command=self.xu_ly_them).grid(row=4, column=0, columnspan=2, pady=10)

        khung_danh_sach = tk.Frame(self)
        khung_danh_sach.pack(pady=5, padx=10, fill="both", expand=True)

        self.listbox_sv = tk.Listbox(khung_danh_sach, width=80, height=12)
        self.listbox_sv.pack(side="left", fill="both", expand=True)

        thanh_cuon = tk.Scrollbar(khung_danh_sach, orient="vertical", command=self.listbox_sv.yview)
        thanh_cuon.pack(side="right", fill="y")
        self.listbox_sv.config(yscrollcommand=thanh_cuon.set)

        khung_nut = tk.Frame(self)
        khung_nut.pack(pady=10)

        tk.Button(khung_nut, text="Xoa sinh vien", command=self.xu_ly_xoa).grid(row=0, column=0, padx=10)
        tk.Button(khung_nut, text="Thong ke theo Lop", command=self.xu_ly_thong_ke).grid(row=0, column=1, padx=10)

    def tai_lai_danh_sach(self):
        self.listbox_sv.delete(0, tk.END)
        self.danh_sach_hien_tai = db.lay_toan_bo_sinh_vien()

        for sv in self.danh_sach_hien_tai:
            id_sv, ma_sv, ho_ten, lop, diem_tb = sv
            self.listbox_sv.insert(tk.END, f"[{ma_sv}] {ho_ten} - Lop: {lop} - Diem TB: {diem_tb}")

    def xu_ly_them(self):
        ma_sv = self.o_nhap_ma_sv.get().strip()
        ho_ten = self.o_nhap_ho_ten.get().strip()
        lop = self.o_nhap_lop.get().strip()
        diem_str = self.o_nhap_diem.get().strip()

        if not ma_sv or not ho_ten or not lop or not diem_str:
            messagebox.showerror("Loi", "Vui long nhap day du thong tin.")
            return

        try:
            diem_tb = float(diem_str)
        except ValueError:
            messagebox.showerror("Loi", "Diem trung binh phai la so.")
            return

        try:
            db.them_sinh_vien(ma_sv, ho_ten, lop, diem_tb)
            self.o_nhap_ma_sv.delete(0, tk.END)
            self.o_nhap_ho_ten.delete(0, tk.END)
            self.o_nhap_lop.delete(0, tk.END)
            self.o_nhap_diem.delete(0, tk.END)
            self.tai_lai_danh_sach()
            messagebox.showinfo("Thanh cong", f"Da them SV: {ho_ten}")
        except Exception as e:
            messagebox.showerror("Loi", "Ma sinh vien da ton tai hoac co loi CSDL.")

    def xu_ly_xoa(self):
        lua_chon = self.listbox_sv.curselection()
        if not lua_chon:
            messagebox.showerror("Loi", "Vui long chon 1 sinh vien de xoa.")
            return
        id_sv = self.danh_sach_hien_tai[lua_chon[0]][0]
        db.xoa_sinh_vien(id_sv)
        self.tai_lai_danh_sach()

    def xu_ly_thong_ke(self):
        du_lieu = db.thong_ke_theo_lop()
        if not du_lieu:
            messagebox.showinfo("Thong bao", "Chua co du lieu sinh vien.")
            return

        cac_lop = [dong[0] for dong in du_lieu]
        so_luong = [dong[1] for dong in du_lieu]

        plt.figure(figsize=(6, 4))
        plt.bar(cac_lop, so_luong, color="mediumseagreen")
        plt.title("So luong sinh vien theo Lop")
        plt.xlabel("Lop")
        plt.ylabel("So luong")
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    app = UngDungQuanLySinhVien()
    app.mainloop()