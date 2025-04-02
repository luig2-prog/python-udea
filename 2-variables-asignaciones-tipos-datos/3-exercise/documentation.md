# Documentación de Pruebas Unitarias - Cálculo de Descuento

## Descripción General
Este conjunto de pruebas verifica el cálculo correcto de un descuento sobre un precio inicial, incluyendo la validación de los valores y la impresión del resultado.

## Pruebas Implementadas

### 1. Validación de Valores Iniciales
```python
def test_validate_initial_price(self):
    """Validar valores iniciales"""
    self.assertEqual(starting_price, 50)
    self.assertEqual(discount_percentage, 10)
```
- Verifica que el precio inicial sea 50
- Verifica que el porcentaje de descuento sea 10%

### 2. Validación del Cálculo del Descuento
```python
def test_validate_discount_value(self):
    """Validar el calculo del descuento"""
    self.assertEqual(discount_value, 5)
```
- Verifica que el valor del descuento sea 5 (10% de 50)

### 3. Validación del Precio Final
```python
def test_validate_final_price(self):
    """Validar precio final"""
    self.assertEqual(final_price, 45)
```
- Verifica que el precio final sea 45 (50 - 5)

### 4. Validación de la Impresión
```python
def test_print_final_price(self):
    """Validar que se imprime el precio final"""
    with patch('sys.stdout', new=io.StringIO()) as fake_output:
        print(final_price)
        self.assertEqual(fake_output.getvalue().strip(), "45.0")
```

#### Explicación Detallada

1. **Propósito de la Prueba**
   - Verifica que el programa imprima correctamente el precio final
   - Asegura que el formato de salida sea el esperado ("45.0")

2. **Componentes del Código**
   - `patch('sys.stdout')`: 
     * Reemplaza temporalmente la salida estándar del sistema
     * Permite capturar lo que se imprimiría en la consola
     * Es como crear una "consola virtual" para las pruebas

   - `io.StringIO()`:
     * Crea un buffer de texto en memoria
     * Actúa como un archivo de texto virtual
     * Almacena todo lo que se imprimió

   - `as fake_output`:
     * Da un nombre al objeto que captura la salida
     * Nos permite acceder a lo que se imprimió

3. **El Bloque `with`**
   - Crea un contexto temporal para la prueba
   - Asegura que la salida estándar se restaure después
   - Todo lo que está dentro del `with` usa la salida falsa

4. **Verificación del Resultado**
   - `fake_output.getvalue()`: 
     * Obtiene todo lo que se imprimió
     * Incluye saltos de línea y espacios

   - `.strip()`:
     * Elimina espacios en blanco al inicio y final
     * Elimina saltos de línea
     * Asegura una comparación limpia

   - `"45.0"`:
     * El valor exacto que esperamos ver impreso
     * Incluye el punto decimal para números flotantes

5. **¿Por qué es Importante?**
   - Verifica no solo el cálculo sino la presentación
   - Asegura que el usuario vea el resultado correcto
   - Valida el formato de salida específico

6. **Posibles Errores que Detecta**
   - Valor incorrecto del precio final
   - Formato de impresión incorrecto
   - Falta de impresión del resultado
   - Impresión de información adicional no deseada

7. **Ventajas del Enfoque**
   - No depende de la consola real
   - Prueba reproducible y consistente
   - No afecta otras partes del programa
   - Fácil de verificar el resultado exacto

## Métodos de Assert Utilizados
- `assertEqual`: Verifica que dos valores sean iguales
- `strip()`: Elimina espacios en blanco y saltos de línea del output

## Importaciones Necesarias
```python
import unittest
from unittest.mock import patch
import io
from main import starting_price, discount_value, discount_percentage, final_price
```

## Ejecución de las Pruebas
Para ejecutar las pruebas:
```bash
python3 -m unittest test_price_calculation.py -v
```

## Resultados Esperados
- Todas las pruebas deben pasar ("OK")
- El precio inicial debe ser 50
- El descuento debe ser 5 (10% de 50)
- El precio final debe ser 45
- La salida impresa debe mostrar "45"

## Notas Adicionales
- Las pruebas verifican tanto los cálculos como la presentación del resultado
- Se usa mock para evitar dependencia de la salida estándar real
- Los valores están hardcodeados para este ejercicio específico
