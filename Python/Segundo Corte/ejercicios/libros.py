#Importar librerias
#import os #Buscar para que funciona
import random

#Declaracion de variables
libros = []
categorias = ["A", "B", "C"]
libros_categoria = []

n = int(input("Ingrese el numero de libros: "))

for i in range(0, n):      
    libros.append(random.choice(categorias)) 
    

while libros[0] != "A" or libros[n-1] != "C":
    libros.clear()
    for i in range(0, n):      
        libros.append(random.choice(categorias)) 
        
    if libros[0] == "A" and libros[n-1] == "C":
        break
    else:
        continue


print(libros)