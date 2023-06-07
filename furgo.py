from PIL import Image
from PIL.ExifTags import TAGS
from tkinter import filedialog as fd
import tkinter as tk

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
img = Image.open(imgPath)

# Mostrar la imagen
img.show()

# Verificar si la imagen contiene datos EXIF
if hasattr(img, "exif"):
    # Extraer los datos EXIF
    exifdata = img.getexif()

    print(exifdata)
    # Iterar sobre los campos de los datos EXIF
    # Exchangeable Image File Format
    # son metadatos que contienen las imágenes, referentes
    # a la fecha de captura, tipo de cámara, resolución,
    # fecha, hora, coordenadas GPS
    for tag_id in exifdata:
        # Obtener el nombre de la etiqueta, en lugar de datos no leíbles
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)

        # decodificar los datos
        if isinstance(data, bytes):
            data = data.decode()
        print(f"{tag:25}: {data}")
else:
    print("La imagen no contiene datos exif")