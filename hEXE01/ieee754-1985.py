# Función para convertir de decimal a binario
def float_bin(number, lugares = 3):
    # Separar el número recibido en su parte entera y decimal
    ent, dec = str(number).split(".")
    ent = int(ent)  
    dec = int(dec)
    # quitar la parte '0b' y concatenar con un punto '.'
    res = bin(ent).lstrip("0b") + "."
  
    for x in range(lugares):  
        ent, dec = str((conversor(dec)) * 2).split(".")  
        dec = int(dec)  
        res += ent
    return res  
  
# conversor decimal
def conversor(num):
    while num > 1:
        num /= 10
    return num
  
def IEEE754(n) :
    # Identificar si el número es positivo o negativo
    sign = 0
    if n < 0 : 
        sign = 1
        n = n * (-1)
    # La cantidad de digitos
    p = 30
  
    # Convertir de decimal a binario (manda parámetro lugares a cierto valor)
    dec = float_bin (n, lugares = p) 
  
    # Separar la parte decimal y entera
    ent, dec = str(dec).split(".") 
    ent = int(ent)
  
    # Calcular el exponente
    exponent = len(str(ent)) - 1
    exponent_bits = 127 + exponent 
    
    # Convertir el exponente de decimal a binario 
    exponent_bits = bin(exponent_bits).lstrip("0b") 
  
    # Encontrar la mantisa
    mantissa = str(ent)[1:exponent + 1] 
    mantissa = mantissa + dec 
    mantissa = mantissa[0:23] 
  
    # Finalmente hallar la notación IEEE754 en binario
    final = str(sign) + str(exponent_bits) + mantissa 
    
    # Regresar el valor IEEE754 hallado
    return (final) 

# # # PROGRAMA PRINCIPAL # # #
res = False
num = ""
while not(res):
    num = input('Ingrese un valor real a convertir: ')
    try:
        num = float(num)
        res = True
    except:
        print("Lo ingresado no es un número")
        res = False

print(IEEE754(num))