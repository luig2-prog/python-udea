# Importar librerias
import seaborn as sns
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import os

# Cargar datos
file_path = "/home/sublime-dev/dev/IA/python-udea/expo/datos_produccion.xlsx"
df = pd.read_excel(file_path)
df.head(5)

# Seleccionar variables
variable_x = "Tamaño (mt2)"
variable_y = "Precio de Venta ($)"
# convertir la columna string en float 'Precio de Venta ($)'
df['Precio de Venta ($)'] = df['Precio de Venta ($)'].replace({r'\$': '', ',': ''}, regex=True).astype(float)

# convertir la columna 'Precio de Arriendo ($)':
df['Precio de Arriendo ($)'] = df['Precio de Arriendo ($)'].replace({r'\$': '', ',': ''}, regex=True).astype(float)

# Verificamos el resultado
print(df.head(5))

# Generar análisis
modelo = LinearRegression() # creamos el modelo
modelo.fit(df[[variable_x]], df[variable_y]) #entrenamos el modelo
# Obtener la ecuación de la recta
# y=mx+b
print ('Ecuación de la recta: y = ', round(modelo.coef_[0],3),'x + ', round(modelo.intercept_,3))#obtenemos la ecuación de la recta
#  Evaluar el modelo
print ('Coeficiente de correlación: ', round(np.corrcoef(df[variable_x], df[variable_y])[0,1], 3))#obtenemos el coeficiente de correlación
print ('Coeficiente de determinación: ', round(r2_score(df[variable_y], modelo.predict(df[[variable_x]])), 3))#obtenemos el coeficiente de determinación
# Gráfica con intervalo de confianza
plt.figure(figsize=(10, 6))
sns.regplot(x=df[variable_x], y=df[variable_y], ci=95, line_kws={"color": "red"}, scatter_kws={"color": "black"})
plt.title('Regresión lineal simple con intervalo de confianza al 95%')
plt.savefig('regresion_lineal.png')
plt.close()

# Definir el dato predictor (por ejemplo, el tamaño del inmueble en m²)

dato_predictor = int(input("Ingrese los m² del inmueble: "))  # Por ejemplo, 100 m²

# Convertir el dato predictor en un DataFrame
nuevas_caracteristicas = pd.DataFrame([dato_predictor], columns=[variable_x])

# Realizar la predicción con el modelo entrenado
precio_prediccion = modelo.predict(nuevas_caracteristicas)

# Mostrar el resultado de la predicción
print(f'La predicción del precio de un inmueble con {nuevas_caracteristicas.iloc[0, 0]} m² es: ${round(precio_prediccion[0], 2)}')