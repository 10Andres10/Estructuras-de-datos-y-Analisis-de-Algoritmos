import os

# Actualizar diccionario
traductor = {}
archivo = "corrector.txt"

if os.path.exists(archivo):
    with open(archivo, "r") as f:
        lineas = f.readlines()
        for linea in lineas:
            lista = linea.strip().split(":")
            if len(lista) == 2:
                palabra_correcta = lista[0]
                palabras_incorrectas = lista[1].split(",")
                traductor[palabra_correcta] = palabras_incorrectas

# Solicitar al usuario una frase
frase_usuario = input("Ingresa una frase: ")

# Dividir la frase en palabras
palabras = frase_usuario.split()

# Verificar y corregir las palabras
nueva_frase = []
for palabra in palabras:
    palabra_corregida = traductor.get(palabra, [palabra])
    print(f"¿Qué palabra prefieres para '{palabra}'?")
    for i, correccion in enumerate(palabra_corregida):
        print(f"{i + 1}: {correccion}")

    eleccion = input("Selecciona una opción (0 para mantener la palabra): ")
    if eleccion.isdigit():
        eleccion = int(eleccion)
        if 0 < eleccion <= len(palabra_corregida):
            palabra = palabra_corregida[eleccion - 1]
    nueva_frase.append(palabra)

# Mostrar la nueva frase corregida
frase_corregida = " ".join(nueva_frase)
print("Frase corregida:", frase_corregida)
