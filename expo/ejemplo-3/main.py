# Importar librerias
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Cargar datos
file_path = os.path.join(os.path.dirname(__file__), "datos_autos.xlsx")
df = pd.read_excel(file_path)

# Mostrar las primeras filas
print("Primeras 5 filas del dataset:")
print(df.head(5))
print("\n")

# Análisis exploratorio básico
print("Estadísticas descriptivas:")
print(df.describe())
print("\n")

# Visualizar correlaciones
plt.figure(figsize=(12, 8))
correlation_matrix = df[['Año', 'Kilometraje', 'Cilindrada', 'Precio ($)']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Matriz de Correlación')
plt.savefig('correlacion_autos.png')
plt.close()

# Preparar datos para el modelo
# Seleccionar características numéricas para el modelo
X = df[['Año', 'Kilometraje', 'Cilindrada']]
y = df['Precio ($)']

# Dividir datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Mostrar coeficientes del modelo
print("Coeficientes del modelo:")
for feature, coef in zip(X.columns, modelo.coef_):
    print(f"{feature}: {round(coef, 2)}")
print(f"Intercepto: {round(modelo.intercept_, 2)}")
print("\n")

# Ecuación del modelo
print("Ecuación del modelo:")
ecuacion = f"Precio = {round(modelo.coef_[0], 2)} × Año + {round(modelo.coef_[1], 2)} × Kilometraje + {round(modelo.coef_[2], 2)} × Cilindrada + {round(modelo.intercept_, 2)}"
print(ecuacion)
print("\n")

# Evaluar el modelo
y_pred = modelo.predict(X_test)
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"Coeficiente de determinación (R²): {round(r2, 4)}")
print(f"Error cuadrático medio (RMSE): {round(rmse, 2)}")
print("\n")

# Visualizar predicciones vs valores reales
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Precio Real ($)')
plt.ylabel('Precio Predicho ($)')
plt.title('Predicciones vs Valores Reales')
plt.savefig('predicciones_autos.png')
plt.close()

# Función para predecir el precio de un auto
def predecir_precio_auto(año, kilometraje, cilindrada):
    datos = pd.DataFrame({
        'Año': [año],
        'Kilometraje': [kilometraje],
        'Cilindrada': [cilindrada]
    })
    prediccion = modelo.predict(datos)[0]
    return prediccion

# Ejemplo de predicción
print("Ejemplo de predicción:")
año_ejemplo = 2020
kilometraje_ejemplo = 50000
cilindrada_ejemplo = 2.0

precio_predicho = predecir_precio_auto(año_ejemplo, kilometraje_ejemplo, cilindrada_ejemplo)
print(f"Para un auto de {año_ejemplo} con {kilometraje_ejemplo} km y motor de {cilindrada_ejemplo}L, el precio estimado es: ${round(precio_predicho, 2)}")

# Permitir al usuario ingresar sus propios datos
print("\nIngrese los datos del auto para predecir su precio:")
año_usuario = int(input("Año del auto (2010-2023): "))
kilometraje_usuario = int(input("Kilometraje: "))
cilindrada_usuario = float(input("Cilindrada (1.4-4.0): "))

precio_usuario = predecir_precio_auto(año_usuario, kilometraje_usuario, cilindrada_usuario)
print(f"\nEl precio estimado para su auto es: ${round(precio_usuario, 2)}") 