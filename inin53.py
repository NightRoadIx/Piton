# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 17:09:32 2021

@author: s_bio
"""
#%%
from PIL import Image, ImageDraw
# Python Image Library

# Con esto se genera una lista con las imágenes que conformarán el gif
# animado
images = []

#%%
# Colocar los valores de la imagen
# Ancho
width = 200
# Centro
center = width // 2
# Colores (se usa RGB)
color_1 = (0, 0, 0)
color_2 = (255, 255, 255)
# Radio máximo 
max_radius = int(center * 1.5)
# Pasos con los que se generará la animación
step = 8

#%%
# Ir generando el primer círculo de color negro
for i in range(0, max_radius, step):
    # Con esto se genera una imagen nueva
    im = Image.new('RGB', (width, width), color_1)
    # Dibujar la imagen generada
    draw = ImageDraw.Draw(im)
    # Con esto se dibuja una elipse, de acuerdo a la perspectiva, se tiene que
    # crear una elipse en lugar de un círculo para que no se vea tan feo
    draw.ellipse((center - i, center - i, center + i, center + i), fill=color_2)
    # Ir añadiendo los cuadros generados a la lista
    images.append(im)

#%%
for i in range(0, max_radius, step):
    im = Image.new('RGB', (width, width), color_2)
    draw = ImageDraw.Draw(im)
    draw.ellipse((center - i, center - i, center + i, center + i), fill=color_1)
    images.append(im)

#%%
images[0].save('pillow_imagedraw.gif',
               save_all=True, append_images=images[1:], optimize=False, duration=40, loop=0)