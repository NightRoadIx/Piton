while True:
    # Ingresar un número
    N = input("Nümêrò: ")
    # Se hacen las verificaciones
    # lo ingresado es un dígito?
    if N.isdigit():
        # En caso de que sea un dígito,
        # cambiar a entero
        N = int(N)
        # y verificar el intervalo correcto (positivo))
        if N > 0:
            # Aquí es cuando el valor es correcto
            # rompe el ciclo
            break
        else:
            print("Intervalo incorrecto")
    else:
        print("No es un nümêrò")

a, b, c, i = 0, 1, 0, 0
# print(a, b)

# for(i=0; i <=; i++)
# for tmp in Iterador:
# r = 1:2:10
# range(1, 10, 2)             [1, 10)
for i in range(0, N-2, 1):
    c = a + b
    a, b = b, c
'''
while (i <= N-3):
    c = a + b
    a, b = b, c
    i += 1      # acumulador
'''
print(f'El número {N} de la serie es {c}')








