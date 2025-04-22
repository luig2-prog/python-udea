import pandas as pd
import numpy as np

# Create sample data
np.random.seed(42)  # For reproducibility

# Number of samples
n = 10000

# Generate base data
data = {
    'Peso (kg)': np.random.uniform(800, 2500, n),  # Peso entre 800kg y 2500kg
    'Cilindrada (cc)': np.random.choice(np.arange(1000, 3500, 100), n),  # Cilindradas comunes
    'Tipo Motor': np.random.choice([0, 1], n),  # 0 = Gasolina, 1 = Diésel
}

# Create DataFrame
df = pd.DataFrame(data)

# Crear consumo base y añadir efectos realistas
# Base: autos más pesados consumen más
consumo_base = 4.0 + (df['Peso (kg)'] - 800) * 0.002

# Efecto de la cilindrada: motores más grandes consumen más
consumo_base += (df['Cilindrada (cc)'] - 1000) * 0.001

# Efecto del tipo de motor: diésel suele consumir ~20% menos
consumo_base = consumo_base * (1 - df['Tipo Motor'] * 0.2)

# Añadir algo de ruido aleatorio
ruido = np.random.normal(0, 0.5, n)
df['Consumo (L/100km)'] = consumo_base + ruido

# Asegurar que no hay consumos negativos
df['Consumo (L/100km)'] = df['Consumo (L/100km)'].clip(lower=3.0)

# Redondear valores para más realismo
df['Peso (kg)'] = df['Peso (kg)'].round(0)
df['Cilindrada (cc)'] = df['Cilindrada (cc)'].round(0)
df['Consumo (L/100km)'] = df['Consumo (L/100km)'].round(1)

# Convertir tipo de motor a categoría
df['Tipo Motor'] = df['Tipo Motor'].map({0: 'Gasolina', 1: 'Diésel'})

# Save to Excel
df.to_excel('datos_consumo.xlsx', index=False)
print("Archivo 'datos_consumo.xlsx' creado exitosamente con 1000 muestras!")

# Mostrar algunas estadísticas básicas
print("\nEstadísticas descriptivas del dataset:")
print(df.describe())

# Mostrar algunos ejemplos
print("\nEjemplos de registros generados:")
print(df.head()) 