# Pedir al usuario que ingrese los valores
N = int(input("N: "))
a = int(input("a: "))
b = int(input("b: "))
m = int(input("m: "))
X = int(input("Semilla: "))

print("n\tXn\tXn+1\tUn")
for n in range(0, N, 1):
    U = X / m   # calcular el aleatorio
    print(f'{n}\t{X}\t', end="")
    X = (a*X + b) % m # calcular el siguiente
    print(f'{X}\t{U}')






