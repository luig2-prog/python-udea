
# print("========== Cadenas de caracteres ==========")

# """
# Cadenas de caracteres: Las cadenas de caracteres son secuencias de caracteres

# capitalize(): Convierte la primera letra de la cadena a mayuscula
# casefold(): Convierte la cadena a minusculas

# """

# cadena = input("Ingrese el nombre: ")
# conMayusculas = cadena.capitalize()
# print("\nEl nombre con la primera letra en mayuscula es: ", conMayusculas)

# todo_en_minuscula = cadena.casefold()
# print("\nTodo en minuscula: ", todo_en_minuscula)

# todo_en_mayuscula = cadena.upper()
# print("\nTodo en mayuscula", todo_en_mayuscula)

# """
# count es case sensitive
# """
# cadena_to_find = input("\nIngrese la letra que quiera contar: ")
# count_a = cadena.count(cadena_to_find)
# print("\nLa '", cadena_to_find, "' aparece ", count_a, " vez/veces")
# print(f"La cadena o caracter '{cadena_to_find}' aparece {count_a} vez/veces")

# """
# Reemplazar cadenas
# replace es case sensitive
# """

# frase = input("\nIngrese una frase: ")
# palabra_a_reemplazar = input("\nIngrese la palabra que quiere reemplazar: ")
# palabra_con_que_reemplazar = input("Ingrese la palabra con la que reemplazará la palabra anterior: ")
# palabra_reemplazada = frase.replace(palabra_a_reemplazar, palabra_con_que_reemplazar)
# print(f"\nLa palabra {palabra_a_reemplazar} fue reemplazada por {palabra_con_que_reemplazar}")
# print(f"La frase final es:\n {palabra_reemplazada}")

# """
# Buscar una cadena y devolver True o False
# """

cadena = "Luis camina y luego corre por la calle"

print(len(cadena))
print("camina" in cadena)
print(cadena.isdigit())
print(cadena[2])
print(cadena[0:4])

