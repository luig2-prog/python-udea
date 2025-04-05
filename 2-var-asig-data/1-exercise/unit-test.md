# Explicación de las Pruebas Unitarias

## Descripción General
Las pruebas unitarias son una forma de verificar que cada parte de nuestro código funciona correctamente de manera aislada. En este caso, estamos verificando las variables definidas en `two_class.py` para asegurarnos de que tienen los tipos de datos correctos y valores válidos.

## Estructura de las Pruebas

### 1. Importaciones Necesarias
```python
import unittest
from two_class import user_name, user_age, user_height, is_currently_student
```
- Importamos el módulo `unittest` que nos proporciona las herramientas para crear pruebas
- Importamos las variables específicas que queremos probar desde nuestro archivo principal

#### Explicación Detallada de la Línea de Importación
La línea `from two_class import user_name, user_age, user_height, is_currently_student` hace lo siguiente:

1. `from two_class`: Indica que queremos importar elementos desde el archivo `two_class.py`
   - El archivo debe estar en el mismo directorio que nuestro archivo de pruebas
   - No necesitamos incluir la extensión `.py` en la importación

2. `import user_name, user_age, user_height, is_currently_student`: 
   - Especifica exactamente qué variables queremos importar
   - Estas variables deben existir en el archivo `two_class.py`
   - Podemos usar estas variables directamente en nuestras pruebas sin necesidad de usar el prefijo `two_class.`

Alternativas de importación:
```python
# Alternativa 1: Importar todo el módulo
import two_class
# Uso: two_class.user_name, two_class.user_age, etc.

# Alternativa 2: Importar todo con *
from two_class import *
# No recomendado porque hace menos explícito qué estamos usando

# Alternativa 3: Importar con alias
from two_class import user_name as nombre
# Útil cuando hay conflictos de nombres
```

### 2. Clase de Prueba
```python
class TestTwoClass(unittest.TestCase):
```
- Creamos una clase que hereda de `unittest.TestCase`
- Esta clase contendrá todos nuestros métodos de prueba

### 3. Métodos de Prueba

#### Prueba del Nombre de Usuario
```python
def test_user_name(self):
    self.assertIsInstance(user_name, str)
    self.assertTrue(len(user_name) > 0)
```
- Verifica que `user_name` es una cadena de texto (str)
- Asegura que el nombre no está vacío

#### Prueba de la Edad
```python
def test_user_age(self):
    self.assertIsInstance(user_age, int)
    self.assertGreaterEqual(user_age, 0)
```
- Verifica que `user_age` es un número entero (int)
- Asegura que la edad no es negativa

#### Prueba de la Altura
```python
def test_user_height(self):
    self.assertIsInstance(user_height, float)
    self.assertGreater(user_height, 0)
    self.assertLess(user_height, 3)
```
- Verifica que `user_height` es un número decimal (float)
- Asegura que la altura es positiva
- Verifica que la altura está en un rango razonable (menos de 3 metros)

#### Prueba del Estado de Estudiante
```python
def test_is_currently_student(self):
    self.assertIsInstance(is_currently_student, bool)
```
- Verifica que `is_currently_student` es un valor booleano (True/False)

## Métodos de Assert Utilizados

1. `assertIsInstance()`: Verifica que un objeto es de un tipo específico
2. `assertTrue()`: Verifica que una condición es verdadera
3. `assertGreaterEqual()`: Verifica que un valor es mayor o igual que otro
4. `assertGreater()`: Verifica que un valor es mayor que otro
5. `assertLess()`: Verifica que un valor es menor que otro

## Ejecución de las Pruebas
Para ejecutar las pruebas, usamos el comando:
```bash
python3 -m unittest test_two_class.py -v
```
- `-v`: Modo verbose que muestra más detalles sobre las pruebas ejecutadas

## Resultados Esperados
Cuando las pruebas son exitosas, verás:
- Un mensaje "OK" al final
- Cada prueba individual marcada como "ok"
- El número total de pruebas ejecutadas

## Beneficios de las Pruebas Unitarias
1. Detección temprana de errores
2. Documentación del comportamiento esperado
3. Facilita la refactorización del código
4. Mejora la calidad del código
5. Proporciona confianza en que el código funciona como se espera
