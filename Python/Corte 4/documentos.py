from datetime import datetime, timedelta

# Función para inicializar las conexiones y distancias entre oficinas
def inicializar_conexiones():
    conexiones = {
        'A': [('C', 1), ('B', 3)],
        'B': [('A', 3), ('G', 5), ('D', 1)],
        'C': [('A', 1), ('F', 5)],
        'D': [('B', 1)],
        'E': [('H', 2), ('G', 5)],
        'F': [('C', 5), ('H', 3)],
        'G': [('E', 5), ('B', 5)],
        'H': [('F', 3), ('E', 1)]
    }
    return conexiones

# Función para obtener rutas posibles entre dos oficinas
def obtener_rutas(conexiones, inicio, fin, ruta_actual=[]):
    ruta_actual = ruta_actual + [inicio]
    if inicio == fin:
        return [ruta_actual]
    if inicio not in conexiones:
        return []
    rutas = []
    for conexion in conexiones[inicio]:
        oficina, distancia = conexion
        if oficina not in ruta_actual:
            nuevas_rutas = obtener_rutas(conexiones, oficina, fin, ruta_actual)
            for ruta in nuevas_rutas:
                rutas.append(ruta)
    return rutas

# Función para calcular la distancia total de una ruta
def calcular_distancia_total(conexiones, ruta):
    distancia_total = 0
    for i in range(len(ruta) - 1):
        oficina_actual = ruta[i]
        oficina_siguiente = ruta[i + 1]
        distancias = [d for o, d in conexiones[oficina_actual] if o == oficina_siguiente]
        if distancias:
            distancia_total += distancias[0]
    return distancia_total

# Función para agregar una solicitud al archivo
def agregar_solicitud(archivo_solicitudes):
    while True:
        destino = input("Ingrese el destino final del documento (o 'salir' para terminar): ")
        if destino.lower() == 'salir':
            break

        identificacion = input("Ingrese la identificación del documento: ")
        solicitante = input("Ingrese el nombre del solicitante: ")

        # Verificar si ya hay una factura para el usuario
        with open(archivo_solicitudes, 'a+') as file:
            file.seek(0)
            lineas = file.readlines()
            encontrado = False
            for i, linea in enumerate(lineas):
                if identificacion in linea:
                    lineas[i] = f"{destino},{identificacion},{solicitante}\n"
                    encontrado = True
                    break

            if not encontrado:
                lineas.append(f"{destino},{identificacion},{solicitante}\n")

            # Sobrescribir el archivo
            file.seek(0)
            file.writelines(lineas)

        print("Solicitud agregada correctamente.")

# Resto del código anterior...

def main():
    archivo_solicitudes = "solicitudes_desarrollar.txt"
    duracion_documentos = {}
    solicitudes_por_oficina = {}
    solicitudes_por_usuario = {}
    conexiones_oficinas = inicializar_conexiones()

    while True:
        print("\nMenú de opciones:")
        print("1. Agregar archivo")
        print("2. Calcular total de días requeridos para todos los documentos")
        print("3. Generar estadística de documentos requeridos por oficina")
        print("4. Generar estadística de solicitudes por usuario")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_solicitud(archivo_solicitudes)
        elif opcion == "2":
            total_dias = calcular_total_dias(duracion_documentos)
            print(f"Total de días requeridos para todos los documentos: {total_dias} días")
        elif opcion == "3":
            generar_estadisticas(duracion_documentos, solicitudes_por_oficina, solicitudes_por_usuario)
        elif opcion == "4":
            generar_estadisticas(duracion_documentos, solicitudes_por_oficina, solicitudes_por_usuario)
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

def mostrar_rutas(conexiones_oficinas):
    inicio = input("Ingrese la oficina de inicio: ")
    fin = input("Ingrese la oficina de destino: ")

    rutas_posibles = obtener_rutas(conexiones_oficinas, inicio, fin)
    
    if rutas_posibles:
        print(f"Rutas posibles entre {inicio} y {fin}:")
        for i, ruta in enumerate(rutas_posibles, start=1):
            print(f"Ruta {i}: {', '.join(ruta)}")
    else:
        print(f"No hay rutas posibles entre {inicio} y {fin}.")

def calcular_distancia_ruta(conexiones_oficinas):
    ruta_str = input("Ingrese la ruta (oficinas separadas por comas, por ejemplo, A,B,C): ")
    ruta = ruta_str.split(',')

    distancia_total = calcular_distancia_total(conexiones_oficinas, ruta)

    if distancia_total > 0:
        print(f"La distancia total de la ruta {ruta_str} es: {distancia_total} metros.")
    else:
        print(f"No se pudo calcular la distancia total de la ruta {ruta_str}.")

if __name__ == "__main__":
    main()
