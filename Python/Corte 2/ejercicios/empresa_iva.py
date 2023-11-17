# Definimos el diccionario de productos con código, nombre y precio
productos = {
    "001": {"nombre": " Gaseosa    ", "precio": 4500},
    "002": {"nombre": " Pan        ", "precio": 3000},
    "003": {"nombre": " Cerveza    ", "precio": 2500},
    "004": {"nombre": " Gomitas    ", "precio": 1500},
    "005": {"nombre": " Chocolatina", "precio": 4000}
}

# Función para calcular el total con IVA
def calcular_total(subtotal):
    iva = subtotal * 0.19
    total = subtotal + iva
    return total

# Inicializamos las variables para la factura
factura = {}
subtotal = 0.0

# Mostramos el menú de productos
print("Menú de productos:")
print("Código  Nombre        Precio")
for codigo, producto in productos.items():
    print(f"{codigo}    {producto['nombre']}    ${producto['precio']}")

# Validación de la cantidad de productos a facturar (de 1 a 5 productos)
def menu():
    can_pro = int(input("Digite cantidad de productos a facturar (de 1 a 5): "))
    while can_pro < 1 or can_pro > 5:
        print("Cantidad incorrecta, debe estar entre 1 y 5.")
        can_pro = int(input("Digite cantidad de productos a facturar (de 1 a 5): "))
    return can_pro


# Proceso de compra
can_pro = menu()

for i in range(can_pro):
    codigos = list(productos.keys())
    cod_pro = input("Digite el código del producto a facturar: ")
    
    while cod_pro not in codigos:
        print("El código no está en la lista")
        cod_pro = input("Digite el código del producto a facturar: ")
    
    cantidad = int(input("Ingrese la cantidad a comprar: "))
    
    if cantidad > 0:
        precio_unitario = productos[cod_pro]["precio"]
        total_producto = precio_unitario * cantidad
        subtotal += total_producto
        factura[cod_pro] = {"nombre": productos[cod_pro]["nombre"], "cantidad": cantidad, "total": total_producto}
    else:
        print("La cantidad debe ser mayor que cero.")

# Mostramos la factura
print("\nFactura de compra:")
print("Código  Nombre        Cantidad  Total")
for codigo, detalle in factura.items():
    print(f"{codigo}    {detalle['nombre']}    {detalle['cantidad']}        ${detalle['total']}")

# Calculamos el total con IVA
total_con_iva = calcular_total(subtotal)
print(f"\nSubtotal: ${subtotal}")
print(f"Total con IVA (19%): ${total_con_iva}")
