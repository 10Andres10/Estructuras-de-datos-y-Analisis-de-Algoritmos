def leer_transacciones(nombre_archivo):
    transacciones = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            codigo, apellidos, nombres, creditos = linea.strip().split(',')
            transacciones.append((codigo, apellidos, nombres, int(creditos)))
    return transacciones

def main():
    archivo = "estudiantes.txt"  # Reemplaza con el nombre de tu archivo de transacciones
    transacciones = leer_transacciones(archivo)

    # Calcular el promedio de créditos matriculados
    total_creditos = sum(transaccion[3] for transaccion in transacciones)
    promedio_creditos = total_creditos / len(transacciones)

    # Encontrar estudiantes con más créditos que el promedio
    estudiantes_mayor_promedio = [(apellidos, nombres, creditos) for codigo, apellidos, nombres, creditos in transacciones if creditos > promedio_creditos]

    # Mostrar el resultado en una tupla
    resultado = (len(estudiantes_mayor_promedio), estudiantes_mayor_promedio)
    print("Número de estudiantes con más créditos que el promedio:", resultado)

if __name__ == "__main__":
    main()
