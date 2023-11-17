def leer_transacciones(archivo):
    transacciones = []
    with open(archivo, 'r') as file:
        for line in file:
            codigo, apellidos, nombres, creditos = line.strip().split(',')
            transacciones.append((codigo, apellidos, nombres, int(creditos)))
    return transacciones

def calcular_promedio_creditos(transacciones):
    total_creditos = sum(transaccion[3] for transaccion in transacciones)
    promedio = total_creditos / len(transacciones)
    return promedio

def estudiantes_con_mas_creditos(transacciones):
    promedio_creditos = calcular_promedio_creditos(transacciones)
    estudiantes_con_mas_creditos = [(codigo, apellidos, nombres, creditos)
                                    for codigo, apellidos, nombres, creditos in transacciones
                                    if creditos > promedio_creditos]
    return len(estudiantes_con_mas_creditos), estudiantes_con_mas_creditos

if __name__ == "__main__":
    archivo_transacciones = "estudiantes.txt"
    transacciones = leer_transacciones(archivo_transacciones)

    cantidad, estudiantes_con_mas_creditos = estudiantes_con_mas_creditos(transacciones)

    resultado = (cantidad, estudiantes_con_mas_creditos)
    print(resultado)