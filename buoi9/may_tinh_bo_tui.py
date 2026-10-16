import tkinter as tk

def btn_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except Exception as e:
        input_text.set("Lỗi")
        expression = ""

root = tk.Tk()
root.title("Máy Tính Bỏ Túi")
root.geometry("320x420")
root.resizable(False, False)

expression = ""
input_text = tk.StringVar()

# Khung chứa màn hình hiển thị (Entry)
input_frame = tk.Frame(root, width=320, height=70, bd=0)
input_frame.pack(side=tk.TOP, fill=tk.BOTH)

input_field = tk.Entry(input_frame, textvariable=input_text, font=('arial', 20, 'bold'), width=18, bg="#eee", bd=0, justify=tk.RIGHT)
input_field.pack(ipady=15, fill=tk.BOTH, expand=True)

# Khung chứa các nút bấm
btns_frame = tk.Frame(root, bg="grey")
btns_frame.pack(fill=tk.BOTH, expand=True)

# Cấu hình để các cột tự động giãn đều bằng nhau (tránh lệch nút C)
for i in range(4):
    btns_frame.columnconfigure(i, weight=1, uniform="col")
for i in range(5):
    btns_frame.rowconfigure(i, weight=1, uniform="row")

# Hàng 0: Nút C (chiếm 2 cột đầu), Chia (*), Nhân (/)
btn_clear_widget = tk.Button(btns_frame, text="C", fg="black", bg="#eee", bd=1, cursor="hand2", command=lambda: btn_clear())
btn_clear_widget.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=1, pady=1)

btn_div = tk.Button(btns_frame, text="/", fg="black", bg="#eee", bd=1, cursor="hand2", command=lambda: btn_click("/"))
btn_div.grid(row=0, column=2, sticky="nsew", padx=1, pady=1)

btn_mul = tk.Button(btns_frame, text="*", fg="black", bg="#eee", bd=1, cursor="hand2", command=lambda: btn_click("*"))
btn_mul.grid(row=0, column=3, sticky="nsew", padx=1, pady=1)

# Hàng 1: 7, 8, 9, -
tk.Button(btns_frame, text="7", fg="black", bg="#fff", bd=1, cursor="hand2", command=lambda: btn_click(7)).grid(row=1, column=0, sticky="nsew", padx=1, pady=1)
tk.Button(btns_frame, text="8", fg="black", bg="#fff", bd=1, cursor="hand2", command=lambda: btn_click(8)).grid(row=1, column=1, sticky="nsew", padx=1, pady=1)
tk.Button(btns_frame, text="9", fg="black", bg="#fff", bd=1, cursor="hand2", command=lambda: btn_click(9)).grid(row=1, column=2, sticky="nsew", padx=1, pady=1)
tk.Button(btns_frame, text="-", fg="black", bg="#eee", bd=1, cursor="hand2", command=lambda: btn_click("-")).grid(row=1, column=3, sticky="nsew", padx=1, pady=1)

# Hàng 2: 4, 5, 6, +
tk.Button(btns_frame, text="4", fg="black", bg="#fff", bd=1, cursor="hand2", command=lambda: btn_click(4)).grid(row=2, column=0, sticky="nsew", padx=1, pady=1)
tk.Button(btns_frame, text="5", fg="black", bg="#fff", bd=1, cursor="hand2", command=lambda: btn_click(5)).grid(row=2, column=1, sticky="nsew", padx=1, pady=1)
tk.Button(btns_frame, text="6", fg="black", bg="#fff", bd=1, cursor="hand2", command=lambda: btn_click(6)).grid(row=2, column=2, sticky="nsew", padx=1, pady=1)
tk.Button(btns_frame, text="+", fg="black", bg="#eee", bd=1, cursor="hand2", command=lambda: btn_click("+")).grid(row=2, column=3, sticky="nsew", padx=1, pady=1)

# Hàng 3: 1, 2, 3 và Dấu bằng (= chiếm 2 hàng)
tk.Button(btns_frame, text="1", fg="black", bg="#fff", bd=1, cursor="hand2", command=lambda: btn_click(1)).grid(row=3, column=0, sticky="nsew", padx=1, pady=1)
tk.Button(btns_frame, text="2", fg="black", bg="#fff", bd=1, cursor="hand2", command=lambda: btn_click(2)).grid(row=3, column=1, sticky="nsew", padx=1, pady=1)
tk.Button(btns_frame, text="3", fg="black", bg="#fff", bd=1, cursor="hand2", command=lambda: btn_click(3)).grid(row=3, column=2, sticky="nsew", padx=1, pady=1)

btn_equal_widget = tk.Button(btns_frame, text="=", fg="black", bg="#eee", bd=1, cursor="hand2", command=lambda: btn_equal())
btn_equal_widget.grid(row=3, column=3, rowspan=2, sticky="nsew", padx=1, pady=1)

# Hàng 4: Số 0 (chiếm 2 cột), Dấu chấm (.)
tk.Button(btns_frame, text="0", fg="black", bg="#fff", bd=1, cursor="hand2", command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, sticky="nsew", padx=1, pady=1)
tk.Button(btns_frame, text=".", fg="black", bg="#fff", bd=1, cursor="hand2", command=lambda: btn_click(".")).grid(row=4, column=2, sticky="nsew", padx=1, pady=1)

root.mainloop()