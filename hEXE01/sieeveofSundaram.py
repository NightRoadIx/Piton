# Imprime los números primos menores a n
def SieveOfSundaram(n): 
      
    '''
        En general, la criba de Sundaram
        produce números primos menores a
        (2*x + 2) para un número dado x.
        Ya que se desea obtener los números
        primos menores que n, se reduce n a
        la mitad
    '''
    nNew = int((n - 2) / 2)
    '''
        Este arreglo es utilizado para separar los
        números de la forma i+j+2ij
        de otros donde 1 <= i <= j
        Y se inicializan todos los elementos 
        como no marcados
    '''
    marked = [0] * (nNew + 1) 
    '''
        La lógica principak de Sundaram
        Marcar todos los números de la forma
        i + j + 2ij
        como verdaderos donde 1 <= i <= j
    '''
    for i in range(1, nNew + 1): 
        j = i
        while((i + j + 2 * i * j) <= nNew): 
            marked[i + j + 2 * i * j] = 1;
            j += 1 
  
    # Dado que 2 es un número primo
    if (n > 2): 
        print(2, end = " ") 
  
    # Imprime otros primos
    # los demás son de la forma 2*i + 1  
    # a los que la marca marked[i] es falsa
    # such that marked[i] is false. 
    for i in range(1, nNew + 1): 
        if (marked[i] == 0): 
            print((2 * i + 1), end = " ") 


# # # CODIGO PRINCIPAL # # #
n = 50000
SieveOfSundaram(n);