class Helper:
    '''
        Aquí se puede colocar que es lo que hace esta clase de manera general
    '''
    def __init__(self): 
        '''Se incia la clase por medio de su constructor'''
  
    def print_help(self): 
        '''Regresa la descripción de la ayuda'''
        print('Descripción de la ayuda') 

# Con esto se manda a llamar la ayuda de la clase
help(Helper) 
print("---")
# y con esto la ayuda de la función de la clase
help(Helper.print_help) 