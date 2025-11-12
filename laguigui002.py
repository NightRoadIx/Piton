import tkinter as tk
from tkinter import ttk, messagebox

FACT = 2.20462262185  # kg -> lb

root = tk.Tk()
root.title("Conversor Kg/Lb")
root.geometry("360x200")

v_kg = tk.StringVar()
v_lb = tk.StringVar()

frm = ttk.Frame(root, padding=12)
frm.grid(sticky="nsew")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frm.columnconfigure(1, weight=1)

ttk.Label(frm, text="Kilogramos (kg):").grid(row=0, column=0, sticky="w")
e_kg = ttk.Entry(frm, textvariable=v_kg)
e_kg.grid(row=0, column=1, sticky="ew", pady=4)

ttk.Label(frm, text="Libras (lb):").grid(row=1, column=0, sticky="w")
e_lb = ttk.Entry(frm, textvariable=v_lb)
e_lb.grid(row=1, column=1, sticky="ew", pady=4)

def to_lb():
    try:
        kg = float(v_kg.get())
        v_lb.set(f"{kg*FACT:.4f}")
    except ValueError:
        messagebox.showerror("Dato inválido", "Ingresa un número en kg.")

def to_kg():
    try:
        lb = float(v_lb.get())
        v_kg.set(f"{lb/FACT:.4f}")
    except ValueError:
        messagebox.showerror("Dato inválido", "Ingresa un número en lb.")

btns = ttk.Frame(frm)
btns.grid(row=2, column=0, columnspan=2, pady=8)
ttk.Button(btns, text="Kg → Lb", command=to_lb).pack(side="left", padx=4)
ttk.Button(btns, text="Lb → Kg", command=to_kg).pack(side="left", padx=4)
ttk.Button(btns, text="Limpiar", command=lambda: (v_kg.set(""), v_lb.set(""))).pack(side="left", padx=4)

e_kg.focus()
root.mainloop()
