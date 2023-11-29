import numpy as np

# Definir el número de nodos en el grafo
num_nodos = 10

# Crear una matriz de adyacencia vacía con todos los valores en cero
matriz_adyacencia = np.zeros((num_nodos, num_nodos), dtype=int)

# Establecer conexiones entre nodos (por ejemplo, el nodo 0 está conectado con el nodo 1 y viceversa)
matriz_adyacencia[1][3] = 1
matriz_adyacencia[3][2] = 1
matriz_adyacencia[3][4] = 1
matriz_adyacencia[5][1] = 1
matriz_adyacencia[5][6] = 1
matriz_adyacencia[6][8] = 1
matriz_adyacencia[8][7] = 1
matriz_adyacencia[8][9] = 1
matriz_adyacencia[9][9] = 1

# Crear una lista con las etiquetas de los nodos
nombres_nodos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

# Imprimir la matriz de adyacencia con etiquetas y formato alineado
print("{:<4}".format(""), end="")
for nodo in nombres_nodos:
    print("{:<4}".format(nodo), end="")
print()

for i in range(num_nodos):
    print("{:<4}".format(nombres_nodos[i]), end="")
    for j in range(num_nodos):
        print("{:<4}".format(matriz_adyacencia[i][j]), end="")
    print()
