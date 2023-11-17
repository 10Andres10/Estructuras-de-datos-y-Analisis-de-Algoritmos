import json

# Leer los datos de la empresa desde "empresa.txt"
with open("empresa.txt", "r") as empresa_file:
    empresa_data = empresa_file.read()

# Leer los datos del cliente desde un diccionario
cliente_data = {
    "nombre": "Chester Bennigton",
    "direccion": "Roads Untraveled",
    "cedula": "1100999323"
}

# Leer los datos de los productos desde un diccionario
productos_data = {
    "001": {"nombre": "Pezuña", "cantidad": 2, "precio_unitario": 10.00},
    "002": {"nombre": "Arepa", "cantidad": 3, "precio_unitario": 15.00},
    "003": {"nombre": "Webo", "cantidad": 1, "precio_unitario": 5.00}
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
factura += f"Total de la venta con IVA: ${total_venta + iva:.2f}\n"
factura += f"Gracias por su compra ctrm!"
# Guardar la factura en un archivo
with open("factura.txt", "w") as factura_file:
    factura_file.write(factura)


print("Factura de venta generada exitosamente en 'factura.txt'")