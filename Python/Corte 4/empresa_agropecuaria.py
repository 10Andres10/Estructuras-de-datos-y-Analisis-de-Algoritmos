import sys
import math

potreros = [
    ('A', ['E', 'F', 'B']),
    ('B', ['C', 'A']),
    ('C', ['B', 'F', 'D']),
    ('D', ['C', 'F', 'G']),
    ('G', ['F', 'D']),
    ('F', ['E', 'A', 'C', 'G']),
    ('E', ['A', 'F']),
]

# Distancias entre potreros de mayor a menor distancia
distancias_ordenadas = [
    ('F', 'D', 400),
    ('A', 'F', 300),
    ('D', 'F', 300),
    ('B', 'C', 250),
    ('E', 'F', 250),
    ('F', 'G', 250),
    ('F', 'C', 200),
    ('C', 'D', 150),
    ('A', 'B', 150),
    ('A', 'E', 150),
]

def calcular_distancia(potrero_a, potrero_b):
    for d in distancias_ordenadas:
        if (d[0] == potrero_a and d[1] == potrero_b) or (d[0] == potrero_b and d[1] == potrero_a):
            return d[2]
    return None

def arbol_recubridor_minimo(potreros):
    n = len(potreros)
    inicio = potreros[0][0]
    visitados = [False] * n
    visitados[0] = True
    recorrido = []

    while len(recorrido) < n - 1:
        distancia_minima = sys.maxsize
        potrero_actual = None
        potrero_destino = None

        for i in range(n):
            if visitados[i]:
                for j in range(len(potreros[i][1])):
                    potrero_conectado = potreros[i][1][j]
                    if not visitados[potreros.index((potrero_conectado, []))]:
                        distancia = calcular_distancia(potrero_actual, potrero_conectado)
                        if distancia < distancia_minima:
                            distancia_minima = distancia
                            potrero_destino = potrero_conectado

        recorrido.append((potrero_actual, potrero_destino))
        visitados[potreros.index((potrero_destino, []))] = True

    return recorrido

def calcular_suministro_total(potreros, cantidad_por_animal):
    total_animales = sum(1 for potrero in potreros)
    return total_animales * cantidad_por_animal

def calcular_suministro_por_potrero(potrero, cantidad_por_animal):
    return 1 * cantidad_por_animal

def main():
    while True:
        print("\nMenú:")
        print("1. Árbol recubridor mínimo.")
        print("2. Cálculo total suministro de todo el suministro.")
        print("3. Calcular suministro por potrero.")
        print("4. Salir.")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            recorrido_ideal = arbol_recubridor_minimo(potreros)
            print("Recorrido ideal:")
            for arco in recorrido_ideal:
                print(f"Potrero {arco[0]} -> Potrero {arco[1]}")

        elif opcion == "2":
            cantidad_total = calcular_suministro_total(potreros, 120)
            print(f"Cantidad total de suministro: {cantidad_total} gramos")

        elif opcion == "3":
            potrero = input("Ingrese el nombre del potrero (A-G): ").upper()
            if potrero in [p[0] for p in potreros]:
                suministro_por_potrero = calcular_suministro_por_potrero(potrero, 120)
                print(f"Suministro para Potrero {potrero}: {suministro_por_potrero} gramos")
            else:
                print("Potrero no válido.")

        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
