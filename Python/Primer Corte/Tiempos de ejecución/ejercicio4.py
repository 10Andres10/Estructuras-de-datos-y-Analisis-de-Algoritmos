import random
import time

tiempo_inicio = time.time()  # Tiempo de inicio

def main():
    n = int(input("Ingrese la cantidad de elementos en el vector: "))
    if n <= 0:
        print("La cantidad de elementos debe ser mayor que 0.")
        return    

    vector = [random.randint(1, 200) for _ in range(n)]
    print("Vector original:", vector)

    vector.sort()  # Ordenar el vector usando el método sort

    tiempo_fin = time.time()  # Tiempo de finalización
    tiempo_transcurrido = tiempo_fin - tiempo_inicio  # Tiempo transcurrido

    print("Vector ordenado:", vector)
    print(f"Tiempo de ejecución: {tiempo_transcurrido:.6f} segundos")

if __name__ == "__main__":
    main()
