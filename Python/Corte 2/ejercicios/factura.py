import json

# Leer los datos de la empresa desde "empresa.txt"
with open("empresa.txt", "r") as empresa_file:
    empresa_data = empresa_file.read()

# Leer los datos del cliente desde un diccionario
cliente_data = {

    "Nombre": "Andrés López",
    "Direccion": "Roads Untraveled",
    "Cédula": "1005542832"
    
}

# Leer los datos de los productos desde un diccionario
productos_data = {

    "001": {"nombre": " Gaseosa    ", "precio": 4500},
    "002": {"nombre": " Pan        ", "precio": 3000},
    "003": {"nombre": " Cerveza    ", "precio": 2500},
    "004": {"nombre": " Gomitas    ", "precio": 1500},
    "005": {"nombre": " Chocolatina", "precio": 4000}

}

# Calcular el total de la venta
total_venta = sum(
    producto["cantidad"] * producto["precio_unitario"]
    for producto in productos_data.values()
)

# Crear la factura de venta
factura = f"""
{empresa_data}

Fecha: Fecha de la factura
Nombre del Cliente: {cliente_data['nombre']}
Dirección del Cliente: {cliente_data['direccion']}
Cédula de Ciudadania: {cliente_data['cedula']}

Detalles de la venta:
{"Código":<10}{"Nombre":<20}{"Cantidad":<10}{"Precio Unitario":<15}{"Precio Total":<15}
{'-'*70}
"""

# Agregar detalles de productos con saltos de línea
factura += "".join(
    [f"{codigo:<10}{producto['nombre'][:20]:<20}{producto['cantidad']:<10}{producto['precio_unitario']:<15}${producto['cantidad']*producto['precio_unitario']:.2f}\n" for codigo, producto in productos_data.items()]
)

factura += f"{'-'*70}\nTotal de la venta: ${total_venta:.2f}"

# Guardar la factura en un archivo
with open("factura.txt", "w") as factura_file:
    factura_file.write(factura)

# Calcular el total de la venta
total_venta = sum(
    producto["cantidad"] * producto["precio_unitario"]
    for producto in productos_data.values()
)

# Calcular el monto del IVA (19% del total de la venta)
iva = total_venta * 0.19

#Mostrar cuanto iva se le cobra por cada producto
for codigo, producto in productos_data.items():
    iva_producto = producto["cantidad"] * producto["precio_unitario"] * 0.19
    print(f"El Iva que se le cobro a {codigo}: {iva_producto}")    

# Crear la factura de venta
factura = f"""
{empresa_data}  

Fecha: Fecha de la factura
Nombre del Cliente: {cliente_data['nombre']}
Dirección del Cliente: {cliente_data['direccion']}
Cédula de Ciudadanía: {cliente_data['cedula']}

Detalles de la venta:
{"Código":<10}{"Nombre":<20}{"Cantidad":<10}{"Precio Unitario":<15}{"Precio Total":<15}
{'-'*70}
"""

# Agregar detalles de productos con saltos de línea
factura += "".join(
    [f"{codigo:<10}{producto['nombre'][:20]:<20}{producto['cantidad']:<10}{producto['precio_unitario']:<15}${producto['cantidad']*producto['precio_unitario']:.2f}\n" for codigo, producto in productos_data.items()]
)

factura += f"{'-'*70}\nTotal de la venta: ${total_venta:.2f}\n"
factura += f"IVA (19%): ${iva:.2f}\n"
factura += f"Total de la venta con IVA: ${total_venta + iva:.2f}"

# Guardar la factura en un archivo
with open("factura.txt", "w") as factura_file:
    factura_file.write(factura)
