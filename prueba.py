# -*- coding: utf-8 -*-
"""
Created on Mon May  9 07:52:01 2022

@author: s_bio
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import fft, signal
import scipy
from scipy.io.wavfile import read
from scipy.fft import fft, fftfreq

# Configuración de las gráficas
plt.rcParams['figure.figsize'] = [8, 6]
plt.rcParams['figure.dpi'] = 140

# Leer los archivos .WAV
# Fs es la frecuencia de muestreo del archivo
Fs, song = read("data/ricktroya.wav")
# Analizar uno solo de los canales
song2 = song[:,0]

#%%
# Revisar un pedazo de la señal en el tiempo
# Vector que va de la Fs hasta Fs * 1.3 del tipo entero
time_to_plot = np.arange(Fs * 1, Fs * 1.3, dtype=int)

# Analizamos la canción en frecuencia
N = len(song2)
fftsong = fft(song2)
transform_y = 2.0 / N * np.abs(fftsong[0:N//2])
transform_x = fftfreq(N, 1 / Fs)[:N//2]

plt.subplot(2, 1, 1)
plt.plot(time_to_plot, song2[time_to_plot])
plt.title("Señal sonido en el tiempo")
plt.xlabel("Índice de Tiempo")
plt.ylabel("Magnitud")
plt.subplot(2, 1, 2)
plt.plot(transform_x, transform_y)
plt.xlabel("Frecuencia (Hz)")
plt.xlim(0,2000)
plt.grid()
plt.show()

#%%
# TODO: Analizar como se encuentran los picos
all_peaks, props = signal.find_peaks(transform_y)
peaks, props = signal.find_peaks(transform_y, prominence=0, distance=10000)
n_peaks = 15

# Obtener los picos más grandes (n_peaks) de las prominencias
# Este es un argpartition
# https://kanoki.org/2020/01/14/find-k-smallest-and-largest-values-and-its-indices-in-a-numpy-array/
largest_peaks_indices = np.argpartition(props["prominences"], -n_peaks)[-n_peaks:]
largest_peaks = peaks[largest_peaks_indices]

plt.plot(transform_x, transform_y, label="Espectro")
plt.scatter(transform_x[largest_peaks], transform_y[largest_peaks], color="r", zorder=10, label="Constrained Peaks")
plt.xlim(0, 3000)
plt.show()

#%%
# Some parameters
window_length_seconds = 3
window_length_samples = int(window_length_seconds * Fs)
window_length_samples += window_length_samples % 2

# Perform a short time fourier transform
# frequencies and times are references for plotting/analysis later
# the stft is a NxM matrix
frequencies, times, stft = signal.stft(
    song2, Fs, nperseg=window_length_samples,
    nfft=window_length_samples, return_onesided=True
)

stft.shape

#%%
constellation_map = []

for time_idx, window in enumerate(stft.T):
    # Spectrum is by default complex. 
    # We want real values only
    spectrum = abs(window)
    # Find peaks - these correspond to interesting features
    # Note the distance - want an even spread across the spectrum
    peaks, props = signal.find_peaks(spectrum, prominence=0, distance=200)

    # Only want the most prominent peaks
    # With a maximum of 5 per time slice
    n_peaks = 5
    # Get the n_peaks largest peaks from the prominences
    # This is an argpartition
    # Useful explanation: https://kanoki.org/2020/01/14/find-k-smallest-and-largest-values-and-its-indices-in-a-numpy-array/
    largest_peaks = np.argpartition(props["prominences"], -n_peaks)[-n_peaks:]
    for peak in peaks[largest_peaks]:
        frequency = frequencies[peak]
        constellation_map.append([time_idx, frequency])

# Transform [(x, y), ...] into ([x1, x2...], [y1, y2...]) for plotting using zip
plt.scatter(*zip(*constellation_map));

#%%
'''
# Número de puntos
N = 600
# Muestreo a 1/800 s
T = 1.0 / 800.0
# La señal se muestrea de 0 a 0.75 s
x = np.linspace(0.0, N*T, N, endpoint=False)

# Crear una señal de 5 Hz y 10 Hz
# f(t) = A*sin(w*t)         donde w = 2pi*f  
# y = sin(5 * 2pi * x) + 0.75*sin(10 * 2pi * x)
y = np.sin(5.0 * 2.0*np.pi*x) + 0.75*np.sin(10.0 * 2.0*np.pi*x)
# Obtener la transformada rápida de Fourier de la señal
yf = fft(y)
# Obtener las frecuencias de análisis de la FFT
# tomando la parte positiva de las frecuencias
xf = fftfreq(N, T)[:N//2]

# Corromper la señal
y_c = y + np.random.normal(0, 10.0, len(y))
yf_c = fft(y_c)
xf_c = fftfreq(N, T)[:N//2]

# Graficar
plt.subplot(2, 1, 1)
plt.plot(x, y)
plt.xlabel("Tiempo (s)")
plt.subplot(2, 1, 2)
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.grid()
plt.xlabel("Frecuencia (Hz)")
plt.xlim(0, 60)
plt.show()

plt.subplot(2, 1, 1)
plt.plot(x, y_c)
plt.xlabel("Tiempo (s)")
plt.subplot(2, 1, 2)
plt.plot(xf_c, 2.0/N * np.abs(yf_c[0:N//2]))
plt.grid()
plt.xlabel("Frecuencia (Hz)")
plt.xlim(0, 60)
plt.show()
'''


