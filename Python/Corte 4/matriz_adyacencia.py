import heapq
import json

class Grafo:
    def __init__(self):
        self.nodos = set()
        self.aristas = {}
        self.distancias = {}

    def agregar_nodo(self, valor):
        self.nodos.add(valor)
        self.aristas[valor] = []
        self.distancias[(valor, valor)] = 0

    def agregar_arista(self, desde, hasta, distancia):
        if desde not in self.aristas:
            self.agregar_nodo(desde)
        if hasta not in self.aristas:
            self.agregar_nodo(hasta)

        self.aristas[desde].append(hasta)
        self.aristas[hasta].append(desde)
        self.distancias[(desde, hasta)] = distancia
        self.distancias[(hasta, desde)] = distancia

def dijkstra(grafo, inicio, fin):
    cola = [(0, inicio, [])]
    visitados = set()

    while cola:
        (costo, actual, camino) = heapq.heappop(cola)

        if actual not in visitados:
            visitados.add(actual)
            camino = camino + [actual]

            if actual == fin:
                return (costo, camino)

            for siguiente in grafo.aristas[actual]:
                nueva_distancia = costo + grafo.distancias[(actual, siguiente)]
                heapq.heappush(cola, (nueva_distancia, siguiente, camino))

    return (float("inf"), [])

def generar_factura(origen, destino, ruta, costo, solicitudes_desarrollar, formato):
    resultados = {
        "origen": origen,
        "destino": destino,
        "ruta": ruta,
        "costo": costo
    }

    if formato == 'txt':
        with open(solicitudes_desarrollar, 'w') as archivo:
            archivo.write("Rutas definidas por el usuario\n")
            archivo.write("==============================\n")
            archivo.write("+++++ Valores Eficientes +++++\n")
            archivo.write(f"Origen: {origen}\n")
            archivo.write(f"Destino: {destino}\n")
            archivo.write("Ruta a seguir: " + "->".join(ruta) + "\n")
            archivo.write("==============================\n")
            archivo.write("--------- Menor Valor --------\n")
            archivo.write(f"Origen: {origen}\n")
            archivo.write(f"Destino: {destino}\n")
            archivo.write("Ruta a seguir: " + "->".join(ruta) + "\n")
            archivo.write("==============================\n")
            archivo.write("¡Gracias por elegir nuestro servicio!")
    elif formato == 'json':
        with open(solicitudes_desarrollar, 'w') as archivo:
            json.dump(resultados, archivo)

# Crear el grafo con los nodos y aristas proporcionados
mi_grafo = Grafo()

grafos = [
    ('A', ['B', 'C', 'D']),    
    ('B', ['A', 'C','D']),
    ('C', ['A', 'B','D']),
    ('D', ['A', 'C','B']),
]

distancias_ordenadas = [
    ('A', 'B', 3),
    ('A', 'C', 4),
    ('A', 'D', 1),
    ('B', 'C', 1),
    ('B', 'D', 3),
    ('C', 'D', 5),
]

for nodo, conexiones in grafos:
    mi_grafo.agregar_nodo(nodo)
    for conexion in conexiones:
        mi_grafo.agregar_arista(nodo, conexion, 0)  # La distancia es 0 porque usaremos las distancias definidas después

# Agregar distancias al grafo
for inicio, fin, distancia in distancias_ordenadas:
    mi_grafo.distancias[(inicio, fin)] = distancia
    mi_grafo.distancias[(fin, inicio)] = distancia

# Solicitar cuantas rutas quiere definir el usuario
num_rutas = int(input("Ingrese cuantas rutas quiere definir: "))

for i in range(num_rutas):
    # Solicitar origen y validar
    while True:
        origen = str(input(f"Ingrese nodo inicial (origen) para la ruta {i+1}: "))
        if origen in mi_grafo.nodos:
            break
        else:
            print("Nodo no válido. Intente de nuevo.")

    # Solicitar destino y validar
    while True:
        destino = str(input(f"Ingrese nodo destino (final) para la ruta {i+1}: "))
        if destino in mi_grafo.nodos and destino != origen:
            break
        else:
            print("Nodo no válido o igual al origen. Intente de nuevo.")

    # Calcular la ruta más corta para cada ruta del usuario
    costo, ruta = dijkstra(mi_grafo, origen, destino)

    # Solicitar formato de archivo al usuario
    formato = input("Ingrese el formato del archivo (txt o json): ")

    # Generar factura en un archivo
    solicitudes_desarrollar = f"Resultados_ruta_{i+1}." + formato
    generar_factura(origen, destino, ruta, costo, solicitudes_desarrollar, formato)

    # Imprimir mensaje de éxito
    print(f"\nResultados para la ruta {i+1} generados correctamente. Puede encontrar los detalles en el archivo: {solicitudes_desarrollar}")