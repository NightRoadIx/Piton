from PIL import Image
from tkinter import filedialog as fd
import tkinter as tk

# Función para colocar imágenes juntas
def tile(*images, vertical=False):
    width, height = images[0].width, images[0].height
    tiled_size = (
        (width, height * len(images))
        if vertical
        else (width * len(images), height)
    )
    tiled_img = Image.new(images[0].mode, tiled_size)
    row, col = 0, 0
    for image in images:
        tiled_img.paste(image, (row, col))
        if vertical:
            col += height
        else:
            row += width
    return tiled_img

# Abrir un cuadro de diálogo para abrir una imagen
root = tk.Tk()
root.withdraw()

# Solicitar abrir el archivo
imgPath = fd.askopenfilename(
    title="Seleccionar imagen",
    filetypes=(
        ('Archivos PNG', '*.png'),
        ('Archivos JPG', '*.jpg;*.jpeg'),
        ('Archivos TIFF', '*.tiff')
    )
)

#print(imgPath)
# Abrir la imagen usando Pillow
img = Image.open(imgPath).convert('RGB')

# Mostrar la imagen usando el software que el so
# posee para abrir imágenes
img.show()

# Mostrar información de la imagen
print("Formato: ", img.format)
print("Tamaño: ", img.size)
print("Modo: ", img.mode)
print("Valor del pixel (0,0,0): ", img[0,0,0])

# Redimensionar la imagen
redimg = img.resize(
    (img.width // 2, img.height // 2)
)
redimg.show()

# Salvar la imagen
# redimg.save("Resultado.jpg")

# Transponer la imagen
img2 = img.transpose(Image.FLIP_TOP_BOTTOM)
img2.show()

# Rotar la imagen
img3 = img.rotate(45, expand=True)
img3.show()

# Separar la imagen en sus componentes
r, g, b = img.split()

# Mapear todos los elementos de la imagen a cerop!
bandacerop = r.point(lambda _: 0)
imgR = Image.merge(
    "RGB", (r, bandacerop, bandacerop)
)
imgG = Image.merge(
    "RGB", (bandacerop, g, bandacerop)
)
imgB = Image.merge(
    "RGB", (bandacerop, bandacerop, b)
)

# Juntar las imágenes para mostrar
tile(imgR, imgG, imgB).show()