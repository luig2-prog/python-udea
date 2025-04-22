# Predicción de Consumo de Combustible con Regresión Lineal Múltiple

Este proyecto implementa un modelo de regresión lineal múltiple para predecir el consumo de combustible de vehículos (en L/100km) basado en sus características físicas y mecánicas.

## Descripción

El proyecto utiliza técnicas de machine learning para crear un modelo predictivo que estima el consumo de combustible de un vehículo basándose en tres características principales:

- Peso del vehículo (kg)
- Cilindrada del motor (cc)
- Tipo de motor (Gasolina/Diésel)

## Fórmula del Modelo

La ecuación general del modelo es:

```
Consumo = a × Peso + b × Cilindrada + c × Tipo de motor + d

Donde:
- Consumo: Litros por 100 kilómetros (L/100km)
- Peso: en kilogramos (kg)
- Cilindrada: en centímetros cúbicos (cc)
- Tipo de motor: variable binaria (0 para Gasolina, 1 para Diésel)
- a, b, c: coeficientes del modelo
- d: término independiente (intercepto)
```

## Características del Proyecto

- Generación de datos sintéticos realistas con correlaciones basadas en principios físicos
- Análisis exploratorio de datos con visualizaciones
- Implementación de regresión lineal múltiple
- Evaluación del modelo con métricas R² y RMSE
- Visualizaciones de correlaciones y predicciones
- Interfaz interactiva para realizar predicciones

## Archivos del Proyecto

- `create_sample_data.py`: Script para generar datos sintéticos de vehículos
- `main.py`: Script principal que implementa el modelo de regresión
- `datos_consumo.xlsx`: Dataset generado con información de vehículos
- `correlacion_consumo.png`: Visualización de la matriz de correlación
- `predicciones_consumo.png`: Gráfico de predicciones vs valores reales

## Requisitos

```bash
pandas
numpy
scikit-learn
matplotlib
seaborn
openpyxl
```

Instalación:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn openpyxl
```

## Uso

1. Generar datos de entrenamiento:

```bash
python create_sample_data.py
```

2. Ejecutar el modelo:

```bash
python main.py
```

3. Seguir las instrucciones en pantalla para ingresar los datos del vehículo y obtener una predicción de consumo.

## Aplicaciones Prácticas

Este modelo puede ser utilizado para:

- Diseño y desarrollo de vehículos
- Optimización de eficiencia de combustible
- Comparación de diferentes configuraciones de vehículos
- Estimación de costos operativos
- Evaluación de impacto ambiental

## Ejemplo de Uso

Para un vehículo con las siguientes características:

- Peso: 1300 kg
- Cilindrada: 1800 cc
- Motor: Diésel

El modelo predecirá su consumo en L/100km.

## Limitaciones y Consideraciones

1. **Datos Sintéticos**: El modelo usa datos generados que, aunque realistas, son simplificaciones del mundo real.

2. **Linealidad**: El modelo asume relaciones lineales entre las variables, lo cual es una simplificación.

3. **Variables Limitadas**: Existen otros factores que afectan el consumo:

   - Aerodinámica
   - Condiciones de manejo
   - Estado del vehículo
   - Condiciones ambientales

4. **Rango de Aplicación**: El modelo es más preciso dentro del rango de datos de entrenamiento:
   - Peso: 800-2500 kg
   - Cilindrada: 1000-3500 cc

## Mejoras Futuras

1. Incorporar más variables:

   - Coeficiente aerodinámico
   - Relación de transmisión
   - Edad del vehículo

2. Implementar modelos no lineales

3. Añadir datos reales de fabricantes

4. Incluir efectos de condiciones ambientales

## Contribuciones

Se aceptan contribuciones para mejorar el modelo. Algunas áreas de mejora:

- Añadir más variables predictoras
- Mejorar la generación de datos sintéticos
- Implementar validación cruzada
- Añadir tests unitarios

# Notas:

`df.describe()`

Genera estadísticas descriptivas de todas las columnas numéricas:

- `count` (Número de datos):
Cuenta cuántas observaciones válidas hay en cada columna
Útil para detectar datos faltantes

Ejemplo: Si tienes 100 vehículos pero count=98, significa que faltan datos de 2 vehículos

- `mean` (Promedio)

Suma de todos los valores dividida por el número de observaciones
Representa el valor "típico" o central

Ejemplo: Si el consumo medio es 6.5 L/100km, es el consumo "típico" de los vehículos

- `std` (Desviación estándar)

Mide qué tan dispersos están los datos respecto al promedio
Valores más altos indican mayor dispersión

Ejemplo: Una std de 1.5 L/100km en consumo significa que la mayoría de valores están entre ±1.5L del promedio

- `min` (Valor mínimo)

El valor más bajo en los datos
Útil para detectar valores extremos o errores

Ejemplo: El consumo más bajo registrado en L/100km

- `25%` (Primer cuartil)

El valor por debajo del cual está el 25% de las observaciones
Marca el límite inferior del "rango normal"

Ejemplo: 25% de los vehículos consumen menos que este valor

- `50%` (Mediana)
El valor que divide el conjunto de datos en dos mitades
Más robusta que la media para datos con valores extremos

Ejemplo: La mitad de los vehículos consume menos que este valor

- `75%` (Tercer cuartil)

El valor por debajo del cual está el 75% de las observaciones
Marca el límite superior del "rango normal"

Ejemplo: 75% de los vehículos consumen menos que este valor

- `max` (Valor máximo)

El valor más alto en los datos
Útil para detectar valores extremos o errores

Ejemplo: El consumo más alto registrado en L/100km



----

`Intercepto (modelo.intercept_)`:

Es el valor base del consumo

El consumo cuando todas las variables son 0
