"""
Diccionarios

clave - valor
"""

carro = {
    "marca": "Ford",
    "modelo": "Mustang",
    "annio": "1964"
}

print(f"len(carro): {len(carro)}")
print(f"carro[\"marca\"]: {carro["marca"]}")

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