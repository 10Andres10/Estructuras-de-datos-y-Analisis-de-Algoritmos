menu()
can_pro = int(input("Digite cantidad de productos a facturar: "))

# Validación de información correcta
while can_pro <= 0:
    print("Cantidad incorrecta, debe ser mayor a 0")
    can_pro = int(input("Digite cantidad de productos a facturar: "))

for i in range (can_pro):
    cod_pro = int(input("Digíte el código del producto a facturar: "))
    while cod_pro not in codigos:
        print("El código no está en la lista")
        cod_pro = int(input("Digíte el código del producto a facturar: "))
        
