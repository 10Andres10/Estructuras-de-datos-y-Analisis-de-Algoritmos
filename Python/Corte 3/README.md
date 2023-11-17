# Problema 14 - Tuplas 
## Se tiene el registro con los datos de una transacción de un cliente a partir de un datáfono en un archivo de texto como lo son: número de tarjeta, valor compra, código datáfono y fecha. Determinar el valor a cobrar por la comisión del manejo de la transacción de acuerdo a la siguiente tabla y generar las tuplas para los servicios de la transacción:

##     Rango               Comisión
## 0 - 100.000               0.5%
## 100.001 - 1.000.000       0.4%
## > 1.000.000                1%

## Como respuesta se deben generar 2 tuplas, una para el establecimiento con los datos del código establecimiento (Diccionario de asignacion de datáfonos), valor comisión y neto a pagar. Otra para el banco del cliente con el número de cuenta (Diccionario de asignacion de tarjetas) y el valor de la compra.

# Problema 15 - txt y Jason
## Se tienen los datos de un grupo de 5 transacciones referentes a las matrículas de un grupo de estudiantes (código, apellidos, nombres, créditos), almacenadas como txt, crear un arreglo con estas transacciones y a partir del mismo, calcular cuántos estudiantes y su número de créditos matriculados, tienen un mayor número de créditos matriculados que el promedio de todos los estudiantes; generando esta respuesta en una tupla.