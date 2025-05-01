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