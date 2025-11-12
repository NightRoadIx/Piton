import tkinter as tk
from tkinter import ttk
import time

root = tk.Tk()
root.title("Trabajo simulado con after")
root.geometry("360x140")

pb = ttk.Progressbar(root, mode="determinate", maximum=100)
pb.pack(fill="x", padx=12, pady=12)

lbl = ttk.Label(root, text="Listo.")
lbl.pack(padx=12)

def tarea_larga(p=0):
    if p == 0:
        lbl.config(text="Procesando…")
    if p <= 100:
        pb['value'] = p
        # Simula trabajo (no usar time.sleep en el hilo UI)
        root.after(120, lambda: tarea_larga(p+2))
    else:
        lbl.config(text="Completado")

ttk.Button(root, text="Iniciar", command=lambda: tarea_larga(0)).pack(pady=8)
root.mainloop()
