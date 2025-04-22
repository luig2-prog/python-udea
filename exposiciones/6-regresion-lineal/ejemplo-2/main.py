import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Cargar datos desde el excel
file_path = os.path.join(os.path.dirname(__file__), "datos_consumo.xlsx")
df = pd.read_excel(file_path)

df['Tipo Motor'] = df['Tipo Motor'].map({'Gasolina': 0, 'Diésel': 1})

print("Primeras 5 filas del dataset:")
print(df.head())
print("\nEstadísticas descriptivas:")
print(df.describe())

# Preparamos los datos para el modelo
X = df[['Peso (kg)', 'Cilindrada (cc)', 'Tipo Motor']]
y = df['Consumo (L/100km)']

# Entrenamos el modelo
modelo = LinearRegression()
modelo.fit(X, y)

print("\nCoeficientes del modelo:")
for feature, coef in zip(X.columns, modelo.coef_):
    print(f"{feature}: {coef:.6f}")
print(f"Intercepto: {modelo.intercept_:.6f}")

ecuacion = f"""
Consumo (L/100km) = {modelo.coef_[0]:.6f} × Peso (kg) + 
                    {modelo.coef_[1]:.6f} × Cilindrada (cc) + 
                    {modelo.coef_[2]:.6f} × Tipo Motor + 
                    {modelo.intercept_:.6f}
"""
print("\nEcuación del modelo:")
print(ecuacion)

# Predicciones para todos los datos
y_pred = modelo.predict(X)

plt.figure(figsize=(10, 6))
sns.regplot(x=y, y=y_pred, 
            ci=95,
            scatter_kws={'color': 'black'},
            line_kws={'color': 'red', 'linestyle': '--'})
plt.xlabel('Consumo Real (L/100km)')
plt.ylabel('Consumo Predicho (L/100km)')
plt.title('Predicciones vs Valores Reales')
plt.tight_layout()
plt.savefig('predicciones_consumo.png')
plt.close()

# Función para predecir consumo
def predecir_consumo(peso, cilindrada, tipo_motor):
    """
    Predice el consumo de combustible para un vehículo.
    
    Args:
        peso: Peso del vehículo en kg
        cilindrada: Cilindrada del motor en cc
        tipo_motor: 0 para Gasolina, 1 para Diésel
    
    Returns:
        Consumo estimado en L/100km
    """
    datos = pd.DataFrame({
        'Peso (kg)': [peso],
        'Cilindrada (cc)': [cilindrada],
        'Tipo Motor': [tipo_motor]
    })
    return modelo.predict(datos)

# Ejemplo de uso
print("\nEjemplo de predicción:")
peso_ejemplo = 2000
cilindrada_ejemplo = 1000
tipo_motor_ejemplo = 0 # Gasolina

consumo_predicho = predecir_consumo(peso_ejemplo, cilindrada_ejemplo, tipo_motor_ejemplo)
print(f"\nPara un vehículo con:")
print(f"- Peso: {peso_ejemplo} kg")
print(f"- Cilindrada: {cilindrada_ejemplo} cc")
print(f"- Motor: {'Diésel' if tipo_motor_ejemplo == 1 else 'Gasolina'}")
print(f"\nConsumo predicho: {consumo_predicho[0]:.1f} L/100km")

print("\n=== Predictor de Consumo de Combustible ===")
print("\nIngrese los datos del vehículo:")

try:
    peso = float(input("Peso del vehículo (kg): "))
    cilindrada = float(input("Cilindrada del motor (cc): "))
    tipo_motor = input("Tipo de motor (Gasolina/Diésel): ").lower()
    
    tipo_motor_valor = 1 if tipo_motor.startswith('d') else 0
    print(f"Tipo de motor: {'Diésel' if tipo_motor_valor == 1 else 'Gasolina'}")    
    consumo = predecir_consumo(peso, cilindrada, tipo_motor_valor)
    print(f"\nDataFrame resultante: {consumo}")
    print(f"\nConsumo estimado: {consumo[0]:.1f} L/100km")
    
except ValueError:
    print("Error: Por favor ingrese valores numéricos válidos para peso y cilindrada.") 