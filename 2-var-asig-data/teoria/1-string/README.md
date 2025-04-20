#### Cadenas (str)

Secuencia de cara

```python
# Diferentes formas de definir strings
nombre = "Juan Pérez"
dirección = 'Calle Principal 123'
descripción = """Este es un texto
que ocupa varias
líneas"""

# Operaciones con strings
saludo = "Hola " + nombre  # Concatenación
repetición = "Eco " * 3    # "Eco Eco Eco "

# Acceso a caracteres
primera_letra = nombre[0]  # "J"
últimas_letras = nombre[-5:]  # "Pérez"

# Métodos útiles
mayúsculas = nombre.upper()  # "JUAN PÉREZ"
reemplazo = nombre.replace("Juan", "Carlos")  # "Carlos Pérez"
palabras = nombre.split()  # ["Juan", "Pérez"]
```