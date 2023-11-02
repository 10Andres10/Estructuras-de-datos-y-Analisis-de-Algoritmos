# Función para obtener el nombre del conductor con mayor recorrido.
def conductor_mayor_recorrido(conductores):
    max_recorrido = 0
    nombre_conductor = ""
    for conductor in conductores:
        if conductor["kilometraje_total"] > max_recorrido:
            max_recorrido = conductor["kilometraje_total"]
            nombre_conductor = conductor["nombre"]
    return nombre_conductor

# Función para obtener el nombre del conductor con mayor kilometraje promedio diario.
def conductor_mayor_promedio(conductores):
    max_promedio = 0
    nombre_conductor = ""
    for conductor in conductores:
        promedio_diario = conductor["kilometraje_total"] / conductor["viajes"]
        if promedio_diario > max_promedio:
            max_promedio = promedio_diario
            nombre_conductor = conductor["nombre"]
    return nombre_conductor

# Función para calcular el total de viajes generados en la empresa.
def total_viajes(conductores):
    total = 0
    for conductor in conductores:
        total += conductor["viajes"]
    return total

# Inicializar la lista de conductores
conductores = []

n = int(input("Ingrese el número de conductores: " ))

# Capturar los datos de cada conductor
for i in range(n):
    nombre = input(f"Ingrese el nombre del conductor {i + 1}: ")
    viajes = int(input(f"Ingrese el número de viajes diarios de {nombre}: "))
    kilometraje_total = float(input(f"Ingrese el kilometraje total de {nombre}: "))
    
    conductor = {
        "nombre": nombre,
        "viajes": viajes,
        "kilometraje_total": kilometraje_total
    }
    
    conductores.append(conductor)

# Menú de opciones
while True:
    print("\nMenú de opciones:")
    print("1. Mostrar conductor con mayor recorrido")
    print("2. Mostrar conductor con mayor kilometraje promedio diario")
    print("3. Generar el total de viajes generados en la empresa")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre_mayor_recorrido = conductor_mayor_recorrido(conductores)
        print(f"El conductor con mayor recorrido es: {nombre_mayor_recorrido}")

    elif opcion == "2":
        nombre_mayor_promedio = conductor_mayor_promedio(conductores)
        print(f"El conductor con mayor kilometraje promedio diario es: {nombre_mayor_promedio}")

    elif opcion == "3":
        total = total_viajes(conductores)
        print(f"El total de viajes generados en la empresa es: {total}")

    elif opcion == "4":
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
