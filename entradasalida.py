# Básicos del lenguaje Python
# Manejo de dispositivos de entrada/salida

'''
    Una función built-in o incorporada son aquellas que se pueden utilizar
    sin requerir de instalar librerías, ya que se encuentran dentro de la
    base del mismo lenguaje, entre ellas se encuentran:
        print()
        input()
        type()
        bin()
        etc...
'''

# * * * * * * * ENTRADA * * * * * * * #
# Ingresar cosas al Pitón =D
# variable = input("Prompt")
# Siempre regresa una cadena de texto
# por lo que puede cambiarse mediante>
# int(variable), float(variable)
entrada = float(input("Ingresa algo: "))

# * * * * * * * SALIDA * * * * * * * #
# Sacar(le) cosas al Pitón
# print tiene incluído el salto de línea
# sin embargo, mediante el parámetro end
# puede modificarse
print(f"Ingresaste: {entrada}", end="\n\n")
# Ver el tipo de datos
print(f"El tipo es: {type(entrada)}")

# Para mostrar variables se pueden utilizar varias formas:
variable = 5
# 1. Directamente usando print()
print(variable)

# 2. Usando concatenación de cadenas de texto mediante el operador '+'
print("Este es el valor de la variable: " + str(variable))
# Hay que observar que se "transforma" la variable en una cadena de texto

# 3. Mediante el método format() de las cadenas de texto
print("Este es el valor de la variable: {:}".format(variable))

# 4. Mediante las cadenas tipo "f"
print(f"Este es el valor de la variable: {variable}")

# Secuencias de escape ANSI
# Inician con \ y un código
# Salto de línea \n
# Tabulador \t
print("Esto va\t tabulado\t y más")
# Puede usarse para colocar ciertos caracteres:
# comillas \' \""
# barra invertida \\
print("Podemos colocar \\ \' y \", para poder escribirlas")

# También colocar caracteres UNICODE \u \U
# esto es usando 16 o 32 bits
print("\u00A9 Derechos reservados")
print("\u0394 Letra griega delta")
print("\u0f84 Halanta")
print("\U0001F604 Una cara sonriente")
print("\U0001F431 Un gato sonriente")

# En el caso de usar ciertos códigos
print("\x1b[30m Panda negro \x1b[0m")
print("\x1b[31m Panda rojo \x1b[0m")
print("\x1b[32m Panda verde \x1b[0m")
print("\x1b[33m Panda amarillo \x1b[0m")
print("\x1b[34m Panda azul \x1b[0m")
print("\x1b[35m Panda magenta \x1b[0m")
print("\x1b[36m Panda cyan \x1b[0m")
print("\x1b[37m Panda blanco \x1b[0m")

# Generar colores RGB
# Código 38;2;R;G;Bm  (color de fuente)
# Código 48;2;R;G;Bm  (color de fondo)
print('\x1b[48;2;100;255;25m Colores RGB \x1b[0m')