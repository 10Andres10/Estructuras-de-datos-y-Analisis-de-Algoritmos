class Nodo:
    def __init__(self, valor):
        self.item = valor
        self.dir = None

class Lista:
    def __init__(self):
        self.primer_nodo = None

    def insertar_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.dir = self.primer_nodo
        self.primer_nodo = nuevo_nodo
    
    def recorrer_lista(self):
        elementos = []  # Creamos una lista para almacenar los elementos
        n = self.primer_nodo
        while n is not None:
            elementos.append(n.item)
            n = n.dir
        return elementos  # Devolvemos la lista de elementos

    def insertar_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.primer_nodo is None:
            self.primer_nodo = nuevo_nodo
            return
        n = self.primer_nodo
        while n.dir is not None:
            n = n.dir
        n.dir = nuevo_nodo

# 1. Insertar por valor 

    def buscar_valor(self, valor):
        n = self.primer_nodo
        while n is not None:
            if n.item == valor:
                return n
            n = n.dir
        return None

mi_lista = Lista()
c = 0
while c <= 10:
    mi_lista.insertar_inicio(c)
    c += 1

valor_buscado = int(input("Ingrese el valor del 0 al 10 que se desea buscar: "))
valor_ingresado = int(input("Ingrese el valor a añadir: "))

nodo_buscado = mi_lista.buscar_valor(valor_buscado)

if nodo_buscado is not None:
    nuevo_nodo = Nodo(valor_ingresado)
    nuevo_nodo.dir = nodo_buscado.dir
    nodo_buscado.dir = nuevo_nodo
    print("Se insertó el valor ", valor_ingresado, " después de ", valor_buscado)
    print("Lista actualizada:")
    print(mi_lista.recorrer_lista())
else:
    print("No se encontró el valor ", valor_buscado, " en la lista.")