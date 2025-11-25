import tkinter as tk
from tkinter import messagebox
import serial
import time
import csv
import os

import pandas as pd
import plotly.express as px

PUERTO = "COM6"    # CAMBIAR según tu PC
BAUDIOS = 9600
ARCHIVO_CSV = "datos_sensor.csv"

class AppArduino:
    def __init__(self, root):
        self.root = root
        self.root.title("Adquisición de datos desde Arduino")
        self.root.geometry("400x250")

        # Estado de adquisición
        self.acquiriendo = False
        self.ser = None
        self.csv_file = None
        self.csv_writer = None
        self.inicio_tiempo = None

        # Widgets
        self.lbl_estado = tk.Label(root, text="Estado: Sin conexión", font=("Arial", 12))
        self.lbl_estado.pack(pady=5)

        self.lbl_valor = tk.Label(root, text="Temperatura: -", font=("Arial", 16))
        self.lbl_valor.pack(pady=5)

        self.btn_iniciar = tk.Button(root, text="Iniciar adquisición", command=self.iniciar_adquisicion)
        self.btn_iniciar.pack(pady=5)

        self.btn_detener = tk.Button(root, text="Detener", command=self.detener_adquisicion, state=tk.DISABLED)
        self.btn_detener.pack(pady=5)

        self.btn_graficar = tk.Button(root, text="Graficar datos", command=self.graficar_datos)
        self.btn_graficar.pack(pady=10)

        self.lbl_info_archivo = tk.Label(root, text=f"Archivo CSV: {ARCHIVO_CSV}")
        self.lbl_info_archivo.pack(pady=5)

    def iniciar_adquisicion(self):
        # Abrir puerto serial
        try:
            self.ser = serial.Serial(PUERTO, BAUDIOS, timeout=1)
            time.sleep(2)  # Dar tiempo a que Arduino reinicie
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir el puerto {PUERTO}:\n{e}")
            return

        # Abrir archivo CSV y preparar encabezados
        nuevo_archivo = not os.path.exists(ARCHIVO_CSV)
        try:
            self.csv_file = open(ARCHIVO_CSV, mode="a", newline="")
            self.csv_writer = csv.writer(self.csv_file)
            if nuevo_archivo:
                self.csv_writer.writerow(["tiempo_seg", "temperatura"])
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir/crear el archivo CSV:\n{e}")
            self.ser.close()
            self.ser = None
            return

        self.inicio_tiempo = time.time()
        self.acquiriendo = True
        self.lbl_estado.config(text="Estado: Adquiriendo datos...")
        self.btn_iniciar.config(state=tk.DISABLED)
        self.btn_detener.config(state=tk.NORMAL)

        # Comenzar ciclo de lectura
        self.leer_dato()

    def leer_dato(self):
        if not self.acquiriendo:
            return

        try:
            if self.ser.in_waiting > 0:
                linea = self.ser.readline().decode(errors="ignore").strip()
                if linea:
                    try:
                        temperatura = float(linea)  # Convertimos el valor a flotante
                    except ValueError:
                        temperatura = None

                    if temperatura is not None:
                        # Actualizar etiqueta con la temperatura
                        self.lbl_valor.config(text=f"Temperatura: {temperatura}°C")

                        # Calcular tiempo relativo
                        t = time.time() - self.inicio_tiempo

                        # Guardar en CSV
                        self.csv_writer.writerow([t, temperatura])
                        self.csv_file.flush()
        except Exception as e:
            self.lbl_estado.config(text=f"Error de lectura: {e}")
            self.detener_adquisicion()
            return

        # Volver a llamar a esta función después de 100 ms
        self.root.after(100, self.leer_dato)

    def detener_adquisicion(self):
        if self.acquiriendo:
            self.acquiriendo = False
            self.lbl_estado.config(text="Estado: Adquisición detenida")

            if self.ser is not None:
                try:
                    self.ser.close()
                except:
                    pass
                self.ser = None

            if self.csv_file is not None:
                try:
                    self.csv_file.close()
                except:
                    pass
                self.csv_file = None

            self.btn_iniciar.config(state=tk.NORMAL)
            self.btn_detener.config(state=tk.DISABLED)

    def graficar_datos(self):
        if not os.path.exists(ARCHIVO_CSV):
            messagebox.showwarning("Aviso", f"No existe el archivo {ARCHIVO_CSV}")
            return

        try:
            df = pd.read_csv(ARCHIVO_CSV)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo leer el CSV:\n{e}")
            return

        if df.empty:
            messagebox.showinfo("Sin datos", "El archivo CSV está vacío.")
            return

        # Gráfico interactivo con Plotly (mostramos solo la temperatura)
        fig = px.line(df, x="tiempo_seg", y="temperatura",
                      title="Temperatura en función del tiempo",
                      labels={"tiempo_seg": "Tiempo (s)", "temperatura": "Temperatura (°C)"})
        fig.show()  # Se abre en el navegador como gráfica interactiva

def main():
    root = tk.Tk()
    app = AppArduino(root)
    root.mainloop()

if __name__ == "__main__":
    main()
