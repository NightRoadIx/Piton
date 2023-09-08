# Básicos del lenguaje Python
# Manejo de la ALU, operaciones artimético-lógicas

# * * * * * * * ALU * * * * * * * #
# Unidad Aritmética Lógica
# Operaciones aritméticas
print(f"5 + 4 = {5+4}")     # suma
print(f"5 - 4 = {5-4}")     # resta
print(f"5 * 4 = {5*4}")     # multiplicación
print(f"5 / 4 = {5/4}")     # división
print(f"5 // 4 = {5//4}")   # división entera
print(f"5 % 4 = {5%4}")     # módulo o residuo
print(f"5 ** 4 = {5**4}")   # potencia

# Operaciones lógicas
# tipo de datos: bool
# Tablas de verdad
# Operación and, y, intersección
print(f"T & T = {True and True}")
print(f"T & F = {True and False}")
print(f"F & T = {False and True}")
print(f"F & F = {False and False}")
# Operación or, o, unión
print(f"T | T = {True or True}")
print(f"T | F = {True or False}")
print(f"F | T = {False or True}")
print(f"F | F = {False or False}")
# Operación not, no, complemento
print(not True)
print(not 0)
# Lo que se obtiene es la clase bool
print(type(True))

# Operaciones de comparación
# regresa un bool
print(5 > 6)    # False
print(5 < 6)    # True
print(5 == 6)   # False
# OJO: nunca comparar == para datos float
# de preferencia utilizar solamente, mayor o menor que
print(5.0 == 5.0)   # puede ser False
print(5 != 6)   # True

# Operaciones con bits
# Unidad mínima de información
# por Claude Shannon
# Cambiar bases numéricas, pasa a str
# a partir de un int
print(bin(42))  # binario
print(hex(42))  # hexadecimal
print(oct(42))  # octal

# Operador and (y)
print(f'{bin(69)} & {bin(255)} = {bin(69 & 255)}')
print(69 & 255)
# Operador or (o)
print(f'{bin(69)} | {bin(255)} = {bin(69 & 255)}')
print(69 | 0)
# Operador xor (o exclusivo)
print(f'{bin(69)} ^ {bin(255)} = {bin(69 & 255)}')
print(69 ^ 0)

# Operador de desplazamiento de bits
# A la derecha
print(138 >> 1)
# A la izquierda
print(34 << 1)
