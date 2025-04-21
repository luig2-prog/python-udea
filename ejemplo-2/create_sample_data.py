import pandas as pd
import numpy as np

# Establecer semilla para reproducibilidad
np.random.seed(42)

# Número de muestras
n = 100

# Generar datos base con distribuciones que nos den el resultado deseado
data = {
    'Peso (kg)': np.random.normal(1300, 150, n).clip(1000, 1800),
    'Cilindrada (cc)': np.random.normal(1800, 200, n).clip(1200, 2500),
    'Tipo Motor': np.random.choice([0, 1], n, p=[0.4, 0.6])
}

# Crear DataFrame
df = pd.DataFrame(data)

# Crear la columna de consumo con la relación deseada
# Ajustamos los coeficientes para obtener ~6.0 L/100km para el caso específico
consumo_base = (
    0.0025 * df['Peso (kg)'] +  # Ajustado para el caso objetivo
    0.001 * df['Cilindrada (cc)'] +  # Ajustado para el caso objetivo
    -1.0 * df['Tipo Motor'] +  # Efecto del diésel
    2.5  # Término independiente ajustado
)

# Añadir ruido aleatorio pequeño
ruido = np.random.normal(0, 0.2, n)
df['Consumo (L/100km)'] = consumo_base + ruido

# Asegurar que los consumos sean realistas (entre 4 y 12 L/100km)
df['Consumo (L/100km)'] = df['Consumo (L/100km)'].clip(4, 12)

# Redondear valores
df['Peso (kg)'] = df['Peso (kg)'].round(0)
df['Cilindrada (cc)'] = df['Cilindrada (cc)'].round(0)
df['Consumo (L/100km)'] = df['Consumo (L/100km)'].round(1)

# Convertir tipo de motor a categoría
df['Tipo Motor'] = df['Tipo Motor'].map({0: 'Gasolina', 1: 'Diésel'})

# Añadir varios casos similares al objetivo para dar más peso a ese punto
casos_objetivo = pd.DataFrame({
    'Peso (kg)': [1300, 1290, 1310, 1300, 1295],
    'Cilindrada (cc)': [1800, 1790, 1810, 1800, 1795],
    'Tipo Motor': ['Diésel'] * 5,
    'Consumo (L/100km)': [6.0, 5.9, 6.1, 6.0, 6.0]
})

df = pd.concat([df, casos_objetivo], ignore_index=True)

# Verificar la predicción para nuestro caso específico
caso_ejemplo = df[
    (df['Peso (kg)'].between(1250, 1350)) & 
    (df['Cilindrada (cc)'].between(1750, 1850)) & 
    (df['Tipo Motor'] == 'Diésel')
]

if not caso_ejemplo.empty:
    print("\nCasos similares al ejemplo objetivo (1300kg, 1800cc, Diésel):")
    print(caso_ejemplo)
    print(f"\nConsumo promedio para casos similares: {caso_ejemplo['Consumo (L/100km)'].mean():.1f} L/100km")

# Guardar a Excel
df.to_excel('datos_consumo.xlsx', index=False)
print("\nArchivo 'datos_consumo.xlsx' creado exitosamente!")

# Mostrar estadísticas básicas
print("\nEstadísticas descriptivas del dataset:")
print(df.describe()) 