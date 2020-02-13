'''
	Manejo de módulos
	Módulo de fechas datetime
'''
# Se debe de incluir la librería datetime
# Para importar librerias se utiliza la siguiente sintaxis
#
# import modulo
#
# Y para utilizar métodos o constantes se utilizan como:
#
# modulo.metodo()
#
# Sin embargo, se puede renombrar como:
#
# import modulo as md
#
# Y entonces para usar ya sea los métodos o constantes:
#
# md.metodo()

# Importar un módulo y renombrarlo
import datetime as dt

# Obtener la fecha
x = dt.datetime.now()
print(x)

# Mostrar solamente el año
print(x.year)

# Método strftime()
# Mostrar el día de la semana
print(x.strftime("%A"))
# Mostrar el nombre del mes
print(x.strftime("%B"))
'''
	%b		Nombre del mes, versión corta
	%m		Número de mes [1,12]
	%d		Día de la semana
	%Y		Número de año
	%H		Hora [0,23]
	%h		hora [0,12]
	%p		PM/AM
	%M		Minuto
	%S		Segundo
	%f		microsegundo
	Entre otros...
'''

# Crear un elemento del tipo fecha
y = dt.datetime(2020, 5, 17)
print(y)
# Se puede crear el elemento tipo fecha con todos los datos