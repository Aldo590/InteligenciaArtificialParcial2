from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np


# Datos de entrada
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Resultados esperados
y = np.array([
    0,
    1,
    1,
    0
])


# Crear red neuronal
modelo = Sequential()

# Capa oculta
modelo.add(Dense(4, input_dim=2, activation="relu"))

# Capa de salida
modelo.add(Dense(1, activation="sigmoid"))


# Compilar modelo
modelo.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)


# Entrenar modelo
modelo.fit(X, y, epochs=200, verbose=0)


# Probar predicción
prediccion = modelo.predict(np.array([[1, 0]]))

print("Predicción:")
print(prediccion)