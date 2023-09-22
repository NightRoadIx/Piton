"""
    Programa que contiene información acerca de
    los comandos de control
"""
"""
    DECISIONES
    if cond1:
      instrucciones
    elif cond2:
      instrucciones
    else:
      instrucciones
"""
"""
    CICLOS 
    while cond:    
      instrucciones mientras cond es True
"""

while True: # ciclo sin fin
    inciso = input("Ingresa el inciso: ")
    if inciso == 'a':
        print("Ya vámonos!")
    elif inciso == 'b':
        print("Qué sueño!")
    elif inciso == 'c':
        print("Desayuno de campeones, vodka con cereal")
    elif inciso == 'd':
        print("Salir "*5)
        break   # rompe el ciclo anterior
    else:
        print("Eso no existe! Tramita tu baja... de la bida")
# Se ejecuta al finalizar ciclo
print("Ups!")

# %%
# Revisar si el dato ingresado es numérico
# y se encuentra dentro de un intervalo
while True:
    # Pedir la edad
    edat = input("Edad: ")
    # Se hacen las verificaciones
    # lo ingresado es un dígito?
    if edat.isdigit():
        # En caso de que sea un dígito,
        # cambiar a entero
        edat = int(edat)
        # y verificar el intervalo correcto [18, 99]
        if (edat >= 18) and (edat <= 99):
            # Aquí es cuando el valor es correcto
            # rompe el ciclo
            break
        else:
            print("Edad incorrecta")
    else:
        print("No es un número")
print(f"Edad ingresada {edat} años")