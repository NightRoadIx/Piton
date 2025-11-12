import tkinter as tk
from tkinter import ttk

# Constructor de la ventana de la GUI
root = tk.Tk()
root.title("Lavasola")
root.geometry("560x360")

# -------------------

# Variables reactivas
nombre = tk.StringVar(value="Héctor")
clics = tk.IntVar(value=0)

# Layout base
frm = ttk.Frame(root, padding=12)
frm.grid(sticky="nsew")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(frm, text="Tu nombre:").grid(column=0, row=0, sticky="w")
entrada = ttk.Entry(frm, textvariable=nombre, width=20)
entrada.grid(column=1, row=0, sticky="ew")
frm.columnconfigure(1, weight=1)

saludo = ttk.Label(frm, text="¡Hola, 21!", font=("Segoe UI", 18))
saludo.grid(column=0, row=1, columnspan=2, pady=8)

def saludar():
    saludo.config(text=f"¡Hola, {nombre.get()}!")
    clics.set(clics.get() + 1)

ttk.Button(frm, text="Saludar...sela", command=saludar).grid(column=0, row=2, pady=6, sticky="w")
ttk.Label(frm, textvariable=clics, font=("Segoe UI", 18)).grid(column=1, row=2, sticky="e")

# Atajos/Enfoque
entrada.focus()
root.bind("<Return>", lambda e: saludar())

# -------------------

# Ciclo sin fin
root.mainloop()
