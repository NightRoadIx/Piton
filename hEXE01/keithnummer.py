# Función para verificar si se trata de un número de Keith
def Keith(x):  
   
    # Guarda todos los dígitos del número x
    terms = [];  
    temp = x;
    # Número de dígitos en el número x
    n = 0;
    # Cargar los dígitos
    while (temp > 0): 
        terms.append(temp % 10);  
        temp = int(temp / 10);  
        n+=1;  
  
    # Obtener los dígitos en orden derecho
    terms.reverse();  
  
    # Buscar los siguientes términos de una secuencia
    # generados usando dígitos de x hasta que se alcance x
    # o uno mayor a x
    next_term = 0;  
    i = n;  
    while (next_term < x):  
        next_term = 0;  
  
        # El siguiente término es la suma de los previos
        for j in range(1,n+1):  
            next_term += terms[i - j];  
  
        terms.append(next_term);  
        i+=1;  
  
    # Regresar si ambos términos son iguales (un booleano)
    return (next_term == x);  

# # # PROGRAMA PRINCIPAL # # #
print("El número ", 197, end = "")
print(" es Número de Keith") if (Keith(197)) else print(" no es Número de Keith")