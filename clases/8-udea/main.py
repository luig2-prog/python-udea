"""
Ciclo while
"""


print(" =========== Ciclo while ===========")

a = 1

while a <= 10:
    print(a)
    a += 1

print("Ciclo while")

a = 1
while a <= 10:
    print(a * 5)
    a += 1


print("Fin del ciclo while")


frutas = ["naranja", "papaya", "mango", 1, 2, 3.1416, True, [1, 2, 3]]
print(f"len(frutas): {len(frutas)}")

i = 0
while i < len(frutas):
    print(f"frutas: {frutas[i]}")
    i += 1

"""
Ejercicio: Sistema de Inventario de una Tienda
Objetivo: Crear un programa que permita gestionar el inventario de una tienda, donde los usuarios puedan:

Agregar productos

Buscar productos

Mostrar todos los productos

Salir del programa

Requisitos:
Diccionario para almacenar cada producto con su nombre, precio y cantidad.
Ejemplo: {"nombre": "Manzana", "precio": 0.5, "cantidad": 10}

Lista para guardar todos los productos del inventario.

Menú interactivo con while y condicionales (if-elif-else).Ejercicio: Sistema de Inventario de una Tienda
Objetivo: Crear un programa que permita gestionar el inventario de una tienda, donde los usuarios puedan:

Agregar productos

Buscar productos

Mostrar todos los productos

Salir del programa

Requisitos:
Diccionario para almacenar cada producto con su nombre, precio y cantidad.
Ejemplo: {"nombre": "Manzana", "precio": 0.5, "cantidad": 10}

Lista para guardar todos los productos del inventario.

Menú interactivo con while y condicionales (if-elif-else).
"""

productos = []

def agregarProducto(producto):
    productos.append(producto)

def buscarProducto(productoBuscar: str):
    for producto in productos:
        if str(producto["nombre"]).lower() == productoBuscar.lower():
            temp = producto
            return producto
    return None

def mostrarProductos():
    if len(productos) <= 0:
        print("No hay productos")
        return
    for producto in productos:
        printProducto(producto)

def printProducto(producto):
    print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

opcion = -1


while opcion != 4:

    print("\n ================================================== ")
    print(" ====== Sistema de Inventario de una Tienda ======= ")
    print(" ====================== Menu ====================== ")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Mostrar todos los productos")
    print("4. Salir\n")

    opcion = int(input())

    if opcion == 1:
        nombre = str(input("Ingrese el nombre del producto: "))
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        producto = { "nombre": nombre, "precio": precio, "cantidad": cantidad }
        agregarProducto(producto)
        print("\nProducto agregado!")
    elif opcion == 2:
        nombre = str(input("Ingrese el nombre del producto a buscar: "))
        producto = buscarProducto(nombre)
        if producto != None:
            print("\nEl producto encontrado es: ")
            printProducto(producto)
        else:
            print("No existe el producto")
    elif opcion == 3:
        print("\nLos productos son: ")
        mostrarProductos()

    elif opcion == 4:
        print("Gracias por usar el software!")
    else:
        print("No seleccionón una opción valida")

