import random
import time

# Medir el tiempo al inicio
tiempo_inicio = time.time()

cantidad_numeros = int(input("Ingrese la cantidad de números a generar y ordenar: "))

vector = []

# Generar números en 5 ciclos diferentes
for _ in range(5):
    for i in range(cantidad_numeros):
        if _ == 0:
            vector.append(random.randint(1, 400))            
        elif _ == 1:
            vector.append(random.randint(401, 800))
        elif _ == 2:
            vector.append(random.randint(801, 1200))
        elif _ == 3:
            vector.append(random.randint(1201,1600))
        else:
            vector.append(random.randint(1601, 2000))
            

print("Vector antes de ordenar:")
print(vector)

# Método burbuja para ordenar el vector
for i in range(cantidad_numeros * 5):
    for j in range(cantidad_numeros * 5 - i - 1):
        if vector[j] > vector[j+1]:
            vector[j], vector[j+1] = vector[j+1], vector[j]

# Medir el tiempo al final
tiempo_final = time.time()

print("Vector después de ordenar:")
print(vector)

# Calcular el tiempo de ejecución
tiempo_ejecucion = tiempo_final - tiempo_inicio
print("Tiempo de ejecución:", tiempo_ejecucion, "segundos")