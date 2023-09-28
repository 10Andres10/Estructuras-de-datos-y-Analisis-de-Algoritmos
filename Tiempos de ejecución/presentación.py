import time

def suma_n_numeros(n):
    suma = 0
    for i in range(1, n+1):
        suma += i
    return suma

n = int(input("Digite n: "))  # Cambia el valor de n para ver cómo afecta al tiempo de ejecución

inicio = time.time()
resultado = suma_n_numeros(n)
fin = time.time()

tiempo_ejecucion = fin - inicio

print(f"La suma de los primeros {n} números es {resultado}")
print(f"Tiempo de ejecución: {tiempo_ejecucion} segundos")




