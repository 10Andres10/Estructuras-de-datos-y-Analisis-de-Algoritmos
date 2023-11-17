import os

# Diccionario de asignación de datáfonos
diccionario_datáfonos = {
    "001": "Establecimiento1",
    "002": "Establecimiento2",
    # Añade más datáfonos según sea necesario
}

# Diccionario de asignación de tarjetas
diccionario_tarjetas = {
    "1234567890123456": "CuentaCliente1",
    "9876543210987654": "CuentaCliente2",
    "2345678901234567": "CuentaCliente3",
    # Se pueden añadir más tarjetas según sea necesario
}

def calcular_comision(valor_compra):
    if valor_compra <= 100000:
        return valor_compra * 0.005
    elif 100001 <= valor_compra <= 1000000:
        return valor_compra * 0.004
    else:
        return valor_compra * 0.01

def procesar_transacciones(archivo):
    # Obtener la ruta del directorio actual
    directorio_actual = os.path.dirname(os.path.abspath(__file__))

    # Construir la ruta completa al archivo transacciones.txt
    ruta_archivo = os.path.join(directorio_actual, archivo)

    with open(ruta_archivo, 'r') as file:
        for linea in file:
            datos_transaccion = linea.strip().split(',')
            numero_tarjeta = datos_transaccion[0]
            valor_compra = float(datos_transaccion[1])
            codigo_datáfono = datos_transaccion[2]

            comision = calcular_comision(valor_compra)
            total_pagar = valor_compra - comision

            establecimiento = diccionario_datáfonos[codigo_datáfono]
            cuenta_cliente = diccionario_tarjetas[numero_tarjeta]

            tupla_establecimiento = (establecimiento, comision, total_pagar)
            tupla_banco_cliente = (cuenta_cliente, valor_compra)

            print("Establecimiento:", tupla_establecimiento)
            print("Banco del cliente:", tupla_banco_cliente)
            print()

# Procesar transacciones y generar tuplas
procesar_transacciones('transacciones.txt')