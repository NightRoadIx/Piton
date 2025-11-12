import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json, os

root = tk.Tk()
root.title("Lista de cosas que hacer")
root.geometry("460x300")

tareas = []

# --- Menú ---
menubar = tk.Menu(root)
root.config(menu=menubar)
archivo_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="Archivo", menu=archivo_menu)

frm = ttk.Frame(root, padding=10)
frm.pack(fill="both", expand=True)

# Entrada + botones
v_tarea = tk.StringVar()
top = ttk.Frame(frm)
top.pack(fill="x")
ttk.Entry(top, textvariable=v_tarea).pack(side="left", fill="x", expand=True)
ttk.Button(top, text="Añadir", command=lambda: add()).pack(side="left", padx=6)

# Listbox con scroll
mid = ttk.Frame(frm)
mid.pack(fill="both", expand=True, pady=8)
lb = tk.Listbox(mid, height=10, activestyle="dotbox")
sb = ttk.Scrollbar(mid, orient="vertical", command=lb.yview)
lb.config(yscrollcommand=sb.set)
lb.pack(side="left", fill="both", expand=True)
sb.pack(side="right", fill="y")

# Botonera
bot = ttk.Frame(frm)
bot.pack(fill="x")
ttk.Button(bot, text="Editar", command=lambda: edit()).pack(side="left")
ttk.Button(bot, text="Eliminar", command=lambda: remove()).pack(side="left", padx=6)
ttk.Button(bot, text="Limpiar lista", command=lambda: clear()).pack(side="left")

def refresh():
    lb.delete(0, "end")
    for t in tareas:
        lb.insert("end", t)

def add():
    t = v_tarea.get().strip()
    if t:
        tareas.append(t)
        v_tarea.set("")
        refresh()

def edit():
    idx = lb.curselection()
    if not idx:
        messagebox.showinfo("Editar", "Selecciona una tarea.")
        return
    i = idx[0]
    nuevo = simple_prompt("Editar tarea", tareas[i])
    if nuevo is not None and nuevo.strip():
        tareas[i] = nuevo.strip()
        refresh()

def remove():
    idx = lb.curselection()
    if not idx:
        return
    i = idx[0]
    if messagebox.askyesno("Eliminar", f"¿Eliminar '{tareas[i]}'?"):
        tareas.pop(i)
        refresh()

def clear():
    if tareas and messagebox.askyesno("Limpiar", "¿Vaciar la lista?"):
        tareas.clear()
        refresh()

# Diálogo simple (sin nueva ventana compleja)
def simple_prompt(title, initial=""):
    top = tk.Toplevel(root)
    top.title(title)
    top.transient(root)
    v = tk.StringVar(value=initial)
    ttk.Label(top, text=title).pack(padx=12, pady=6)
    e = ttk.Entry(top, textvariable=v, width=40)
    e.pack(padx=12, pady=6)
    ok = {"value": None}
    def aceptar():
        ok["value"] = v.get()
        top.destroy()
    ttk.Button(top, text="Aceptar", command=aceptar).pack(pady=8)
    e.focus()
    top.grab_set()
    root.wait_window(top)
    return ok["value"]

# Persistencia
def guardar():
    if not tareas:
        messagebox.showinfo("Guardar", "No hay tareas para guardar.")
        return
    path = filedialog.asksaveasfilename(defaultextension=".json",
                                        filetypes=[("JSON","*.json")])
    if path:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(tareas, f, ensure_ascii=False, indent=2)

def abrir():
    path = filedialog.askopenfilename(filetypes=[("JSON","*.json")])
    if path and os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, list) and all(isinstance(x, str) for x in data):
                tareas.clear()
                tareas.extend(data)
                refresh()
            else:
                messagebox.showerror("Error", "Archivo JSON inválido.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

archivo_menu.add_command(label="Abrir…", command=abrir)
archivo_menu.add_command(label="Guardar como…", command=guardar)
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=root.destroy)

root.mainloop()
