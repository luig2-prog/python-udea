# Ejercicios de Python: Variables, asignaciones y tipos de datos

¡Excelente! Ha llegado el momento de consolidar tus conocimientos con algunos ejercicios prácticos. Resuelve los siguientes problemas basados en la clase que hemos tenido sobre variables, asignaciones y tipos de datos en Python.

**Ejercicio 1: Creación y asignación de variables**

1.  Crea una variable llamada `nombre_usuario` y asígnale tu nombre.
2.  Crea una variable llamada `edad_usuario` y asígnale tu edad como un número entero.
3.  Crea una variable llamada `altura_usuario` y asígnale tu altura en metros (o una estimación) como un número decimal.
4.  Crea una variable llamada `es_estudiante_actualmente` y asígnale un valor booleano (`True` o `False`) según corresponda.
5.  Imprime el valor de cada una de estas variables en líneas separadas utilizando la función `print()`.

- Solution: [two_class.py](./1-exercise/two_class.py)
- Unit test: [unit_test.py](./1-exercise/unit_test.py)

```bash
cd 1-exercise
python3 -m unittest unit_test.py -v
```

#### Explicación del comando de pruebas:
El comando `python3 -m unittest unit_test.py -v` ejecuta las pruebas unitarias y se descompone así:

1. `python3`: El intérprete de Python 3
2. `-m`: Ejecuta un módulo como script
3. `unittest`: El módulo de Python para pruebas unitarias
4. `unit_test.py`: La ruta al archivo de pruebas
5. `-v`: Modo verbose (detallado) que muestra información sobre cada prueba

La salida mostrará:
- El nombre de cada prueba ejecutada
- El resultado de cada prueba (ok/fail)
- Un resumen final con el total de pruebas ejecutadas

**Ejercicio 2: Identificación de tipos de datos**

Para cada uno de los siguientes valores, escribe en un comentario el tipo de dato de Python que representa:

```python
"Programando en Python"  #
123                      #
3.14159                  #
True                     #
[1, 2, 3, "cuatro"]      #
{"clave": "valor", "otro": 5} #
(10, 20, 30)             #
{1, 2, 3, 3}             #
None                     #
```


### Ejercicio 3: Nombres de variables válidos

Indica cuáles de los siguientes nombres de variables son válidos en Python. Para los que no sean válidos, explica brevemente por qué no cumplen con las reglas de nomenclatura:

```
mi_variable_1 # valido
_contador # valido
nombreCompleto # valido
2_variable # no valido, no puede iniciar por un numero
variable-larga # no valido
VariableConMayusculas # valido
palabra reservada # no valido
últimoElemento # no valido
```

### Ejercicio 4: Operaciones aritméticas y asignación

1.  Crea una variable llamada `precio_inicial` y asígnale el valor 50.
2.  Crea una variable llamada `descuento_porcentaje` y asígnale el valor 10.
3.  Calcula el valor del descuento (precio inicial multiplicado por el porcentaje de descuento dividido por 100) y guárdalo en una variable llamada `valor_descuento`.
4.  Utiliza el operador de asignación `-=` para restar el `valor_descuento` del `precio_inicial` y actualizar la variable `precio_inicial` con el precio final.
5.  Imprime el valor del `precio_inicial` después del descuento.

### Ejercicio 5: Comparaciones y booleanos

1.  Crea dos variables numéricas, `edad_permitida` con el valor 18 y `edad_usuario_actual` con un valor de tu elección.
2.  Utiliza operadores de comparación para determinar si `edad_usuario_actual` es mayor o igual que `edad_permitida`. Guarda el resultado en una variable llamada `puede_votar`.
3.  Imprime el valor de la variable `puede_votar`.
4.  Utiliza operadores de comparación para determinar si `edad_usuario_actual` es menor que `edad_permitida`. Guarda el resultado en una variable llamada `es_menor_de_edad`.
5.  Imprime el valor de la variable `es_menor_de_edad`.

### Ejercicio 6: Operadores lógicos

1.  Crea dos variables booleanas: `tiene_licencia` con el valor `True` y `sabe_manejar` con el valor `False`.
2.  Utiliza el operador lógico `and` para determinar si una persona puede conducir (necesita ambas condiciones verdaderas). Guarda el resultado en una variable llamada `puede_conducir`. Imprime el valor.
3.  Utiliza el operador lógico `or` para determinar si una persona puede entrar a un evento (si tiene una entrada VIP o una entrada regular). Crea las variables `tiene_vip` (True o False) y `tiene_regular` (True o False) con valores de tu elección y guarda el resultado en `puede_entrar_evento`. Imprime el valor.
4.  Utiliza el operador lógico `not` para negar el valor de `sabe_manejar` y guárdalo en una variable llamada `no_sabe_manejar`. Imprime el valor.

### Ejercicio 7: Operadores de Identidad y Pertenencia

1. Crea dos listas `lista1` y `lista2` con los mismos valores `[1, 2, 3]`.
2. Crea una variable `lista3` que sea una referencia a `lista1` (asignación directa).
3. Utiliza el operador `is` para comparar:
   - `lista1` con `lista2`
   - `lista1` con `lista3`
4. Crea una lista `numeros = [1, 2, 3, 4, 5]`
5. Utiliza el operador `in` para verificar si:
   - El número 3 está en `numeros`
   - El número 6 está en `numeros`
6. Guarda los resultados en variables e imprímelos.

### Ejercicio 8: Operadores Bit a Bit

1. Crea dos variables `a = 60` y `b = 13`
2. Realiza las siguientes operaciones bit a bit:
   - AND (`&`)
   - OR (`|`)
   - XOR (`^`)
   - Desplazamiento a la izquierda de `a` por 2 posiciones (`<<`)
   - Desplazamiento a la derecha de `a` por 2 posiciones (`>>`)
3. Imprime los resultados en formato binario usando `bin()`

### Ejercicio 9: Docstrings y Documentación

1. Crea una función llamada `calcular_promedio` que tome una lista de números.
2. Agrega un docstring que explique:
   - Qué hace la función
   - Qué parámetros recibe
   - Qué retorna
   - Un ejemplo de uso
3. Implementa la función para que calcule el promedio.
4. Imprime el docstring usando `.__doc__`

### Ejercicio 10: Tipos de Colecciones

1. Crea un diccionario `estudiante` con:
   - Nombre
   - Edad
   - Lista de calificaciones
   - Tuple con fecha de inscripción (año, mes, día)
   - Set con materias cursadas
2. Realiza las siguientes operaciones:
   - Agrega una nueva calificación a la lista
   - Agrega una nueva materia al set
   - Modifica la edad
   - Intenta modificar la fecha de inscripción (debería dar error por ser tuple)
3. Imprime el diccionario después de cada operación.

### Ejercicio 11: Operadores de Asignación Compuestos

1. Crea una variable `contador = 0`
2. Utiliza diferentes operadores de asignación para:
   - Incrementar en 5 (`+=`)
   - Multiplicar por 2 (`*=`)
   - Dividir entre 3 (`/=`)
   - Calcular el residuo de dividir entre 2 (`%=`)
   - Elevar al cuadrado (`**=`)
3. Imprime el valor después de cada operación.

### Ejercicio 12: Conversión de Tipos

1. Crea las siguientes variables:
   - `numero_texto = "123.45"`
   - `booleano = True`
   - `entero = 42`
2. Realiza las siguientes conversiones:
   - `numero_texto` a float
   - `booleano` a str
   - `entero` a float
   - `numero_texto` a int (debe fallar, maneja el error)
3. Imprime cada resultado y su tipo usando `type()`

### Ejercicio 13: Manipulación de Strings

1. Crea una variable `texto` con el valor "Python es un lenguaje de programación versátil".
2. Realiza las siguientes operaciones:
   - Convierte todo el texto a mayúsculas y guárdalo en `texto_mayusculas`
   - Convierte todo el texto a minúsculas y guárdalo en `texto_minusculas`
   - Obtén la longitud del texto y guárdala en `longitud_texto`
   - Reemplaza "Python" por "JavaScript" y guárdalo en `texto_reemplazado`
   - Divide el texto en palabras y guárdalas en una lista llamada `palabras`
3. Imprime todos los resultados.

### Ejercicio 14: Slicing de Listas y Strings

1. Crea una lista `numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`
2. Crea una cadena `abecedario = "abcdefghijklmnopqrstuvwxyz"`
3. Utiliza slicing para obtener:
   - Los primeros 5 números
   - Los últimos 3 números
   - Los números en posiciones pares
   - Los números en posiciones impares
   - La lista invertida
   - Las primeras 10 letras del abecedario
   - El abecedario invertido
4. Imprime todos los resultados.

### Ejercicio 15: Operaciones con Sets

1. Crea dos sets: `set_a = {1, 2, 3, 4, 5}` y `set_b = {4, 5, 6, 7, 8}`
2. Realiza y guarda en variables las siguientes operaciones:
   - La unión de ambos sets
   - La intersección de ambos sets
   - La diferencia set_a - set_b
   - La diferencia set_b - set_a
   - La diferencia simétrica (elementos en uno u otro set, pero no en ambos)
3. Verifica si `set_a` es subconjunto de la unión calculada.
4. Imprime todos los resultados.

### Ejercicio 16: Métodos de Diccionarios

1. Crea un diccionario `inventario` con al menos 5 productos y sus precios.
2. Realiza las siguientes operaciones:
   - Obtén una lista de todos los productos
   - Obtén una lista de todos los precios
   - Encuentra el producto más caro
   - Calcula el valor total del inventario
   - Crea una copia del diccionario e incrementa todos los precios en un 10%
3. Imprime los resultados después de cada operación.

### Ejercicio 17: Tuplas y Desempaquetado

1. Crea una tupla `coordenadas` con tres valores (x, y, z).
2. Crea una tupla `datos_personales` con (nombre, edad, ciudad, profesión).
3. Realiza desempaquetado para asignar los valores a variables individuales.
4. Crea una función que reciba las coordenadas y retorne la distancia al origen (0,0,0).
5. Crea una lista de tuplas `personas` donde cada tupla contenga (nombre, edad) de diferentes personas.
6. Utiliza desempaquetado en un bucle for para imprimir: "Nombre: [nombre], Edad: [edad]" para cada persona.

### Ejercicio 18: Valores Truthy y Falsy

1. Crea las siguientes variables y verifica si Python las considera True o False cuando se usan en una condición:
   - `vacio = ""`
   - `cero = 0`
   - `nulo = None`
   - `lista_vacia = []`
   - `diccionario_vacio = {}`
   - `uno = 1`
   - `texto = "Hola"`
   - `lista_con_elementos = [1, 2, 3]`
2. Para cada variable, crea una estructura if-else que imprima "Es True" o "Es False" según corresponda.

### Ejercicio 19: Operadores de Cortocircuito

1. Crea una función `imprimir_mensaje()` que imprima "Función ejecutada" y retorne None.
2. Crea las siguientes variables: `a = True`, `b = False`.
3. Evalúa las siguientes expresiones y predice si la función se ejecutará o no:
   - `a and imprimir_mensaje()`
   - `b and imprimir_mensaje()`
   - `a or imprimir_mensaje()`
   - `b or imprimir_mensaje()`
4. Explica por qué la función se ejecuta o no en cada caso.

### Ejercicio 20: Conversión entre Tipos de Colecciones

1. Crea un diccionario `datos = {"a": 1, "b": 2, "c": 3}`
2. Realiza las siguientes conversiones:
   - Convierte las claves del diccionario a una lista
   - Convierte los valores del diccionario a una tupla
   - Convierte el diccionario a una lista de tuplas (clave, valor)
   - Crea un set con las claves del diccionario
   - Crea un nuevo diccionario donde las claves y valores estén intercambiados
3. Imprime todos los resultados.

Cada ejercicio debe incluir:
- Pruebas unitarias para validar los resultados
- Manejo de errores cuando sea apropiado
