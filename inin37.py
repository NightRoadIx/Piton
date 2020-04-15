'''
    GENERAR ARCHIVOS PDF CON PYTHON (REPORTLAB)
    Muchas veces cuando se quieren generar reportes a partir de un programa
    lo que se hace es copiar los datos generados por el programa, o se guardan
    archivo txt o csv con los datos generados, sin embargo, Python cuenta con
    un toolkit para crear documentos PDF.
    
    Instalar con: pip install reportlab
    
'''
#%%
# Mandar a cargar las librerías a utilizar
from reportlab.pdfgen import canvas
# estas permiten manejar los tamaños de las hojas a crear, las más utilizadas
# son el tamaño A4 o Letter
from reportlab.lib.pagesizes import A4, letter

# Con esto podemos conocer cual es el ancho y alto de la hoja
# Letter es de 612 x 792 pixeles
w, h = letter

# Ahora se genera el archivo PDF con el nombre "muestra" y de tamaño pagesize
c = canvas.Canvas("muestra.pdf", pagesize=letter)
# Ahora lo que se hace es dibujar en el pixel (50, h-50) el texto
# Es importante recalcar que a diferencia de muchas otras librerías, el 
# origen de coordenadas (0,0) se localizan en el extremo inferior izquierdo
# de la hoja, por lo que Y aumenta conforme se sube en la hoja y X cuando
# se recorre hacia la derecha
c.drawString(50, h-50, "Este es un texto horrible")

# También es posible pintar líneas
c.line(50, h-70, 200, h-70)
# Un rectángulo ((x,y) de la esquina superior izquierda, ancho, alto)
c.rect(50, h-300, 300, 200)
# círculos (centro (x,y), radio)
c.circle(100, h-100, 50)

# Generar rejillas
# Se crean listas de posciones en X, Y, en odnde colocarán cada una de las
# líneas que componen a la rejilla
xlist = [310, 360, 410, 460]
ylist = [h - 10, h - 60, h - 110, h - 160]
c.grid(xlist, ylist)

# Las imágenes se pueden colocar mediante
c.drawImage("coreanoviro.jpg", 400, h-400, width = 100, height = 100)

# Finalmente se salva el archivo
c.save()

#%%

# En esta sección del código se generará un reporte de calificaciones de 
# alumnos
import itertools
from random import randint
from statistics import mean
from reportlab.pdfgen import canvas

# función grouper
def grouper(iterable, n):
    # Crea a partir de ciertos datos iterables (en este caso los datos)
    # una variable para manejarlos
    args = [iter(iterable)] * n
    # Aquí entonces regresa los datos "encapsulados" de manera apuntador
    #Es por ello que se envían así a la función
    return itertools.zip_longest(*args)

# Función para exportar al PDF
def export_to_pdf(data):
    # Primero se crea el archivo PDF con su nombre y tamaño de hoja
    c = canvas.Canvas("alumnos.pdf", pagesize=A4)
    # Se saca el tamaño de la hoja A4
    w, h = A4
    # con esto se establece el número máximo de registros por página
    max_rows_per_page = 45
    # Márgenes
    x_offset = 50
    y_offset = 50
    # Se coloca un espacio entrew cada una de las filas
    padding = 15
    
    # Aquí se genera las listas para cada una de las líneas que comprenderán
    # a la rejilla de la tabla
    xlist = [x + x_offset for x in [0, 200, 250, 300, 350, 400, 480]]
    # Observar como se generan las líneas horizontales en el eje Y
    ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
    
    # Pasar por todos los datos
    for rows in grouper(data, max_rows_per_page):
        # acomodar las fils
        rows = tuple(filter(bool, rows))
        # Crear las líneas de la rejillas de la tabla
        c.grid(xlist, ylist[:len(rows) + 1])
        # en este doble for se va iterando sobre los datos para irlos
        # "pintando" dentro de 1 sola página
        for y, row in zip(ylist[:-1], rows):
            for x, cell in zip(xlist, row):
                c.drawString(x + 2, y - padding + 3, str(cell))
        # Showpage termina la página
        c.showPage()
    # Aquí termina de crear cada página y salva el archivo
    c.save()

# Se genera una lista con los datos del encabezado de la tabla
data = [("NOMBRE", "NOTA 1", "NOTA 2", "NOTA 3", "PROM.", "ESTADO")]
# Ahora recorrer de 1 a 100 elementos (que serán como simular 100 alumnos)
for i in range(1, 101):
    # Los exámenes se crea una lista de 3 elementos aleatorios
    exams = [randint(0, 10) for _ in range(3)]
    # Se obtiene el promedio de las calificaciones generadas
    avg = round(mean(exams), 2)
    # Aquí se decide si su estado es Aprobado o Reprobado
    state = "Aprobado" if avg >= 6 else "Reprobado"
    # Se añadden a la lista losa valores, observar que exams se trata como una
    # especie de apuntador
    data.append((f"Alumno {i}", *exams, avg, state))
# Una vez que se generaron las 100 calificaciones, se crear el PDF
export_to_pdf(data)