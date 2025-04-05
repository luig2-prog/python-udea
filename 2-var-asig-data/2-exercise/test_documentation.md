# Explicación de las Pruebas de Tipos de Datos

## Descripción General
Este conjunto de pruebas unitarias verifica que cada variable en nuestro programa tiene el tipo de dato correcto y contiene los valores esperados. Las pruebas cubren todos los tipos de datos básicos de Python.

## Estructura de las Pruebas

### 1. Importaciones
```python
import unittest
from main import (
    texto,
    numero_entero,
    numero_decimal,
    valor_booleano,
    lista,
    diccionario,
    tupla,
    conjunto,
    valor_nulo
)
```
- Importamos el módulo `unittest` para las herramientas de prueba
- Importamos todas las variables que queremos probar desde el archivo principal

### 2. Métodos de Prueba

#### Prueba de Texto (String)
```python
def test_texto(self):
    self.assertIsInstance(texto, str)
    self.assertEqual(texto, "Programando en Python")
```
- Verifica que `texto` es una cadena de texto (str)
- Comprueba que el contenido es exactamente "Programando en Python"

#### Prueba de Número Entero
```python
def test_numero_entero(self):
    self.assertIsInstance(numero_entero, int)
    self.assertEqual(numero_entero, 123)
```
- Verifica que `numero_entero` es un número entero (int)
- Comprueba que el valor es 123

#### Prueba de Número Decimal
```python
def test_numero_decimal(self):
    self.assertIsInstance(numero_decimal, float)
    self.assertAlmostEqual(numero_decimal, 3.14159)
```
- Verifica que `numero_decimal` es un número decimal (float)
- Usa `assertAlmostEqual` para comparar números decimales (evita problemas de precisión)

#### Prueba de Valor Booleano
```python
def test_valor_booleano(self):
    self.assertIsInstance(valor_booleano, bool)
    self.assertTrue(valor_booleano)
```
- Verifica que `valor_booleano` es un booleano (bool)
- Comprueba que el valor es True

#### Prueba de Lista
```python
def test_lista(self):
    self.assertIsInstance(lista, list)
    self.assertEqual(len(lista), 4)
    self.assertEqual(lista[0], 1)
    self.assertEqual(lista[-1], "cuatro")
```
- Verifica que `lista` es una lista (list)
- Comprueba su longitud
- Verifica elementos específicos (primer y último elemento)

#### Prueba de Diccionario
```python
def test_diccionario(self):
    self.assertIsInstance(diccionario, dict)
    self.assertEqual(diccionario["clave"], "valor")
    self.assertEqual(diccionario["otro"], 5)
```
- Verifica que `diccionario` es un diccionario (dict)
- Comprueba valores específicos por sus claves

#### Prueba de Tupla
```python
def test_tupla(self):
    self.assertIsInstance(tupla, tuple)
    self.assertEqual(len(tupla), 3)
    self.assertEqual(tupla[0], 10)
    self.assertEqual(tupla[-1], 30)
```
- Verifica que `tupla` es una tupla (tuple)
- Comprueba su longitud
- Verifica elementos específicos

#### Prueba de Conjunto
```python
def test_conjunto(self):
    self.assertIsInstance(conjunto, set)
    self.assertEqual(len(conjunto), 3)  # El 3 duplicado se elimina
    self.assertTrue(1 in conjunto)
    self.assertTrue(2 in conjunto)
    self.assertTrue(3 in conjunto)
```
- Verifica que `conjunto` es un conjunto (set)
- Comprueba su longitud (nota: los duplicados se eliminan)
- Verifica la presencia de elementos específicos

#### Prueba de Valor Nulo
```python
def test_valor_nulo(self):
    self.assertIsNone(valor_nulo)
```
- Verifica que `valor_nulo` es None

## Métodos de Assert Utilizados

1. `assertIsInstance()`: Verifica el tipo de dato
2. `assertEqual()`: Verifica igualdad exacta
3. `assertAlmostEqual()`: Verifica igualdad aproximada (para números decimales)
4. `assertTrue()`: Verifica que una condición es verdadera
5. `assertIsNone()`: Verifica que un valor es None

## Ejecución de las Pruebas
Para ejecutar las pruebas, usa el comando:
```bash
python3 -m unittest test_data_types.py -v
```

## Resultados Esperados
Cuando las pruebas son exitosas, verás:
- Un mensaje "OK" al final
- Cada prueba individual marcada como "ok"
- El número total de pruebas ejecutadas (9 en este caso) 