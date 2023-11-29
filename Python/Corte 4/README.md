## Se tienen los datos de un grupo de 5 transacciones referentes a las matrículas de un grupo de estudiantes (código, apellidos, nombres, créditos), almacenadas como txt, crear un arreglo con estas transacciones y a partir del mismo, calcular cuántos estudiantes y su número de créditos matriculados, tienen un mayor número de créditos matriculados que el promedio de todos los estudiantes; generando esta respuesta en una tupla.
-----------------------------------------------------------------------------------------
## import numpy as np

# Definir el número de nodos en el grafo
num_nodos = 10

# Crear una matriz de adyacencia vacía con todos los valores en cero
matriz_adyacencia = np.zeros((num_nodos, num_nodos), dtype=int)

# Establecer conexiones entre nodos (por ejemplo, el nodo 0 está conectado con el nodo 1 y viceversa)
matriz_adyacencia[0][1] = 1
matriz_adyacencia[1][0] = 1

# Mostrar la matriz de adyacencia
print("Matriz de adyacencia:")
print(matriz_adyacencia)

## Implementar el recorrido en Profundidad y a lo ancho en Python o Java.
-----------------------------------------------------------------------------------------
## Problema 1 
## Una empresa agropecuaria tiene su propiedad dividida en 7 potreros para el engorde de bovinos, el mapa de estos potreros es el siguiente, distancias en metros.

![Mapa](ej1.png)

## Mediante un programa determine cual debe ser el recorrido ideal para asegurarse de llevar suplementos alimenticios a cada uno de los potreros, la longitud del recorrido en metros y calcular la cantidad total y cuanto se debe dejar del suplemento en cada potrero, si la cantidad a suministrar se les calcula dando 120gr por cada animal.

# menú con 4 opciones: 
# 1. Árbol recubridor mínimo. 
# 2. Cálculo total suministro de todo el suministro.
# 3. Calcular suministro por potrero.
# 4. Salir.
-----------------------------------------------------------------------------------------
