import pandas as pd
import numpy as np

# Create sample data
np.random.seed(42)  # For reproducibility

# Number of samples
n = 1000

# Generate data
data = {
    'Marca': np.random.choice(['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Volkswagen', 'Nissan', 'Hyundai', 'Kia', 'Mazda', 'BMW'], n),
    'Modelo': np.random.choice(['Sedan', 'SUV', 'Hatchback', 'Pickup', 'Van', 'Coupe', 'Crossover', 'Wagon', 'Minivan', 'Truck'], n),
    'Año': np.random.randint(2010, 2023, n),
    'Kilometraje': np.random.randint(0, 200000, n),
    'Cilindrada': np.random.choice([1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.5, 3.0, 3.5, 4.0], n),
    'Transmisión': np.random.choice(['Manual', 'Automática', 'CVT', 'DCT'], n),
    'Combustible': np.random.choice(['Gasolina', 'Diesel', 'Híbrido', 'Eléctrico', 'GNC'], n),
    'Precio ($)': np.random.uniform(50000000, 200000000, n)
}

# Create DataFrame
df = pd.DataFrame(data)

# Add some correlations to make the data more realistic
# Newer cars are more expensive
df['Precio ($)'] = df['Precio ($)'] + (df['Año'] - 2010) * 5000000

# Higher mileage cars are less expensive
df['Precio ($)'] = df['Precio ($)'] - df['Kilometraje'] * 100

# Larger engines are more expensive
df['Precio ($)'] = df['Precio ($)'] + df['Cilindrada'] * 10000000

# Format currency column
df['Precio ($)'] = df['Precio ($)'].round(2)

# Save to Excel
df.to_excel('datos_autos.xlsx', index=False)
print("Sample data file 'datos_autos.xlsx' has been created successfully with 1000 samples!") 