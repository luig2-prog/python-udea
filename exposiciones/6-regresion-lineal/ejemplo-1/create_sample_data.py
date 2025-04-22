import pandas as pd
import numpy as np

# Create sample data
np.random.seed(42)  # For reproducibility

# Number of samples
n = 100000  # Changed from 50 to 1000

# Generate data
data = {
    'Ubicación': np.random.choice(['Robledo', 'Itagüí', 'La Candelaria', 'La Estrella', 'Envigado', 'El Poblado', 'Laureles'], n),
    'Tamaño (mt2)': np.random.randint(50, 300, n),
    'Tipo': np.random.choice(['Casa', 'Apto'], n),
    'Precio de Venta ($)': np.random.uniform(150000000, 500000000, n),
    'Precio de Arriendo ($)': np.random.uniform(1000000, 3000000, n)
}

# Create DataFrame
df = pd.DataFrame(data)

# Format currency columns
df['Precio de Venta ($)'] = df['Precio de Venta ($)'].round(2)
df['Precio de Arriendo ($)'] = df['Precio de Arriendo ($)'].round(2)

# Save to Excel
df.to_excel('datos_produccion.xlsx', index=False)
print("Sample data file 'datos_produccion.xlsx' has been created successfully with 1000 samples!") 