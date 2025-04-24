"""
Operadores
"""

# n1 = float(input("Digite el numero 1"))
# n2 = float(input("Digite el numero 2"))

n1 = 5
n2 = 2

print(f"n1: {n1}")
print(f"n2: {n2}")

suma = n1 + n2
print(f"Suma: {suma}")

resta = n1 - n2
print(f"Resta: {resta}")

multiplicacion = n1 * n2
print(f"Multiplicacion: {multiplicacion}")

division = n1 / n2
print(f"Division: {division}")

# Divide y redondea hacia abajo el resultado al entero mas cercano
division_entera = n1 // n2
print(f"Division Entera {division_entera}")

# Residuo de la division
residuo = n1 % n2
print(f"Residuo: {residuo}")

# Potencia
potencia = n1 ** n2
print(f"Potencia: {potencia}")

"""
Orden de precedencia

1. Parentesis
2. Potencias y raices
3. Multiplicaciones y divisiones
4. Suma y restas

1. ()
2. **
3. *, /, //, %
4. +, -
"""
resultado = 3 + 2 * 5
resultado2 = (3 + 2) * 5
print(resultado)
print(resultado2)


"""
Operadores de asignacion
"""
print("\n Suma")
a = 5
print(f"a = {a}")
a = a + 1
print(f"a = a + 1: {a}")
# Es equivalente a 
a = 5
print(f"a = {a}")
a += 1
print(f"a += 1: {a}")

print("\n Resta")
a = 5
print(f"a = {a}")
a = a - 1
print(f"a = a - 1: {a}")
# Es equivalente a 
a = 5
print(f"a = {a}")
a -= 1
print(f"a -= 1: {a}")

print("\n Multiplicacion")
a = 5
print(f"a = {a}")
a = a * 2
print(f"a = a * 2: {a}")
# Es equivalente a 
a = 5
print(f"a = {a}")
a *= 2
print(f"a *= 2: {a}")

print("\n Division")
a = 5
print(f"a = {a}")
a = a / 2
print(f"a = a / 2: {a}")
# Es equivalente a 
a = 5
print(f"a = {a}")
a /= 2
print(f"a /= 2: {a}")

print("\n Division Entera")
a = 5
print(f"a = {a}")
a = a // 2
print(f"a = a // 2: {a}")
# Es equivalente a 
a = 5
print(f"a = {a}")
a //= 2
print(f"a //= 2: {a}")

print("\n Modulo")
a = 5
print(f"a = {a}")
a = a % 2
print(f"a = a % 2: {a}")
# Es equivalente a 
a = 5
print(f"a = {a}")
a %= 2
print(f"a %= 2: {a}")


"""
Operadores de comparacion
"""
n1 = 10
n2 = 1
n3 = 10
print(f"n1: {n1}")
print(f"n2: {n2}")
print(f"n2: {n2}")

# Igual que ==

print(f"n1 == n2: {n1 == n2}")
print(f"n1 == n1: {n1 == n1}")

# Diferente que !=

print(f"n1 != n2 {n1 != n2}")
print(f"n1 != n1 {n1 != n1}")

# Mayor que >

print(f"n1 > n2: {n1 > n2}")
print(f"n1 > n3: {n1 > n3}")

# Mayor o igual que >=

print(f"n1 >= n2: {n1 >= n2}")
print(f"n1 >= n3: {n1 >= n3}")


# Menor que <
print(f"n1 < n2: {n1 < n2}")
print(f"n2 < n1: {n2 < n1}")

# Menor o igual que <=
print(f"n1 <= n2: {n1 <= n2}")
print(f"n2 <= n1: {n2 <= n1}")
print(f"n1 <= n3: {n1 <= n3}")

"""
Operadores logicos
"""

print(" ======== Operadores logicos ======== ")
n1 = 10
n2 = 1
n3 = 10
print(f"n1: {n1}")
print(f"n2: {n2}")
print(f"n3: {n3}")

# Y - and

print(f"n1 > n2 and n1 == n3: {n1 > n2 and n1 == n3}")
print(f"n1 > n2 and n1 == n2: {n1 > n2 and n1 == n2}")
print(f"n1 >= n3 and n1 >= n2: {n1 >= n3 and n1 >= n2}")

# O - or
print("\n == or ==")
print(f"n1 > n2 or n1 == n3: {n1 > n2 or n1 == n3}")
print(f"n1 > n2 or n1 == n2: {n1 > n2 or n1 == n2}")
print(f"n1 > n3 or n1 >= n2: {n1 > n3 or n1 >= n2}")

# Negacion no - not
print("\n == Negacion no - not ==")
print(f"not(n1 > n2 and n1 == n3): {not(n1 > n2 and n1 == n3)}")
print(f"not(n1 > n2 and n1 == n2): {not(n1 > n2 and n1 == n2)}")
print(f"not(n1 >= n3 and n1 >= n2): {not(n1 >= n3 and n1 >= n2)}")

"""
Colecciones

Listas
Tuplas
Conjuntos
Diccionarios
"""

# Listas

"""
Pueden tener elementos del mismo tipo, o de diferentes tipos
"""
print(" == Colecciones ==")
print(" == Listas == ")
frutas = ["naranja", "papaya", "mango", 1, 2, 3.1416, True, [1, 2, 3]]

print(f"len(frutas): {len(frutas)}")

print(f"frutas[2]: {frutas[2]}")
print(f"frutas[1:3]: {frutas[1:3]}")
print(f"frutas[-1]: {frutas[-1]}")
print(f"frutas[-1][1]: {frutas[-1][1]}")

print(f"frutas: {frutas}")
# Agrega al final
frutas.append("test")
print(f"frutas.append(\"test\")")
print(f"frutas: {frutas}\n")

# Puedo decir donde lo quiero agregar

frutas.insert(1, "piña")
print(f"frutas.insert(1, \"piña\") -> frutas: {frutas}")


frutas2 = frutas.copy()
print(f"\nfrutas2: {frutas2}")
# Es frutas2 = frutas.copy() es diferente a:

print(f"\nfrutas: {frutas}")
frutas3 = frutas
frutas3.append(22) 
print(f"frutas: {frutas}")

print(f"\nfrutas.count(\"mango\"): {frutas.count("mango")}")

# Extend es diferente a append

nueva = [3, 2, 1]
respaldo = frutas.copy()
print(f"\nfrutas: {frutas}")

frutas.append(nueva)
print(f"frutas: {frutas}")

frutas = respaldo.copy()
print(f"frutas: {frutas}")

frutas.extend(nueva)
print(f"frutas: {frutas}")

print(f"\frutas.index(\"mango\"): {frutas.index("mango")}")

print(" == pop() == ")
# Si especificas te saca la ultima, si no te saca el elemento en la posicion
print(f"\nfrutas: {frutas}")
frutas.pop()
print(f"frutas: {frutas}")
frutas.pop(0)
print(f"frutas: {frutas}")

numeros = [4, 5, 2, 4, 6, 3, 1]
print(f"numeros: {numeros}")
# No puede ordenar textos y numeros a la vez
numeros.sort()
print(f"numeros: {numeros}")
numeros.sort(reverse=True)
print(f"numeros: {numeros}")
palabras = ["a", "c", "d", "e"]
palabras.sort()
print(f"palabras: {palabras}")

print(sorted("This is a test string from Andrew".split(), key=str.casefold))

"""
Tuplas

Elementos repetidos
Es inmutable
Mas restricciones
"""

print(" == Tuplas == ")

frutas = ("naranjas", 'peras', 'manzanas')
print(f"\nfrutas: {frutas}")

print(f"frutas.count(\"peras\"): {frutas.count("peras")}")

print(f"frutas.index(\"manzana\"): {frutas.index("manzanas")}")

print("\n == Eliminar un elemento == ")

print("\nCasteo a una list, elimino el elemento de la lista")
print("Luego casteo la lista a tupla\n")

print(f"frutas: {frutas}")
copia = list(frutas)
copia.remove("manzanas")
print(f"copia: {copia}")
frutas = tuple(copia)
print(f"frutas: {frutas}")


"""
Conjuntos

No puede tener elementos repetidos
No son ordenados, no hay posiciones
"""

print("\n == Conjuntos == ")

frutas = {"manzana", "naranja", "peras", "naranja"}
print(f"frutas: {frutas}")
print(f"len(frutas): {len(frutas)}")

frutas.add("uva")
print(f"frutas: {frutas}")

copia = frutas.copy()
copia.add("patilla")
print(f"copia: {copia}")

frutas = {"manzana", "naranja", "peras", "naranja"}
print(f"\nfrutas: {frutas}")

carros = {"chevrolet", "ford", "peras", "mazda"}
print(f"carros: {carros}")

print("\n")
# Resta
print(f"frutas.difference(carros): {frutas.difference(carros)}")
print(f"frutas.intersection(carros): {frutas.intersection(carros)}")
print(f"frutas.union(carros): {frutas.union(carros)}")
print(f"\nfrutas: {frutas}")
frutas.discard("naranja")
print(f"\nfrutas: {frutas}")

