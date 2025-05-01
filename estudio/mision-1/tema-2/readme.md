# Tema 2: Historia Ciclo de vida de una aplicación de Aprendizaje de máquina

El desarrollo de una aplicación de machine learning sigue un ciclo de vida estructurado que asegura que el modelo sea efectivo, preciso y útil. 


[Introducción a Machine Learning (ML Zero to Hero, parte 1)](https://www.youtube.com/watch?v=LcXOMKE7d7A)
Hacer el curso completo:

Aprender de la misma manera como aprende un humano

Programación tradicional: Tienes datos y reglas que actuan sobre unos datos, cuando usas las reglas para procesar tus datos te da unas respuestas

Machine Learning: En vez de dar las reglas al programa, le damos los datos y respuestas y dejamos que el computador nos diga cuales son reglas

Ej: Un juego de piedra, papel y tijera; puedo tener muchas fotos de manos haciendo señas y decirle a la computadora como se ve una piedra, un papel y tijera. 

La computadora aprende los patrones

Ej 2: Tenemos el siguiente conjunto de datos:

X = -1, 0, 1, 2, 3, 4
Y = -3, -1, 1, 3, 5, 7

Hay una relación entre X y Y

Y = 2X - 1

code: 

```python
import tensorflow as tf
from tensorflow import keras
import numpy as np

# Descubra la relación
# Definimos el modelo, red neurola
# Una sola capa
model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
# Funcion de perdida y optimizador
# Al entrenar la red calcula que tan buena o mala es la estimación
# The keyword argument should be 'optimizer', not 'optimize'
model.compile(optimizer='sgd', loss='mean_squared_error')

# Datos
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

# Para por el flico 500 veces
model.fit(xs, ys, epochs=500)

# Predice el valor de Y cuando X es 10
# Convert the input to a NumPy array
print(model.predict(np.array([10.0])))
```

[google developer - Te presentamos el aprendizaje automático de aprendizaje automático](https://developers.google.com/codelabs/tensorflow-1-helloworld?hl=es-419#0)

[Coding TensorFlow](https://www.youtube.com/playlist?list=PLQY2H8rRoyvwLbzbnKJ59NkZvQAW9wLbx)

[Coding TensorFlow en Español](https://www.youtube.com/playlist?list=PLQY2H8rRoyvz3rEFpW2I3gPSru5xm8Bf7)

## 1. Identificación del problema 

La primera fase en el ciclo de vida de una aplicación de aprendizaje de máquina es la identificación del problema que se quiere resolver. Esto implica definir claramente el objetivo del proyecto y determinar cómo el aprendizaje de máquina puede ayudar a alcanzar este objetivo.

Ejemplo: Una empresa minorista puede querer predecir qué productos serán más populares en la próxima temporada para optimizar su inventario. El problema aquí es "predecir la demanda del producto."

## 2. Recolección de Datos

Una vez identificado el problema, la siguiente fase es la recolección de datos. Estos datos serán utilizados para entrenar el modelo. Es importante asegurarse de que los datos sean relevantes, precisos y representativos del problema que se está tratando de resolver.

Ejemplo: La empresa minorista recolecta datos históricos de ventas, datos de tendencias de búsqueda en línea, datos demográficos de clientes, y datos de campañas de marketing pasadas.

## 3. Preparación de Datos

Los datos crudos raramente están listos para ser usados directamente para el entrenamiento del modelo. La preparación de datos implica limpiar los datos, manejar los valores faltantes, normalizar y escalar las características, y dividir los datos en conjuntos de entrenamiento y prueba.

Ejemplo: La empresa limpia su conjunto de datos eliminando duplicados, manejando valores faltantes (por ejemplo, usando la imputación), y normalizando las características como precios y cantidades vendidas.

## 4. Ingeniería de Modelos

En esta fase, se seleccionan y entrenan modelos de aprendizaje de máquina utilizando los datos preparados. Esta etapa puede incluir la selección de algoritmos, la creación de características (feature engineering), y la realización de ajustes de hiperparámetros para optimizar el rendimiento del modelo.

Ejemplo: La empresa experimenta con varios algoritmos de regresión y árboles de decisión para encontrar el modelo que mejor predice la demanda de productos. También crea nuevas características basadas en datos de estacionalidad y tendencias de marketing.

## 5. Evaluación del Modelo

Una vez que el modelo ha sido entrenado, es crucial evaluar su desempeño. Esto implica medir la precisión, la exactitud, el recall, la F1-score, entre otras métricas, usando el conjunto de prueba. La evaluación ayuda a determinar si el modelo es suficientemente bueno para ser desplegado.

Ejemplo: La empresa usa métricas como el error cuadrático medio (MSE) y la R-cuadrada para evaluar la precisión de sus modelos de predicción de demanda. Comparan estas métricas para seleccionar el mejor modelo.

[¿Cómo seleccionar el MEJOR MODELO en un problema de Machine Learning?](https://www.youtube.com/watch?v=HSon9k2-kdw&t=1s)

Parámetros: Variables numericas internas que el modelo aprende duránte el modelo

Hiper-parámetros: Variables numéricas externas que se deben fijar al momento de programar dicho algoritmo

Afinación de hiper-parámetros, nos permite encontrar los valores mas adecuados que deben tener los hiper-parámetros para lograr generar las mejores predicciones posibles

Grid Search:

Random search: 

Para entrenar como para ajustar h-p, podemos usar los sets de entrenamiento, validación y prueba o usando la validación cruzada

Problema a resolver: 

Eficiencia de consumo de un vehiculo, como es un número, quiere decir que es una tarea de regresión. 

Pasos para seleccionar el modelo:

1. Definir la métrica de desempeño: formula matematica que compara el valor predicho con el valor real de la data con la que se entrenó el modelo

RMSE: 

2. Modelo de candidatos: 

Maquina de soporte vectorial: 
Bosque aleatorio
Red neuronal

3. Entrenar, afinar y validar el modelo:

Entrenarlo: encontrar los parámetros
Afinarlo: Set de hiper-parámetros
Validarlos: Calcular su RMSE

4. Seleccionar el mejor modelo: el que genere las mejores predicciones posibles

## 6. Despliegue

Desplegar el modelo significa ponerlo en producción para que pueda ser utilizado en el entorno real. Esto puede implicar la integración del modelo en aplicaciones existentes, la creación de APIs, y la configuración de infraestructura para manejar las predicciones en tiempo real.

Ejemplo: La empresa despliega el modelo de predicción de demanda en su sistema de gestión de inventario, permitiendo a los gerentes de tienda ver las predicciones y ajustar los pedidos de inventario en consecuencia.

[El DESPLIEGUE en el Machine Learning (MLOps)](https://www.youtube.com/watch?v=9eqLtaY_hqY)

Llevarlo, de la etapa de desarrollo a la etapa de producción para llevarlo a un usuario final

1. 

2. Requerimiento de diseño: Tipo de predicción (inferencia): 

En tiempo real:  Generadas y entregadas al usuario en el menor tiempo posible, ej: Google Translate

Por lotes: Se procesa una gran cantidad de datos de entrada y el modelo genera las predicciones de forma asincrona, ej: Predicciones de netflix

Latencia: Tiempo de respuesta requerido, lo más pequeña posible, gestión de ingresos 

Rendimiento: N de solicitudes/segundos

3. Alternativas: 

Nube: Servidores remotos, a traves de internet, cuando usamos modelos complejos, cuando la laterncia no es un problema o cuando no es asincrona

Se puede almacenar en una BD

Con una REST API: Baja latencia

On-the-edge: Limitadas capacitad de computo, modelos no complejo, bajo nivel de latencia, temas de seguridad

4. Herramientas:

Local: Flask, FastAPI, TensorFlow Serving, TorchServer
Mobile: TensorFlow Lite, Pytoch Mobile

out-of-the-box: 

Streamlit, servicio gratuito nube. No modelos complejos

AWS, Azure, Google Cloud -> se pueden desplegar las herramientas locales



## 7. Mantenimiento y Actualización

El ciclo de vida de una aplicación de aprendizaje de máquina no termina con el despliegue. Es importante monitorear el desempeño del modelo en producción y realizar actualizaciones periódicas para mantener su precisión y relevancia. Esto puede implicar reentrenar el modelo con nuevos datos o ajustar sus parámetros.

Ejemplo: La empresa monitorea las predicciones del modelo y las compara con las ventas reales. Si el desempeño del modelo disminuye, recolectan nuevos datos y reentrenan el modelo para mejorar su precisión.

Este ciclo de vida asegura que las aplicaciones de aprendizaje de máquina sean desarrolladas de manera sistemática y efectiva, permitiendo a las organizaciones aprovechar al máximo el potencial de esta tecnología.

[El MONITOREO en el Machine Learning (MLOps)](https://www.youtube.com/watch?v=LnCT7Z-6eXY)



Material complementario: 

[¿Qué hace un MLOps? Antonio Feregrino](https://www.youtube.com/live/Cpvq0kAJShw)

[Ciclo de Vida de los Modelos de Machine Learning](https://www.youtube.com/watch?v=c21Pu7C585U)


