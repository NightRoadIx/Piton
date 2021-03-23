# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 17:00:00 2021

@author: NightRoadIx
"""

'''
    Programa para el cálculo de la serie de Fibonacci
    Utilizando la Programación Orientada a Objetos
    
    0, 1, 1, 2, 3, 5, 8, 13, ...
    
    El usuario ingresa cuántos números quiere ver de la serie
    Solamente se debe ingresar un número entero y positivo > 1
'''

class Fibonacci:
    # ATRIBUTOS
    # int n
    # int arreglo[]
    
    # MÉTODOS
    # Constructor
    def __init__(self):  # self (Python) -> this (C#)
        self.n = 0
        self.arreglo = []
    
    # Recepción de valores enteros
    def recibirValorInt(self, nim = 1, xam = 46):
        while True:
            resp = input("Ingrese el número de elementos de la serie: ")
            try:
                self.n = int(resp)
                if( (self.n >= nim)and(self.n < xam) ):
                    break
                print("Ingrese un valor dentro del intervalo ({:},{:})".format(
                        nim, xam))
            except ValueError:
                print("Error mortal, volver a intentar ")
    
    # Recepción de valores caracter
    def recibirValorChar(self, *args):
        while True:
            resp = input("Mostrar otros valores? (s/n): ").lower()
            if( len(resp) > 1):
                print("No es un solo caracter")
            elif resp not in args:
                print("Caracter erróneo")
            else:
                return resp
        
    # Calcular la serie
    def calcularFibonacci(self):
        a, b, c = 1, 0, 0
        
        for tmp in range(0, self.n):
            self.arreglo.append(c)
            c = a + b
            a, b = b, c
    
    # Mostrar la serie
    def mostrarFibonacci(self):
        for tmp in self.arreglo:
            print(tmp, end = ", ")
 
# PARTE MAIN
# Este main indica que el intérpete de Python está ejecutando el script y no
# importándolo, esto es en especial importante al incluir la palabra "import"
if __name__ == "__main__":
    # Instanciar un objeto
    serie = Fibonacci()
    
    while True:
        serie.recibirValorInt()
        serie.calcularFibonacci()
        serie.mostrarFibonacci()
        
        opc = serie.recibirValorChar('s', 'n')
        if(opc == 'n'):
            break
        