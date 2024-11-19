# Dibuja un gráfico de barras para las frecuencias de las letras en la palabra "estadística".

import matplotlib.pyplot as plt
from collections import Counter

# Version number 1

palabra = "estadística"
frecuencias = {}
for i in palabra:
    if i in frecuencias:
        frecuencias[i] += 1
    else:
        frecuencias[i] = 1

print("Tabla de frecuencias:")
print(frecuencias)

plt.bar(frecuencias.keys(), frecuencias.values())
plt.show()


# Version number 2

# Datos
palabra = "estadística"
frecuencias = Counter(palabra)
print(frecuencias)

# Preparar datos para la gráfica
letras = list(frecuencias.keys())
conteos = list(frecuencias.values())

# Crear gráfico de barras
plt.figure(figsize=(8, 5))
plt.bar(letras, conteos, color='skyblue', edgecolor='black')
plt.title("Frecuencia de letras en la palabra 'estadística'")
plt.xlabel("Letras")
plt.ylabel("Frecuencia")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


