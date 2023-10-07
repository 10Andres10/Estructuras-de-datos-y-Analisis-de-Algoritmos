import random
import time

# Ordenar lista
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[len(lista) // 2]
    left, middle, right = [], [], []
    for x in lista:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)
    return quicksort(left) + middle + quicksort(right)

# Ingresar el numero de pares
def Pares():

    N = int(input("Ingrese la cantidad de números pares a generar: "))
    # Medir el tiempo de ejecución
    inicio_time = time.time()    
    numeros_pares = [random.randint(1, 100) * 2 for _ in range(N)]
    ## print("Números pares generados:", numeros_pares)
    
    # Promedio
    suma = sum(numeros_pares) / len(numeros_pares)
    print("Promedio:", suma)

    # Numeros menores que el promedio
    contar_menores = 0
    for num in numeros_pares:
        if num < suma:
            contar_menores += 1
    print("Cantidad de números menores que el promedio:", contar_menores)



    # Calcular y mostrar el tiempo de ejecución
    fin_time = time.time()
    tiempo = fin_time - inicio_time
    print("Tiempo de ejecución:", tiempo, "segundos")

# Ejecutar la función Pares si este script es el programa principal
if __name__ == "__main__":
    Pares()