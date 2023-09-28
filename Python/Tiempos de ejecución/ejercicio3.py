import random
import time

# Función para generar números aleatorios en un rango dado
def generate_numbers(start, end, count):
    return [random.randint(start, end) for _ in range(count)]

# Obtener la cantidad de números del usuario
n = int(input("Digite la cantidad de números: "))

# Definir los rangos para los ciclos
ranges_cycle_1 = [(1, n//5), (n//5 + 1, 2*n//5), (2*n//5 + 1, 3*n//5), (3*n//5 + 1, 4*n//5), (4*n//5 + 1, n)]
ranges_cycle_2 = list(reversed(ranges_cycle_1))

# Realizar 3 ejecuciones y medir el tiempo promedio de generación
num_executions = 3
avg_generation_times = []

for _ in range(num_executions):
    total_generation_time = 0

    for start, end in ranges_cycle_1 + ranges_cycle_2:
        start_time = time.time()
        generate_numbers(start, end, n)
        end_time = time.time()
        execution_time = end_time - start_time
        total_generation_time += execution_time

    avg_generation_time = total_generation_time / (len(ranges_cycle_1) + len(ranges_cycle_2))
    avg_generation_times.append(avg_generation_time)

# Calcular el promedio de los tiempos de generación
average_generation_time = sum(avg_generation_times) / num_executions

print(f"Tiempo promedio de generación para {n} números: {average_generation_time} segundos")

# Generar el vector
vector = []
for start, end in ranges_cycle_1:
    vector.extend(generate_numbers(start, end, n//5))
for start, end in ranges_cycle_2:
    vector.extend(generate_numbers(start, end, n//5))
    
# Función para ordenar un vector utilizando el método de burbuja
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Realizar 3 ejecuciones y medir el tiempo promedio de ordenación
avg_sorting_times = []

for _ in range(num_executions):
    vector_copy = vector.copy()
    start_time = time.time()
    bubble_sort(vector_copy)
    end_time = time.time()
    execution_time = end_time - start_time
    avg_sorting_times.append(execution_time)

# Calcular el promedio de los tiempos de ordenación
average_sorting_time = sum(avg_sorting_times) / num_executions

print(f"Tiempo promedio de ordenación: {average_sorting_time} segundos")
