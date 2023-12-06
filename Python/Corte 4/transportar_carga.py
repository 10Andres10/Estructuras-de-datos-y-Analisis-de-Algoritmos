import heapq

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

def calcular_costo(distancia, peso):
    costo_por_km = 2000  # Costo por kilómetro
    costo_total = (distancia * costo_por_km) * (peso / 150)  # Calculamos el costo total considerando el peso
    return costo_total

def generar_factura(origen, destino, ruta, costo_transporte, peso, solicitudes_desarrollar):
    with open(solicitudes_desarrollar, 'w') as archivo:
        archivo.write("Factura de Transporte\n")
        archivo.write("======================\n")
        archivo.write(f"Origen: {origen}\n")
        archivo.write(f"Destino: {destino}\n")
        archivo.write("Ruta a seguir: " + "->".join(ruta) + "\n")
        archivo.write(f"Peso de la carga: {peso} kg\n")
        archivo.write(f"Costo de transporte: ${costo_transporte:.2f}\n")
        archivo.write("======================\n")
        archivo.write("¡Gracias por elegir nuestro servicio!")

# Crear el grafo con los nodos y aristas proporcionados
mi_grafo = Grafo()

grafos = [
    ('A', ['B']),
    ('B', ['A', 'C', 'D']),
    ('C', ['B', 'E']),
    ('D', ['B', 'E']),
    ('E', ['C', 'D'])    
]

distancias_ordenadas = [
    ('A', 'B', 3),
    ('B', 'D', 6.5),
    ('B', 'C', 4.3),
    ('C', 'E', 3.5),
    ('D', 'E', 4.5),
]

for nodo, conexiones in grafos:
    mi_grafo.agregar_nodo(nodo)
    for conexion in conexiones:
        mi_grafo.agregar_arista(nodo, conexion, 0)  # La distancia es 0 porque usaremos las distancias definidas después

# Agregar distancias al grafo
for inicio, fin, distancia in distancias_ordenadas:
    mi_grafo.distancias[(inicio, fin)] = distancia
    mi_grafo.distancias[(fin, inicio)] = distancia

# Imprimir opciones para origen y destino
print("Opciones disponibles:")
print("Nodos:", mi_grafo.nodos)

# Solicitar origen y validar
while True:
    origen = str(input("Ingrese nodo inicial (origen): "))
    if origen in mi_grafo.nodos:
        break
    else:
        print("Nodo no válido. Intente de nuevo.")

# Solicitar destino y validar
while True:
    destino = str(input("Ingrese nodo destino (final): "))
    if destino in mi_grafo.nodos and destino != origen:
        break
    else:
        print("Nodo no válido o igual al origen. Intente de nuevo.")

# Solicitar peso de la carga
while True:
    try:
        peso = float(input("Ingrese el peso de la carga (en kg): "))
        break
    except ValueError:
        print("Ingrese un valor numérico válido.")

# Calcular ruta más corta y costo
costo, ruta = dijkstra(mi_grafo, origen, destino)
costo_transporte = calcular_costo(costo, peso)

# Imprimir factura en un archivo
solicitudes_desarrollar = "factura_transportista.txt"
generar_factura(origen, destino, ruta, costo_transporte, peso, solicitudes_desarrollar)

# Imprimir mensaje de éxito
print(f"\nFactura generada correctamente. Puede encontrar la factura en el archivo: {solicitudes_desarrollar}")
import heapq

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

def calcular_costo(distancia, peso):
    costo_por_km = 2000  # Costo por kilómetro
    costo_total = (distancia * costo_por_km) * (peso / 150)  # Calculamos el costo total considerando el peso
    return costo_total

def generar_factura(origen, destino, ruta, costo_transporte, peso, solicitudes_desarrollar):
    with open(solicitudes_desarrollar, 'w') as archivo:
        archivo.write("Factura de Transporte\n")
        archivo.write("======================\n")
        archivo.write(f"Origen: {origen}\n")
        archivo.write(f"Destino: {destino}\n")
        archivo.write("Ruta a seguir: " + "->".join(ruta) + "\n")
        archivo.write(f"Peso de la carga: {peso} kg\n")
        archivo.write(f"Costo de transporte: ${costo_transporte:.2f}\n")
        archivo.write("======================\n")
        archivo.write("¡Gracias por elegir nuestro servicio!")

# Crear el grafo con los nodos y aristas proporcionados
mi_grafo = Grafo()

grafos = [
    ('A', ['B']),
    ('B', ['A', 'C', 'D']),
    ('C', ['B', 'E']),
    ('D', ['B', 'E']),
    ('E', ['C', 'D'])    
]

distancias_ordenadas = [
    ('A', 'B', 3),
    ('B', 'D', 6.5),
    ('B', 'C', 4.3),
    ('C', 'E', 3.5),
    ('D', 'E', 4.5),
]

for nodo, conexiones in grafos:
    mi_grafo.agregar_nodo(nodo)
    for conexion in conexiones:
        mi_grafo.agregar_arista(nodo, conexion, 0)  # La distancia es 0 porque usaremos las distancias definidas después

# Agregar distancias al grafo
for inicio, fin, distancia in distancias_ordenadas:
    mi_grafo.distancias[(inicio, fin)] = distancia
    mi_grafo.distancias[(fin, inicio)] = distancia

# Imprimir opciones para origen y destino
print("Opciones disponibles:")
print("Nodos:", mi_grafo.nodos)

# Solicitar origen y validar
while True:
    origen = str(input("Ingrese nodo inicial (origen): "))
    if origen in mi_grafo.nodos:
        break
    else:
        print("Nodo no válido. Intente de nuevo.")

# Solicitar destino y validar
while True:
    destino = str(input("Ingrese nodo destino (final): "))
    if destino in mi_grafo.nodos and destino != origen:
        break
    else:
        print("Nodo no válido o igual al origen. Intente de nuevo.")

# Solicitar peso de la carga
while True:
    try:
        peso = float(input("Ingrese el peso de la carga (en kg): "))
        break
    except ValueError:
        print("Ingrese un valor numérico válido.")

# Calcular ruta más corta y costo
costo, ruta = dijkstra(mi_grafo, origen, destino)
costo_transporte = calcular_costo(costo, peso)

# Imprimir factura en un archivo
solicitudes_desarrollar = "factura_transportista.txt"
generar_factura(origen, destino, ruta, costo_transporte, peso, solicitudes_desarrollar)

# Imprimir mensaje de éxito
print(f"\nFactura generada correctamente. Puede encontrar la factura en el archivo: {solicitudes_desarrollar}")
