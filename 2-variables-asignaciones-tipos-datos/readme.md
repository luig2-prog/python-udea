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






