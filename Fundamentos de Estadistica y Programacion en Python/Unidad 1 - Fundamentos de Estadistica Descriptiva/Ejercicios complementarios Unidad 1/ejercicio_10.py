# Dibuja un histograma para el siguiente conjunto de datos: [1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 7, 8, 9, 10].

datos = [1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 7, 8, 9, 10]
print(f"Los datos son: {datos}")

import matplotlib.pyplot as plt

# Data
data = [1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 7, 8, 9, 10]

# Creating the histogram
plt.hist(data, bins=10, edgecolor='black', color='skyblue')

# Adding titles and labels
plt.title("Histograma del conjunto de datos")
plt.xlabel("Valores")
plt.ylabel("Frecuencia")

# Display the plot
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()


