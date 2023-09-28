import random
import time

# Obtener la cantidad de números del usuario
N = int(input("Digite la cantidad de números: "))

# Generar N números aleatorios entre 1 y 1000 y almacenarlos en un vector
vector = []
tiempos_generacion = []  # Lista para almacenar los tiempos de generación

for _ in range(N):
    tiempo_inicio = time.time()  # Capturar el tiempo de inicio de generación
    num = random.randint(1, 1000)
    tiempo_fin = time.time()  # Capturar el tiempo de final de generación
    vector.append(num)
    tiempos_generacion.append(tiempo_fin - tiempo_inicio)  # Almacenar el tiempo de generación
    print(f"Número generado: {num} (Tiempo de generación: {tiempo_fin - tiempo_inicio:.6f} segundos)")

# Contar la cantidad de números pares
numeros_pares = 0
for num in vector:
    if num % 2 == 0:
        numeros_pares += 1

# Calcular el porcentaje de números pares
porcentaje_pares = (numeros_pares / N) * 100

print(f"Porcentaje de números pares: {porcentaje_pares}%")

# Calcular el tiempo total de generación
tiempo_total_generacion = sum(tiempos_generacion)
print(f"Tiempo total de generación: {tiempo_total_generacion:.6f} segundos")
