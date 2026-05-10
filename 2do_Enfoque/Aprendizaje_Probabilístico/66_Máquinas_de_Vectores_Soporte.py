from sklearn.svm import SVC


# Datos de entrenamiento
X = [
    [1, 2],
    [2, 3],
    [2, 1],
    [8, 8],
    [9, 10],
    [10, 8]
]

# Clases
y = ["A", "A", "A", "B", "B", "B"]


# Crear modelo SVM con núcleo radial (RBF)
modelo = SVC(kernel="rbf")


# Entrenar modelo
modelo.fit(X, y)


# Nuevo dato
nuevo = [[3, 3]]


# Predecir clase
prediccion = modelo.predict(nuevo)


print("Clase predicha:", prediccion[0])