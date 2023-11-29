from collections import deque

# Definir el número de nodos en el grafo
num_nodos = 10

# Crear una matriz de adyacencia vacía con todos los valores en cero
matriz_adyacencia = [[0] * num_nodos for _ in range(num_nodos)]

# Establecer conexiones entre nodos
matriz_adyacencia[5][1] = 1  # F -> B
matriz_adyacencia[1][5] = 1  # B -> F
matriz_adyacencia[1][0] = 1  # B -> A (Nueva conexión)
matriz_adyacencia[1][3] = 1  # B -> D
matriz_adyacencia[1][9] = 1  # B -> J
matriz_adyacencia[3][2] = 1  # D -> C
matriz_adyacencia[3][4] = 1  # D -> E
matriz_adyacencia[5][6] = 1  # F -> G
matriz_adyacencia[6][8] = 1  # G -> I
matriz_adyacencia[8][7] = 1  # I -> H

# Imprimir la matriz de adyacencia en el formato deseado
print("    " + "   ".join(chr(ord('A') + i) for i in range(num_nodos)))  # Encabezado de columnas

for i in range(num_nodos):
    print(chr(ord('A') + i) + "   " + "   ".join(str(matriz_adyacencia[i][j]) for j in range(num_nodos)))

print("\n")

# --- Recorrido en Profundidad (DFS) ---

print("DFS: Búsqueda por profundidad")
stack = [5]  # Nodo de inicio (F)
visitados_dfs = set()

while stack:
    nodo_actual = stack.pop()
    if nodo_actual not in visitados_dfs:
        print(chr(ord('A') + nodo_actual), end=" ")  # Convertir índice a letra
        visitados_dfs.add(nodo_actual)
        # Agregar vecinos no visitados a la pila
        stack.extend(neighbour for neighbour, isConnected in enumerate(matriz_adyacencia[nodo_actual]) if isConnected and neighbour not in visitados_dfs)

print("\n")

# --- Recorrido en Anchura (BFS) ---

print("BFS: Búsqueda por anchura")
queue = deque([5])  # Nodo de inicio (F)
visitados_bfs = set()

while queue:
    nodo_actual = queue.popleft()
    if nodo_actual not in visitados_bfs:
        print(chr(ord('A') + nodo_actual), end=" ")  # Convertir índice a letra
        visitados_bfs.add(nodo_actual)
        # Agregar vecinos no visitados a la cola
        queue.extend(neighbour for neighbour, isConnected in enumerate(matriz_adyacencia[nodo_actual]) if isConnected and neighbour not in visitados_bfs)

print("\n")
