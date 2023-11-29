import sys
import math

# Función para calcular la distancia entre dos puntos (coordenadas)
def calcular_distancia(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Función para encontrar el árbol recubridor mínimo usando el algoritmo de Prim
def arbol_recubridor_minimo(potreros):
    n = len(potreros)
    # Seleccionar el primer potrero como inicio
    inicio = potreros[0]
    visitados = [False] * n
    visitados[0] = True
    recorrido = []

    while len(recorrido) < n - 1:
        distancia_minima = sys.maxsize
        potrero_actual = None
        potrero_destino = None

        for i in range(n):
            if visitados[i]:
                for j in range(n):
                    if not visitados[j]:
                        distancia = calcular_distancia(potreros[i], potreros[j])
                        if distancia < distancia_minima:
                            distancia_minima = distancia
                            potrero_actual = i
                            potrero_destino = j

        recorrido.append((potrero_actual, potrero_destino))
        visitados[potrero_destino] = True

    return recorrido

# Función para calcular el suministro total
def calcular_suministro_total(potreros, cantidad_por_animal):
    total_animales = sum(potrero[2] for potrero in potreros)
    return total_animales * cantidad_por_animal

# Función para calcular el suministro por potrero
def calcular_suministro_por_potrero(potrero, cantidad_por_animal):
    return potrero[2] * cantidad_por_animal

# Función principal
def main():
    potreros = [(0, 0, 50), (1, 1, 30), (2, 2, 40), (3, 3, 25), (4, 4, 35), (5, 5, 20), (6, 6, 45)]

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
                potrero_origen, potrero_destino = arco
                print(f"Potrero {potrero_origen} -> Potrero {potrero_destino}")

        elif opcion == "2":
            cantidad_total = calcular_suministro_total(potreros, 120)
            print(f"Cantidad total de suministro: {cantidad_total} gramos")

        elif opcion == "3":
            potrero = int(input("Ingrese el número de potrero (0-6): "))
            if 0 <= potrero < len(potreros):
                suministro_por_potrero = calcular_suministro_por_potrero(potreros[potrero], 120)
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
