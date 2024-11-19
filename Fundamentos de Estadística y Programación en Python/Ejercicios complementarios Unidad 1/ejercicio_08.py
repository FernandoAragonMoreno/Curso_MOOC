# Dado el siguiente conjunto de pares de datos (x, y): [(1, 2), (2, 3), (3, 5), (4, 4), (5, 5)],
# crea un diagrama de dispersión en un plano cartesiano.

import matplotlib.pyplot as plt

# Version 1.

# Datos
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 4, 5]

plt.scatter(x, y)
plt.grid(True)
plt.title("Diagrama de dispersión")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


# version 2.

# Datos
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 4, 5]

# Crear el gráfico de dispersión
plt.scatter(x, y, color='blue', marker='o')

# Etiquetas y título
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Diagrama de dispersión')

# Mostrar el gráfico
plt.grid(True)
plt.show()