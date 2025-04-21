# Predicción de Precios de Autos con Regresión Lineal Múltiple

Este proyecto implementa un modelo de regresión lineal múltiple para predecir el precio de los autos basado en características como el año, kilometraje y cilindrada del motor.

## Descripción

Este ejemplo demuestra cómo utilizar técnicas de aprendizaje automático (machine learning) para crear un modelo predictivo que puede estimar el precio de un auto basado en sus características. A diferencia del primer ejemplo que utilizaba regresión lineal simple (una sola variable predictora), este proyecto utiliza regresión lineal múltiple para considerar varias características simultáneamente.

## Características del Proyecto

- Generación de datos sintéticos realistas con correlaciones entre variables
- Análisis exploratorio de datos con visualizaciones
- Implementación de regresión lineal múltiple
- Evaluación del modelo con métricas como R² y RMSE
- Visualización de resultados
- Interfaz interactiva para realizar predicciones

## Archivos del Proyecto

- `create_sample_data.py`: Script para generar datos sintéticos de autos
- `main.py`: Script principal que implementa el modelo de regresión lineal múltiple
- `datos_autos.xlsx`: Dataset generado con información de autos
- `correlacion_autos.png`: Visualización de la matriz de correlación
- `predicciones_autos.png`: Gráfico de predicciones vs valores reales

## Requisitos

Para ejecutar este proyecto, necesitarás las siguientes bibliotecas de Python:

```
pandas
numpy
scikit-learn
matplotlib
seaborn
openpyxl
```

Puedes instalarlas con pip:

```
pip install pandas numpy scikit-learn matplotlib seaborn openpyxl
```

## Cómo Usar

1. Primero, genera los datos sintéticos ejecutando:
   ```
   python create_sample_data.py
   ```

2. Luego, ejecuta el modelo de regresión:
   ```
   python main.py
   ```

3. Sigue las instrucciones en pantalla para ingresar los datos de un auto y obtener una predicción de precio.

## Explicación Técnica

### Regresión Lineal Múltiple

La regresión lineal múltiple es una extensión de la regresión lineal simple que permite predecir una variable dependiente (en este caso, el precio del auto) basada en múltiples variables independientes (año, kilometraje, cilindrada).

La ecuación del modelo tiene la forma:

```
y = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ + ε
```

Donde:
- y es la variable dependiente (precio)
- β₀ es el intercepto
- β₁, β₂, ..., βₙ son los coeficientes de las variables independientes
- x₁, x₂, ..., xₙ son las variables independientes
- ε es el término de error

### Evaluación del Modelo

El modelo se evalúa utilizando:
- **Coeficiente de determinación (R²)**: Indica la proporción de la varianza en la variable dependiente que es predecible a partir de las variables independientes.
- **Error cuadrático medio (RMSE)**: Mide la diferencia entre los valores predichos y los valores reales.

## Aplicaciones Prácticas

Este tipo de modelo puede ser utilizado en:
- Valuación de autos usados
- Análisis de mercado automotriz
- Ayuda en la toma de decisiones de compra/venta
- Estimación de seguros

## Limitaciones

- Los datos sintéticos no reflejan la complejidad completa del mercado real
- El modelo asume relaciones lineales entre las variables
- No considera factores cualitativos como marca, modelo, color, etc.
- No tiene en cuenta factores externos como la economía, estacionalidad, etc. 