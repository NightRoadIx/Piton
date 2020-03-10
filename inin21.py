import numpy as np
import matplotlib.pyplot as plt
import wave
import struct
 
#%%
# Se generará una señal senoidal de cierta frecuencia
# DATOS DE LA SEÑAL A GENERAR
# Frecuencia de la onda
frecuencia = 1000
 # Número de muestras
num_samples = 48000 
# La frecuencia de muestreo es la conversión analógica-digital
sampling_rate = 48000.0
# Amplitud de la onda 
amplitud = 16000

# Nombre del archivo a generar
file = "test.wav"

# Generación de la señal
# señal senoidal de frecuencia f debe ser 2*pi*f*t, t es el inverso de la frecuencia de muestreo
# y lo que se obtiene es una señal de 1 segundo exactamente
sine_wave = [np.sin(2 * np.pi * frecuencia * x/sampling_rate) for x in range(num_samples)]

# PARÁMETROS PARA GENERAR EL ARCHIVO DE AUDIO
# Número de muestras
nframes=num_samples
# Tipo de compresión
comptype="NONE"
compname="not compressed"
# Número de canales
nchannels=1
# ancho del muestreo en bytes
sampwidth=2
# Abrir el archivo para su creación y escritura
wav_file=wave.open(file, 'w')
# Colocar los parámetros del archivo de audio WAV
wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))

# Se abre el archivo y se colocan los parámetros
# struct es una librería de Python que empaqueta los datos como binarios
# el parámetro 'h' significa que es a 16 bits
for s in sine_wave:
   wav_file.writeframes(struct.pack('h', int(s*amplitud)))

# Cerrar el archivo, es muy importante
wav_file.close()
#%%
# Ahora se va a leer esta señal
# Esto es la frecuencia de muestreo
frame_rate = 48000.0
# Nombre del archivo a leer
infile = "test.wav"
# Número de muestras a leer (la longitud total de la señal)
num_samples = 48000
# Abrir el archivo para leer
wav_file = wave.open(infile, 'r')
# Obtener los datos totales
data = wav_file.readframes(num_samples) 
# Cerrar el archivo, es muy importante
wav_file.close()

# Ahora se desempaquetarán los datos
data = struct.unpack('{n}h'.format(n=num_samples), data)
# Ahora se volverá un arreglo numpy
data = np.array(data)

# Ahora se obtiene la FFT de los datos recibidos
# Fast-Fourier Transform
data_fft = np.fft.fft(data)
# Esto regresa un arreglo de números complejos que parecen no decir nada
print(data_fft[:8])

# Al utilizar el valor absoluto de los datos, se obtienen valores reales
frecuencias = np.abs(data_fft)
# Lo cual son todas las posibles frecuencias de la señal...
# por ejemplo, data_fft[1] sería el dato de 1Hz
# data_fft[2] datos para 2Hz...

# Se hallan las frecuencias para mostrar
xf = np.linspace(0.0, 1.0/(2.0*(1.0/num_samples)), num_samples/2)

# Obtener la frecuencia con el valor más alto
print("La frecuencia es {} Hz".format(np.argmax(frecuencias)))

# Se realiza la gráfica para observar mejor
plt.subplot(2,1,1)
# graficar solo una parte de la señal
plt.plot(data[:300])
plt.title("Señal de audio")
plt.subplot(2,1,2)
plt.plot(xf, frecuencias[:num_samples//2])
plt.title("Frecuencias")
plt.xlim(0,1200)
plt.show()


#%%
# AHORA SE VA A LIMPIAR LA SEÑAL
# Frecuencia de la señal
frequency = 1000
# Frecuencia de la señal que va a "ensuciar" la señal
noisy_freq = 50
 # Número de muestras
num_samples = 48000
# La frecuencia de muestreo de la señal digital
sampling_rate = 48000.0


# Se generan ambas señales
sine_wave = [np.sin(2 * np.pi * frequency * x1 / sampling_rate) for x1 in range(num_samples)]
sine_noise = [np.sin(2 * np.pi * noisy_freq * x1/  sampling_rate) for x1 in range(num_samples)]
 
# Se convierten las señales en arreglos numpy
sine_wave = np.array(sine_wave)
sine_noise = np.array(sine_noise)

# Ahora se añade la señal ruidosa a la original
combined_signal = sine_wave + sine_noise

# Se obtiene la FFT de la señal "sucia"
data_fft = np.fft.fft(combined_signal) 
freq = (np.abs(data_fft[:len(data_fft)]))

# Se hallan las frecuencias para mostrar
xf = np.linspace(0.0, 1.0/(2.0*(1.0/num_samples)), num_samples/2)

# Graficar las señales
plt.subplot(4,1,1) 
plt.title("Señal original")
# Esto añade un espacio entre subplots para que sea legible
plt.subplots_adjust(hspace = 1.5)
plt.plot(sine_wave[:500]) 
plt.subplot(4,1,2) 
plt.title("Señal ruidosa") 
plt.plot(sine_noise[:4000]) 
plt.subplot(4,1,3) 
plt.title("Señal combinada") 
plt.plot(combined_signal[:3000]) 
plt.subplot(4,1,4)
plt.title("Frecuencias de la señal") 
plt.plot(xf, freq[:num_samples//2])
plt.xlim(0,1200)
plt.show()

# Filtrar entre 950 y 1050 Hz
filtered_freq = [f if (950 < index < 1050 and f > 1) else 0 for index, f in enumerate(freq)]

# Recuperar la señal por medio de la IFFT
recovered_signal = np.fft.ifft(filtered_freq)

plt.subplot(4,1,1)
plt.title("Señal original")
# Need to add empty space, else everything looks scrunched up!
plt.subplots_adjust(hspace=1.5)
plt.plot(sine_wave[:500])
plt.subplot(4,1,2)
plt.title("Señal con ruido")
plt.plot(combined_signal[:4000])
plt.subplot(4,1,3)
plt.title("Señal filtrada")
plt.plot((recovered_signal[:500]))
plt.subplot(4,1,4)
plt.plot(xf, filtered_freq[:num_samples//2])
plt.title("Frecuencias")
plt.xlim(0,1200)
plt.show()








