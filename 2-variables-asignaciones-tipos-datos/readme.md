# Variables, asignaciones y tipos de datos

## Variables

Las variables son espacios en memoria que almacenan valores que pueden cambiar durante la ejecución del programa.

En Python, no es necesario declarar el tipo de variable, ya que se determina automáticamente según el valor que se le asigne. Para crear una variable, simplemente eliges un nombre y le asignas un valor con el operador de asignación `=`.

```python
nombre = "Juan"
edad = 30
altura = 1.75
es_estudiante = True
```

Reglas para nombrar variables:

- Deben empezar con una letra o underscore. Un underscore es una convención para indicar que la variable es una variable de tipo privado:

```python
_nombre = "Juan"
```

- Pueden contener letras, números y underscores (guiones bajos).
- Son sensibles a mayúsculas y minúsculas (miVariable, MiVariable y MIVARIABLE son variables diferentes).
- No pueden ser palabras reservadas del lenguaje (if, for, while, etc.).

## Asignaciones

Las asignaciones son el proceso de darle un valor a una variable.

```python
nombre = "Juan"
edad = 30
altura = 1.75
es_estudiante = True
```

## Tipos de datos fundamentales

Python tiene varios tipos de datos fundamentales que se pueden clasificar en:

- `Enteros` (int): Números enteros, positivos o negativos, sin decimales.

```python
edad = 30
```

- `Flotantes` (float): Números con parte decimal.

```python
altura = 1.75
```

- `Booleanos` (bool): Valores lógicos que pueden ser `True` o `False`.

```python
es_estudiante = True
```

- `Cadenas` (str): Secuencias de caracteres, como palabras o frases, se pueden definir con comillas simples ('Hola') o dobles ("Hola").

```python
nombre = "Juan"
saludo = 'Hola'
```

- `Listas` (list): Colecciones ordenadas de elementos, como lista de números o palabras. Pueden contener cualquier tipo de dato como enteros, flotantes, cadenas, booleanos, etc. Pueden contener ejemplo, cadenas y enteros a la vez.

```python
numeros = [1, 2, 3, 4, 5]
nombres = ["Juan", "María", "Pedro"]
myList = ["Hello", 1, True]
```

- `Diccionarios` (dict): Colecciones de pares clave-valor, como diccionarios de palabras y sus significados.

```python
person = { "name": "Luis", "age": 25, "city": "Medellín" }
```

- `Tuplas` (tuple): Colecciones ordenadas e inmutables de elementos, como coordenadas o fechas.

```python
coordinates = (10, 20)
date = (2025, 3, 26)
```

- `Sets` (set): Colecciones de elementos únicos y no ordenados, no se pueden repetir elementos.

```python
colors = {"red", "blue", "green" }
```

- `None`: Tipo especial que representa la ausencia de valor

```python
value = None
```

Python es un lenguaje de tipado dinámico, lo que significa que no es necesario declarar el tipo de dato de una variable, esto se determina automáticamente según el valor que se le asigne. Puedes validar el tipo de dato de una variable con la función `type()`.

```python
age = 30
print(type(age)) # <class int>

name = "Luis"
print(type(name)) # <class 'str'>

is_student = True
print(type(is_student)) # <class bool>

height = 1.75
print(type(height)) # <class float>

coordinates = (10, 20)
print(type(coordinates)) # <class tuple>

colors = {"red", "blue", "green"}
print(type(colors)) # <class set>

value = None
print(type(value)) # <class NoneType>
```

## Conversión de tipos

....

## Operadores

Los operadores son símbolos que realizan operaciones entre variables y valores.

### Operadores aritméticos

Los operadores aritméticos son los que realizan operaciones matemáticas entre variables y valores.

| Operador | Descripción     | Ejemplo  | Resultado |
| -------- | --------------- | -------- | --------- |
| `+`      | Suma            | `x + y`  | `x + y`   |
| `-`      | Resta           | `x - y`  | `x - y`   |
| `*`      | Multiplicación  | `x * y`  | `x * y`   |
| `/`      | División        | `x / y`  | `x / y`   |
| `%`      | Módulo          | `x % y`  | `x % y`   |
| `//`     | División entera | `x // y` | `x // y`  |
| `**`     | Exponente       | `x ** y` | `x ** y`  |

### Operadores de comparación

Los operadores de comparación son los que realizan comparaciones entre variables y valores. Compara dos valores y devuelve un resultado booleano (True o False).

| Operador | Descripción | Ejemplo | Resultado |
| -------- | ----------- | ------- | --------- |
| `==`     | Igual       | `x == y` | `x == y`  |
| `!=`     | Diferente   | `x != y` | `x != y`  |
| `>`      | Mayor       | `x > y`  | `x > y`   |
| `<`      | Menor       | `x < y`  | `x < y`   |
| `>=`     | Mayor o igual | `x >= y` | `x >= y`  |
| `<=`     | Menor o igual | `x <= y` | `x <= y`  |

### Operadores lógicos

Los operadores lógicos son los que realizan operaciones lógicas entre variables y valores. Se usan para combinar múltiples condiciones.

| Operador | Descripción | Ejemplo | Resultado |
| -------- | ----------- | ------- | --------- |
| `and`    | Y           | `x and y` | `x and y`  |
| `or`     | O           | `x or y`  | `x or y`   |
| `not`    | No          | `not x`   | `not x`    |

### Operadores de asignación

Los operadores de asignación son los que realizan asignaciones entre variables y valores. Asignación combinada con operadores aritméticos y asignan el resultado a la variable.

| Operador | Descripción | Ejemplo | Resultado |
| -------- | ----------- | ------- | --------- |
| `=`      | Asignación | `x = y`  | `x = y`   |
| `+=`     | Asignación y suma | `x += y`  | `x = x + y`   |
| `-=`     | Asignación y resta | `x -= y`  | `x = x - y`   |
| `*=`     | Asignación y multiplicación | `x *= y`  | `x = x * y`   |
| `/=`     | Asignación y división | `x /= y`  | `x = x / y`   |
| `//=`    | Asignación y división entera | `x //= y`  | `x = x // y`   |
| `%=`     | Asignación y módulo | `x %= y`  | `x = x % y`   |
| `**=`    | Asignación y exponente | `x **= y`  | `x = x ** y`   |

### Operadores de identidad

Verifica si dos variables referencian el mismo objeto en memoria.
Los operadores de identidad son los que realizan comparaciones de identidad entre variables y valores.

| Operador | Descripción | Ejemplo | Resultado |
| -------- | ----------- | ------- | --------- |
| `is`     | Verdadero si ambos operandos son el mismo objeto | `x is y` | `x is y`  |
| `is not` | Verdadero si ambos operandos no son el mismo objeto | `x is not y` | `x is not y`  |

### Operadores de pertenencia

Verifica si un valor está contenido en una secuencia, como listas, cadenas o diccionarios.

| Operador | Descripción | Ejemplo | Resultado |
| -------- | ----------- | ------- | --------- |
| `in`     | Verdadero si el valor está contenido en la secuencia | `x in y` | `x in y`  |
| `not in` | Verdadero si el valor no está contenido en la secuencia | `x not in y` | `x not in y`  |

### Operadores Bit a Bit

Realizan operaciones bit a bit entre variables y valores.

| Operador | Descripción | Ejemplo | Resultado |
| -------- | ----------- | ------- | --------- |
| `&`      | AND         | `x & y`  | `x & y`   |
| `|`      | OR          | `x | y`  | `x | y`   |
| `^`      | XOR         | `x ^ y`  | `x ^ y`   |
| `~`      | NOT         | `~x`  | `~x`   |
| `<<`     | Desplazamiento a la izquierda | `x << y`  | `x << y`   |
| `>>`     | Desplazamiento a la derecha | `x >> y`  | `x >> y`   |

## Comentarios y Documentación (docstrings)

Los comentarios son notas que se añaden al código para explicar lo que hace el código.

```python
# Este es un comentario
```

La documentación es una forma de documentar el código para que otros puedan entenderlo.

```python
"""
Este es un comentario
Multiples lineas
"""
```

### Docstrings

Son cadenas multilínea que se utilizan para documentar funciones, clases, módulos y otros objetos. Van inmediatamente después de la definición de la función, clase, módulo, etc. Y se cierran con tres comillas dobles. 

Son accesibles a través del atributo `__doc__` de los objetos. Python los almacena como un atributo de tipo `str` en el objeto lo que permite que herramientas como `pydoc` puedan extraer la documentación y generar documentación HTML o Sphynx.

```python
def saludar(nombre):
    """
    Esta función saluda al usuario por su nombre
    """
    print(f"Hola, {nombre}!")

print(saludar.__doc__
```

### Ejemplos detallados por tipo de dato:

#### Enteros (int)
```python
# Ejemplos de enteros
edad = 30
temperatura_bajo_cero = -5
población = 8_000_000  # Los guiones bajos hacen más legible números grandes

# Operaciones con enteros
suma = 5 + 3           # 8
resta = 10 - 4         # 6
multiplicación = 3 * 6 # 18
división_entera = 7 // 2  # 3 (descarta el decimal)
```

#### Flotantes (float)
```python
# Ejemplos de flotantes
altura = 1.75
pi = 3.14159
científica = 1.23e-4  # Notación científica (0.000123)

# Operaciones con flotantes
división = 7 / 2      # 3.5
raíz_cuadrada = 9 ** 0.5  # 3.0

# Precisión y redondeo
resultado = round(3.14159, 2)  # 3.14
```

#### Booleanos (bool)
```python
# Valores booleanos directos
es_estudiante = True
tiene_mascota = False

# Valores booleanos por comparación
es_mayor_de_edad = edad >= 18
número_es_par = (10 % 2 == 0)  # True

# Operaciones lógicas
usuario_activo = True
suscripción_vigente = False
puede_acceder = usuario_activo and suscripción_vigente  # False
necesita_renovar = usuario_activo and not suscripción_vigente  # True
```

#### Cadenas (str)
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

#### Listas (list)
```python
# Creación de listas
números = [1, 2, 3, 4, 5]
nombres = ["Juan", "María", "Pedro"]
mixta = ["Hola", 42, True, 3.14]

# Acceso y modificación
primer_nombre = nombres[0]  # "Juan"
nombres[1] = "Ana"  # Modifica la lista: ["Juan", "Ana", "Pedro"]

# Métodos de listas
números.append(6)  # Añade al final: [1, 2, 3, 4, 5, 6]
números.insert(0, 0)  # Inserta al inicio: [0, 1, 2, 3, 4, 5, 6]
números.remove(3)  # Elimina el primer 3: [0, 1, 2, 4, 5, 6]
último = números.pop()  # Elimina y retorna el último: 6

# Slicing (rebanado)
primeros_tres = números[0:3]  # [0, 1, 2]
```

#### Diccionarios (dict)
```python
# Creación de diccionarios
persona = {"nombre": "Luis", "edad": 25, "ciudad": "Medellín"}
calificaciones = {"matemáticas": 90, "historia": 85, "ciencias": 95}

# Acceso y modificación
nombre_persona = persona["nombre"]  # "Luis"
persona["edad"] = 26  # Modifica el valor

# Añadir y eliminar elementos
persona["ocupación"] = "Ingeniero"  # Añade nuevo par clave-valor
del persona["ciudad"]  # Elimina el par clave-valor

# Métodos útiles
claves = persona.keys()  # dict_keys(['nombre', 'edad', 'ocupación'])
valores = persona.values()  # dict_values(['Luis', 26, 'Ingeniero'])
persona.update({"ciudad": "Bogotá", "estado_civil": "Soltero"})  # Añade/actualiza múltiples
```

#### Tuplas (tuple)
```python
# Creación de tuplas
coordenadas = (10, 20)
fecha = (2023, 5, 15)
singleton = (42,)  # Tupla de un solo elemento (necesita la coma)

# Acceso (similar a las listas)
x = coordenadas[0]  # 10
y = coordenadas[1]  # 20

# Desempaquetado de tuplas
año, mes, día = fecha
print(f"Fecha: {día}/{mes}/{año}")  # "Fecha: 15/5/2023"

# Tuplas son inmutables
# coordenadas[0] = 15  # Esto daría error

# Métodos útiles
posición = fecha.index(5)  # 1 (índice del valor 5)
conteo = fecha.count(2023)  # 1 (número de veces que aparece 2023)
```

#### Sets (set)
```python
# Creación de sets
colores = {"rojo", "azul", "verde"}
números_pares = {2, 4, 6, 8, 10}
duplicados = {1, 2, 2, 3, 3, 4}  # Se convierte en {1, 2, 3, 4}

# Operaciones de conjuntos
unión = colores | {"amarillo", "naranja"}  # Unión
intersección = números_pares & {4, 5, 6}  # Intersección: {4, 6}
diferencia = colores - {"verde", "amarillo"}  # Diferencia: {"rojo", "azul"}

# Métodos útiles
colores.add("púrpura")  # Añade un elemento
colores.remove("azul")  # Elimina un elemento (error si no existe)
colores.discard("negro")  # Elimina si existe (no da error si no existe)
```

#### None
```python
# Uso básico de None
valor = None
print(valor)  # None

# Comprobación de None
def buscar_usuario(id):
    # Simulación de búsqueda
    if id > 1000:
        return None
    return {"id": id, "nombre": "Usuario " + str(id)}

resultado = buscar_usuario(1500)
if resultado is None:
    print("Usuario no encontrado")
else:
    print(f"Usuario encontrado: {resultado['nombre']}")
```


### Ejemplos detallados de variables:

1. **Asignación básica de variables:**
```python
# Asignación de diferentes tipos de datos
nombre = "María González"  # Variable tipo string
edad = 28                  # Variable tipo integer
altura = 1.65              # Variable tipo float
es_estudiante = True       # Variable tipo boolean

# Imprimir valores
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Altura: {altura}m")
print(f"¿Es estudiante?: {es_estudiante}")
```

2. **Reasignación de variables:**
```python
# Las variables pueden cambiar de valor
contador = 10
print(f"Valor inicial: {contador}")

contador = 25
print(f"Nuevo valor: {contador}")

# También pueden cambiar de tipo
variable = "Hola"
print(f"Valor como string: {variable}")

variable = 42
print(f"Ahora como entero: {variable}")
```

3. **Asignación múltiple:**
```python
# Asignar el mismo valor a múltiples variables
x = y = z = 100
print(x, y, z)  # Imprime: 100 100 100

# Asignar diferentes valores a múltiples variables
a, b, c = 10, "Hola", True
print(a)  # Imprime: 10
print(b)  # Imprime: Hola
print(c)  # Imprime: True
```
```

### Para añadir a cada tipo de dato:

```markdown
### Ejemplos detallados por tipo de dato:

#### Enteros (int)
```python
# Ejemplos de enteros
edad = 30
temperatura_bajo_cero = -5
población = 8_000_000  # Los guiones bajos hacen más legible números grandes

# Operaciones con enteros
suma = 5 + 3           # 8
resta = 10 - 4         # 6
multiplicación = 3 * 6 # 18
división_entera = 7 // 2  # 3 (descarta el decimal)
```

#### Flotantes (float)
```python
# Ejemplos de flotantes
altura = 1.75
pi = 3.14159
científica = 1.23e-4  # Notación científica (0.000123)

# Operaciones con flotantes
división = 7 / 2      # 3.5
raíz_cuadrada = 9 ** 0.5  # 3.0

# Precisión y redondeo
resultado = round(3.14159, 2)  # 3.14
```

#### Booleanos (bool)
```python
# Valores booleanos directos
es_estudiante = True
tiene_mascota = False

# Valores booleanos por comparación
es_mayor_de_edad = edad >= 18
número_es_par = (10 % 2 == 0)  # True

# Operaciones lógicas
usuario_activo = True
suscripción_vigente = False
puede_acceder = usuario_activo and suscripción_vigente  # False
necesita_renovar = usuario_activo and not suscripción_vigente  # True
```

#### Cadenas (str)
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

#### Listas (list)
```python
# Creación de listas
números = [1, 2, 3, 4, 5]
nombres = ["Juan", "María", "Pedro"]
mixta = ["Hola", 42, True, 3.14]

# Acceso y modificación
primer_nombre = nombres[0]  # "Juan"
nombres[1] = "Ana"  # Modifica la lista: ["Juan", "Ana", "Pedro"]

# Métodos de listas
números.append(6)  # Añade al final: [1, 2, 3, 4, 5, 6]
números.insert(0, 0)  # Inserta al inicio: [0, 1, 2, 3, 4, 5, 6]
números.remove(3)  # Elimina el primer 3: [0, 1, 2, 4, 5, 6]
último = números.pop()  # Elimina y retorna el último: 6

# Slicing (rebanado)
primeros_tres = números[0:3]  # [0, 1, 2]
```

#### Diccionarios (dict)
```python
# Creación de diccionarios
persona = {"nombre": "Luis", "edad": 25, "ciudad": "Medellín"}
calificaciones = {"matemáticas": 90, "historia": 85, "ciencias": 95}

# Acceso y modificación
nombre_persona = persona["nombre"]  # "Luis"
persona["edad"] = 26  # Modifica el valor

# Añadir y eliminar elementos
persona["ocupación"] = "Ingeniero"  # Añade nuevo par clave-valor
del persona["ciudad"]  # Elimina el par clave-valor

# Métodos útiles
claves = persona.keys()  # dict_keys(['nombre', 'edad', 'ocupación'])
valores = persona.values()  # dict_values(['Luis', 26, 'Ingeniero'])
persona.update({"ciudad": "Bogotá", "estado_civil": "Soltero"})  # Añade/actualiza múltiples
```

#### Tuplas (tuple)
```python
# Creación de tuplas
coordenadas = (10, 20)
fecha = (2023, 5, 15)
singleton = (42,)  # Tupla de un solo elemento (necesita la coma)

# Acceso (similar a las listas)
x = coordenadas[0]  # 10
y = coordenadas[1]  # 20

# Desempaquetado de tuplas
año, mes, día = fecha
print(f"Fecha: {día}/{mes}/{año}")  # "Fecha: 15/5/2023"

# Tuplas son inmutables
# coordenadas[0] = 15  # Esto daría error

# Métodos útiles
posición = fecha.index(5)  # 1 (índice del valor 5)
conteo = fecha.count(2023)  # 1 (número de veces que aparece 2023)
```

#### Sets (set)
```python
# Creación de sets
colores = {"rojo", "azul", "verde"}
números_pares = {2, 4, 6, 8, 10}
duplicados = {1, 2, 2, 3, 3, 4}  # Se convierte en {1, 2, 3, 4}

# Operaciones de conjuntos
unión = colores | {"amarillo", "naranja"}  # Unión
intersección = números_pares & {4, 5, 6}  # Intersección: {4, 6}
diferencia = colores - {"verde", "amarillo"}  # Diferencia: {"rojo", "azul"}

# Métodos útiles
colores.add("púrpura")  # Añade un elemento
colores.remove("azul")  # Elimina un elemento (error si no existe)
colores.discard("negro")  # Elimina si existe (no da error si no existe)
```

#### None
```python
# Uso básico de None
valor = None
print(valor)  # None

# Comprobación de None
def buscar_usuario(id):
    # Simulación de búsqueda
    if id > 1000:
        return None
    return {"id": id, "nombre": "Usuario " + str(id)}

resultado = buscar_usuario(1500)
if resultado is None:
    print("Usuario no encontrado")
else:
    print(f"Usuario encontrado: {resultado['nombre']}")
```
```

### Para añadir a la sección de Operadores:

```markdown
### Ejemplos detallados de operadores:

#### Operadores aritméticos
```python
# Ejemplos detallados
a, b = 10, 3

suma = a + b          # 13
resta = a - b         # 7
multiplicación = a * b  # 30
división = a / b      # 3.3333...
módulo = a % b        # 1 (resto de 10/3)
división_entera = a // b  # 3 (parte entera de 10/3)
exponente = a ** b    # 1000 (10^3)

# Ejemplo práctico: cálculo de precio total con impuestos
precio_base = 100
tasa_impuesto = 0.16  # 16%
precio_total = precio_base + (precio_base * tasa_impuesto)
print(f"Precio con impuestos: ${precio_total}")  # $116.0
```

#### Operadores de comparación
```python
# Ejemplos básicos
x, y = 5, 10

igual = x == y        # False
diferente = x != y    # True
mayor = x > y         # False
menor = x < y         # True
mayor_igual = x >= 5  # True
menor_igual = y <= 10 # True

# Comparaciones encadenadas
edad = 25
en_rango = 18 <= edad <= 65  # True (equivale a: 18 <= edad and edad <= 65)

# Ejemplo práctico: validación de entrada
temperatura = 38.5
tiene_fiebre = temperatura > 37.5
necesita_atención = temperatura >= 39.0

print(f"¿Tiene fiebre? {tiene_fiebre}")  # True
print(f"¿Necesita atención urgente? {necesita_atención}")  # False
```

#### Operadores lógicos
```python
# Ejemplos básicos
p, q = True, False

y_lógico = p and q    # False (ambos deben ser True)
o_lógico = p or q     # True (al menos uno debe ser True)
negación = not p      # False (invierte el valor)

# Cortocircuito en operadores lógicos
resultado = False and print("Esto no se ejecuta")  # No imprime nada
resultado = True or print("Esto no se ejecuta")    # No imprime nada

# Ejemplo práctico: control de acceso
edad_usuario = 16
tiene_permiso_padres = True

puede_acceder = edad_usuario >= 18 or tiene_permiso_padres
print(f"¿Puede acceder al contenido? {puede_acceder}")  # True
```

#### Operadores de asignación
```python
# Ejemplos de operadores de asignación
x = 10

# Operadores combinados
x += 5      # x = x + 5 = 15
x -= 3      # x = x - 3 = 12
x *= 2      # x = x * 2 = 24
x /= 6      # x = x / 6 = 4.0
x //= 2     # x = x // 2 = 2.0
x %= 3      # x = x % 3 = 2.0
x **= 3     # x = x ** 3 = 8.0

# Ejemplo práctico: actualización de inventario
inventario = 100
ventas_diarias = 15
devoluciones = 3

inventario -= ventas_diarias  # Resta las ventas
inventario += devoluciones    # Suma las devoluciones
print(f"Inventario actual: {inventario}")  # 88
```

#### Operadores de identidad
```python
# Ejemplos de operadores de identidad
a = [1, 2, 3]
b = [1, 2, 3]
c = a

es_mismo_objeto_ab = a is b    # False (diferentes objetos)
es_mismo_objeto_ac = a is c    # True (mismo objeto)
no_es_mismo_objeto = a is not b  # True

# Comprobación más segura para None
valor = None
if valor is None:             # Mejor que: if valor == None
    print("El valor es None")

# Ejemplo práctico: cache de objetos
def obtener_configuración(reset=False):
    # Simulación de caché
    if "config" not in obtener_configuración.__dict__ or reset:
        obtener_configuración.config = {"tema": "claro", "idioma": "es"}
    return obtener_configuración.config

config1 = obtener_configuración()
config2 = obtener_configuración()
print(config1 is config2)  # True (mismo objeto)
```

#### Operadores de pertenencia
```python
# Ejemplos de operadores de pertenencia
frutas = ["manzana", "banana", "naranja"]
usuario = {"nombre": "Ana", "edad": 28}

contiene_manzana = "manzana" in frutas          # True
no_contiene_uva = "uva" not in frutas           # True
tiene_propiedad = "nombre" in usuario           # True
valor_en_diccionario = "Ana" in usuario.values()  # True

# Ejemplo práctico: filtro de lista
palabras_prohibidas = ["spam", "ofensivo", "inapropiado"]
mensaje = "Hola, este es un mensaje normal"

es_apropiado = all(palabra not in mensaje.lower() for palabra in palabras_prohibidas)
print(f"¿Es un mensaje apropiado? {es_apropiado}")  # True
```

#### Operadores Bit a Bit
```python
# Ejemplos de operadores bit a bit
a = 60  # 0011 1100 en binario
b = 13  # 0000 1101 en binario

and_bit = a & b   # 0000 1100 = 12
or_bit = a | b    # 0011 1101 = 61
xor_bit = a ^ b   # 0011 0001 = 49
not_bit = ~a      # 1100 0011 = -61 (complemento a 2)
shift_left = a << 2  # 1111 0000 = 240 (desplaza 2 bits a la izquierda)
shift_right = a >> 2  # 0000 1111 = 15 (desplaza 2 bits a la derecha)

# Ver la representación binaria
print(f"a en binario: {bin(a)}")  # 0b111100
print(f"b en binario: {bin(b)}")  # 0b1101
print(f"a & b en binario: {bin(and_bit)}")  # 0b1100

# Ejemplo práctico: banderas de permisos
LEER = 0b0001    # 1
ESCRIBIR = 0b0010  # 2
EJECUTAR = 0b0100  # 4
ADMIN = 0b1000    # 8

permisos_usuario = LEER | ESCRIBIR  # 0011 = 3

# Verificar permisos
puede_leer = permisos_usuario & LEER != 0      # True
puede_escribir = permisos_usuario & ESCRIBIR != 0  # True
puede_ejecutar = permisos_usuario & EJECUTAR != 0  # False

print(f"¿Puede leer? {puede_leer}")
print(f"¿Puede escribir? {puede_escribir}")
print(f"¿Puede ejecutar? {puede_ejecutar}")
```

Con esta información, el readme.md quedará más completo con ejemplos detallados de cada concepto y múltiples casos prácticos de uso.



