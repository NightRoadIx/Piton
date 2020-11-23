nombre = "Ying"

def funcionExterna():
    nombre = "Yang"
    
    def funcionInterna():
        nonlocal nombre
        nombre = "el Ying y el Yang"
        print(nombre)
        
    funcionInterna()
    print(nombre)

funcionExterna()
print(nombre)