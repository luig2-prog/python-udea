"""
Diccionarios

clave - valor
"""

carro = {
    "marca": "Ford",
    "modelo": "Mustang",
    "annio": "1964"
}


print(f"\ncarro: {carro}")

print(f"len(carro): {len(carro)}")
print(f"carro[\"marca\"]: {carro["marca"]}")

carroCopy = carro.copy()
print(f"\ncarroCopy: {carroCopy}")
carroCopy.clear()
print(f"\ncarroCopy: {carroCopy}")

carroFrom = carro.fromkeys("marca", "e")
print(f"\ncarroFrom: {carroFrom}")

print(f"carro.get(\"marca\"): {carro.get("marca")}")

print(f"carro.keys(): {carro.keys()}")

print(f"\ncarro: {carro}")

carro.update({"modelo": "fiesta"})

print(f"\ncarro: {carro}")

print(f"carro.values(): {carro.values()}")

print(f"\ncarro: {carro}")

carro.setdefault("test", "dos")

print(f"\ncarro: {carro}")




# Valido
ensayo = { 
    1 : "Luis", 
    2 : 15 , 
    "notas": [2.5, 3.5, 4] 
}


hijos = {
    "hijo1" : {
        "nombre": "Luis",
        "edad": 29
    },
    "hijo2": {
        "nombre": "Jesus",
        "edad": 22,
        "notas": [2.3, 5, 4]
    }
}

print(f"hijos[\"hijo2\"][\"nombre\"]: {hijos["hijo2"]["nombre"]}")
print(hijos["hijo2"]["notas"][1])


"""
Condicionales:


"""

print("\n ======================== Condicionales ======================== \n")

edad = 19
# edad = int(input("Ingrese la edad: "))

if edad >= 18:
    print("Es mayor de edad!")
else:
    print("No es mayor de edad!")


if edad >= 0 and edad < 6:
    print("primera infancia")
elif edad >= 6 and edad < 12:
    print("infancia")
elif edad >= 12 and edad < 18:
    print("adolecente")
elif edad >= 18 and edad < 26:
    print("adulto joven")
elif edad >= 26 and edad < 60:
    print("adulto")
elif edad >= 60:
    print("adlto mayor")
else:
    print("Fuera de rango")

dia = 3
# dia = int(input("Ingrese un numero del 1 al 7 para ver el día: "))

# Una forma
if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miercoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sabado")
elif dia == 7:
    print("Domingo")
else:
    print("No ingresó un número valido")

# Otra forma

lista_dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

if dia > 0 and dia <= 7:
    print(lista_dias[dia - 1])
else:
    print("No ingresó un número valido")
