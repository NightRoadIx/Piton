'''
    Manejo de archivos PDF
    
    Requiere de la instalación de la librería PyPDF2
    pip install PyPDF2
'''
# Importar la librería
import PyPDF2 
  
# Crear un objeto archivo pdf
pdfFileObj = open('exemple.pdf', 'rb') 
  
# Crear el objeto lector de pdf
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

# Obtener información del documento
info = pdfReader.getDocumentInfo()
print("Autor: ", info.author)
print("Creador: ", info.creator)
print("Productor: ", info.producer)
print("Materia: ", info.subject)
print("Título: ", info.title)
# Imprimir el número de páginas del documento
print("Número de páginas: ", pdfReader.numPages) 
  
# Crear un objeto página
pageObj = pdfReader.getPage(1) 
  
# Extraer texto del objeto página
print(pageObj.extractText()) 

# IMPORTANTE, CERRAR EL ARCHIVO PDF
pdfFileObj.close() 

#%% 
# Separar un PDF
# Generar la función para separar 
def PDFsplit(pdf, splits): 
    # Crear un objeto archivo pdf
    pdfFileObj = open(pdf, 'rb') 
      
    # Crear el objeto lector de pdf
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
      
    # Índice de la primera rebanada
    start = 0
      
    # Índice de la última rebanada
    end = splits[0]
      
    for i in range(len(splits)+1): 
       # Crear el objeto escritura de pdf para la (i+1)-sima rebanada 
        pdfWriter = PyPDF2.PdfFileWriter() 
          
        # Nombre e salida del PDF
        outputpdf = pdf.split('.pdf')[0] + str(i) + '.pdf'
          
        # Añadir páginas al objeto escritura del PDF
        for page in range(start,end): 
            pdfWriter.addPage(pdfReader.getPage(page)) 
          
        # Escribir esas páginas en el archivo PDF
        with open(outputpdf, "wb") as f: 
            pdfWriter.write(f) 
  
        # Intercambiar las posiciones
        start = end 
        # Esto se coloca en un try - except para evitar errores
        try: 
            # Colocar la posición final de la rebanada para la siguiente división
            end = splits[i+1] 
        except IndexError: 
            # Colocar la posición final de la rebanada para la última división
            end = pdfReader.numPages 
          
    # Cerrar el objeto de entrada archivo PDF
    pdfFileObj.close() 

# Nombre del archivo a separar
pdf = "exemple.pdf"
# Posición de las páginas a separar
splits = [2,4]
# Llamar a la función
PDFsplit(pdf, splits)       

