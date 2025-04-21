# Importar librerías necesarias
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configurar el estilo de las gráficas de manera más simple
plt.style.use('default')
sns.set_theme()  # Usar el tema por defecto de seaborn

# Cargar datos
file_path = os.path.join(os.path.dirname(__file__), "datos_consumo.xlsx")
df = pd.read_excel(file_path)

# Convertir tipo de motor a numérico
df['Tipo Motor'] = df['Tipo Motor'].map({'Gasolina': 0, 'Diésel': 1})

# Mostrar información del dataset
print("Primeras 5 filas del dataset:")
print(df.head())
print("\nEstadísticas descriptivas:")
print(df.describe())

# Visualizar correlaciones
plt.figure(figsize=(10, 8))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Matriz de Correlación')
plt.tight_layout()
plt.savefig('correlacion_consumo.png')
plt.close()

# Preparar datos para el modelo
X = df[['Peso (kg)', 'Cilindrada (cc)', 'Tipo Motor']]
y = df['Consumo (L/100km)']

# Dividir datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Mostrar coeficientes del modelo
print("\nCoeficientes del modelo:")
for feature, coef in zip(X.columns, modelo.coef_):
    print(f"{feature}: {coef:.6f}")
print(f"Intercepto: {modelo.intercept_:.6f}")

# Crear ecuación del modelo
ecuacion = f"""
Consumo (L/100km) = {modelo.coef_[0]:.6f} × Peso (kg) + 
                    {modelo.coef_[1]:.6f} × Cilindrada (cc) + 
                    {modelo.coef_[2]:.6f} × Tipo Motor + 
                    {modelo.intercept_:.6f}
"""
print("\nEcuación del modelo:")
print(ecuacion)

# Evaluar el modelo
y_pred = modelo.predict(X_test)
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("\nMétricas de evaluación:")
print(f"R² Score: {r2:.4f}")
print(f"RMSE: {rmse:.4f} L/100km")

# Visualizar predicciones vs valores reales
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
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
    return modelo.predict(datos)[0]

# Ejemplo de uso con el caso proporcionado
print("\nEjemplo de predicción:")
peso_ejemplo = 2000
cilindrada_ejemplo = 1000
tipo_motor_ejemplo = 1  # Diésel

consumo_predicho = predecir_consumo(peso_ejemplo, cilindrada_ejemplo, tipo_motor_ejemplo)
print(f"\nPara un vehículo con:")
print(f"- Peso: {peso_ejemplo} kg")
print(f"- Cilindrada: {cilindrada_ejemplo} cc")
print(f"- Motor: {'Diésel' if tipo_motor_ejemplo == 1 else 'Gasolina'}")
print(f"\nConsumo predicho: {consumo_predicho:.1f} L/100km")

# Interfaz interactiva para predicciones
print("\n=== Predictor de Consumo de Combustible ===")
print("\nIngrese los datos del vehículo:")

try:
    peso = float(input("Peso del vehículo (kg): "))
    cilindrada = float(input("Cilindrada del motor (cc): "))
    tipo_motor = input("Tipo de motor (Gasolina/Diésel): ").lower()
    
    # Convertir tipo de motor a valor numérico
    tipo_motor_valor = 1 if tipo_motor.startswith('d') else 0
    print(f"Tipo de motor: {tipo_motor_valor}")    
    # Realizar predicción
    consumo = predecir_consumo(peso, cilindrada, tipo_motor_valor)
    
    print(f"\nConsumo estimado: {consumo:.1f} L/100km")
    
except ValueError:
    print("Error: Por favor ingrese valores numéricos válidos para peso y cilindrada.") 