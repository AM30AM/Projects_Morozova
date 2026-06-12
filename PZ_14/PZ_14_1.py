#'''  https://i.stack.imgur.com/5MatP.png'''

import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title('Registration')
root.geometry('820x520')
BG = "#2f5f90"
FRAME_BG = '#2f5f90'
root.configure(bg=BG)


wrap = tk.Frame(root, bg=BG)
wrap.place(relx=0.5, rely=0.48, anchor="c", width=800, height=420)

frame = tk.Frame(wrap, bg=BG, bd=3, relief="flat", highlightbackground="white", highlightthickness=3)
frame.place(relx=0.5, rely=0.5, anchor="c", width=720, height=320)

tk.Label(frame, text="Registration Details", bg=BG, fg="white", font=("Helvetica", 12, "bold")).place(x=12, y=8)

content = tk.Frame(frame, bg=BG)
content.place(x=20, y=40, width=650, height=400)
content.grid_columnconfigure(0, minsize=140)
content.grid_columnconfigure(1, weight=1)

def make_label(r, text):
    lbl = tk.Label(content, text=text, bg=BG, fg="white", anchor="e", font=("Helvetica", 10))
    lbl.grid(row=r, column=0, sticky="e", padx=(0,8), pady=6)

def make_entry(r, placeholder=""):
    e = tk.Entry(content, width=40)
    e.grid(row=r, column=1, sticky="w", pady=6)
    if placeholder:
        e.insert(0, placeholder)
    return e

make_label(0, "University :")
entry_uni = make_entry(0, "Enter university")

make_label(1, "Institute :")
entry_inst = make_entry(1, "Enter institute")

make_label(2, "Branch :")
cmb_branch = ttk.Combobox(content, values=["-- select --", "CS", "EE", "ME"], width=30, state="readonly")
cmb_branch.current(0)
cmb_branch.grid(row=2, column=1, sticky="w", pady=6)

make_label(3, "Degree :")
deg_frame = tk.Frame(content, bg=BG)
deg_frame.grid(row=3, column=1, sticky="w", pady=6)
cmb_deg = ttk.Combobox(deg_frame, values=["-- select --", "B.Sc", "M.Sc", "PhD"], width=15, state="readonly")
cmb_deg.current(0)
cmb_deg.pack(side="left", padx=(0,8))
deg_var = tk.StringVar(value="Pursuing")
rb1 = tk.Radiobutton(deg_frame, text="Pursuing", variable=deg_var, value="Pursuing", bg=BG, fg="white", selectcolor=BG, activebackground=BG)
rb2 = tk.Radiobutton(deg_frame, text="Completed", variable=deg_var, value="Completed", bg=BG, fg="white", selectcolor=BG, activebackground=BG)
rb1.pack(side="left", padx=6); rb2.pack(side="left", padx=6)

make_label(4, "Avarage CPI :")
cpi_frame = tk.Frame(content, bg=BG)
cpi_frame.grid(row=4, column=1, sticky="w", pady=6)
spin_cpi = tk.Spinbox(cpi_frame, from_=0.0, to=10.0, increment=0.1, width=6)
spin_cpi.pack(side="left")
tk.Label(cpi_frame, text=" Upto ", bg=BG, fg="white").pack(side="left", padx=6)
spin_sem = tk.Spinbox(cpi_frame, from_=1, to=10, width=4)
spin_sem.pack(side="left")
tk.Label(cpi_frame, text=" Th Semester", bg=BG, fg="white").pack(side="left", padx=6)

make_label(5, "Experience :")
exp_frame = tk.Frame(content, bg=BG)
exp_frame.grid(row=5, column=1, sticky="w", pady=6)
spin_exp = tk.Spinbox(exp_frame, from_=0, to=50, width=6)
spin_exp.pack(side="left")
tk.Label(exp_frame, text=" Years", bg=BG, fg="white").pack(side="left", padx=6)

make_label(6, "Your Website Or Blog :")
entry_site = make_entry(6, "http://")

btn_frame = tk.Frame(root, bg=BG)
btn_frame.place(relx=0.5, rely=0.92, anchor="c")

def on_next():
    if not entry_uni.get().strip() or not entry_inst.get().strip():
        messagebox.showwarning("Fill fields", "Please fill University and Institute")
        return
    messagebox.showinfo("Next", "Proceed to Step 2 (mock)")

left_arrow = tk.Button(btn_frame, text="◀", bg="#7fcf6b", fg="white", width=3, relief="flat", command=lambda: None)
step_lbl = tk.Label(btn_frame, text="  Step 2  ", bg=BG, fg="white", font=("Helvetica", 10, "bold"))
right_arrow = tk.Button(btn_frame, text="▶", bg="#7fcf6b", fg="white", width=3, relief="flat", command=on_next)

left_arrow.pack(side="left", padx=6)
step_lbl.pack(side="left")
right_arrow.pack(side="left", padx=6)

root.mainloop()