# Plantilla del recibo

plantilla = """
    DATOS Y PROCESOS CORPORATIVOS LTDA

Facturas de ventas Nro. 10      Fecha: {fecha}
       Nit: 890090200-1 Regimen Comun
    Cliente: {codigo_cliente} - {nombre_cliente}

|Codigo |Nombre  |Cantidad|Vlr Unit|%Iva |Iva  |Vlr Total |
|{cod_producto}    |{nombre_producto}    |  {cantidad_producto}     |  {precio_unidad}  |  {iva} | {ivaTotal} | {valor_Total} |

                    Subtotal: $3000
                    Total Iva: $300
                    Total Venta: $3300

"""
# Diccionario de elementos de la canasta basica
# Leer los datos de los productos desde un diccionario

productos_data = {
    "001" : {"nombre": "Gaseosa    ", "precio_unitario": 4500, "porcentaje_iva": (15)},
    "002" : {"nombre": "Pan        ", "precio_unitario": 3000, "porcentaje_iva": (35)},
    "003" : {"nombre": "Cerveza    ", "precio_unitario": 2500, "porcentaje_iva": (25)},
    "004" : {"nombre": "Gomitas    ", "precio_unitario": 1500, "porcentaje_iva": (5) },
    "005" : {"nombre": "Chocolatina", "precio_unitario": 4000, "porcentaje_iva": (45)},
}

# Datos pedidos

fecha = input("Ingrese la fecha actual: ")
cliente_codigo = input("Ingrese la cedula del Cliente: ")
cliente_nombre = input("Ingrese el nombre del Cliente: ")
codigo_producto = input("Ingrese el código del producto: ")
if codigo_producto in productos_data:
    producto = productos_data[codigo_producto]
    nombre_producto = producto['nombre']
    precio_unidad = producto['precio_unitario']
    porcentaje_iva = producto['porcentaje_iva']
else:
    print("No se encontro el codigo del producto que digitaste.")

cantidad_producto = int(input("Ingrese la cantidad del producto: "))
if cantidad_producto > 1:
    valor_total = precio_unidad * cantidad_producto
else:
    valor_total = precio_unidad

# Calcular el iva

iva = float(porcentaje_iva) / 100
valor_total = float(cantidad_producto) * float(precio_unidad)
iva_total = valor_total * iva

datos_factura = {
    "fecha": fecha,
    "codigo_cliente": cliente_codigo,
    "nombre_cliente": cliente_nombre,
    "cod_producto": codigo_producto,
    "nombre_producto": nombre_producto,
    "cantidad_producto": cantidad_producto,
    "precio_unidad": precio_unidad,
    "iva": porcentaje_iva,
    "ivaTotal": iva_total,
    "valor_Total": valor_total
}

factura_generada = plantilla.format(**datos_factura)

ruta_archivo = "facturaFinal.txt"
with open(ruta_archivo, "w") as archivo:
    archivo.write(factura_generada)