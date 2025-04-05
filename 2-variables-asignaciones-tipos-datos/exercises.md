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

Cada ejercicio debe incluir:
- Pruebas unitarias para validar los resultados
- Comentarios explicando el código
- Manejo de errores cuando sea apropiado

¡Estos ejercicios te permitirán aplicar lo que hemos aprendido! Tómate tu tiempo para resolverlos y cuando estés listo, podemos revisarlos juntos. ¡Adelante!

