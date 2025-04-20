# Comentarios de una línea

"""
Comentario en múltiples líneas
Othe line
"""

print('Luis "Software Enginner" Hernandez')

print("Luis 'Software Enginner' Hernandez")

# Tipos de datos - Básicos

"""
Numericos: que pueden ser enteros (int) o decimales (float)

Cadenas: (string o str)

Booleanos: True (verdadero) o False (falso)
"""

# Variable de tipo numerico

"""
Nombres de variables
No pueden empezar por numero
Puede contener en su nombre solo el caracter especial  _

Python es de tipado dinámico, el tipo de variable puede cambiar
"""

# Entero
a = 5
# Decimal
b = 3.1416

print(a)
print(type(a))


# Las variables deben ser coherente el nombre con su contenido o tipo de dato

age = 19
PI = 3.14
name = "Luis"
married = False
print(type(married))
print(PI)


# Tipado dinámico

dato = 19.3
print(dato)
print(type(dato))

dato = "Luis"
print(dato)
print(type(dato))

dato = 12
print(dato)
print(type(dato))

print()
print("========== Operadores aritméticos ==========")

"""
Operadores aritméticos
suma: +
resta: -
multiplicacion: * 
Division: *
"""

"""
f-string (formatted string literals): Forma moderna y legible de formatear cadenas de texto
1. La 'f' antes de las comillas indican que es un f-string
2. Las llaves {} se utilizan para interpolar variables o expresiones
"""

number1 = 9
number2 = 3

suma = number1 + number2
print("El resultado de la suma es: ", suma)
print(f"{number1} + {number2} = {suma}")
print()

resta = number1 - number2
print("El resultado de la resta es: ", resta)
print(f"{number1} - {number2} = {resta}")
print()

multiplicacion = number1 * number2
print(f"{number1} * {number2} = {multiplicacion}")
print("El resultado de la multiplicacion es: ", multiplicacion)
print()

division = number1 / number2
print(f"{number1} / {number2} = {division}")
print("El resultado de la division es: ", division)
print()

print(suma, resta, multiplicacion, division)

print()
print("========== input ==========")

"""
input: Permite obtener datos del usuario por teclado o consola
Se almacena como cadena de texto

Para convertir a otro tipo de dato se utiliza:
int()
float()
str()
bool()
"""

n1 = input("Ingrese el primer numero: ")
n2 = input("Ingrese el segundo numero: ")

"""
Se puede usar tambien:
n1 = int(input("Texto"))
Con recibir el texto y convertirlo a entero

"""

concatenacion = n1 + n2
print("El resultado de la concatenacion es: ", concatenacion)

suma = int(n1) + int(n2)
print("El resultado de la suma es: ", suma)

resta = int(n1) + int(n2)
print("El resultado de la resta es: ", resta)

multiplicacion = int(n1) * int(n2)
print("El resultado de la multiplicacion es: ", multiplicacion)

division = int(n1) + int(n2)
print("El resultado de la division: ", division)

