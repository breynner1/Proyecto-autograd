import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

#añadimos los valores de X y Y
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 32, 15, 16]
y = [10, 15, 20, 42, 2, 2, 2, 2, 39, 44, 84, 24, 66, 15, 36, 24]

#creamos el grafico de dispaercion de los puntos
plt.scatter(x, y)

#ajustamos el grado de regrecion polinomica a 2
model = np.poly1d(np.polyfit(x, y, 2))

#añadimos la lienea del polinomio ajustada al grafico de dispercion
polyline = np.linspace(1, 60, 50)
plt.scatter(x, y)
plt.plot(polyline, model(polyline))
plt.show()
print(model)


