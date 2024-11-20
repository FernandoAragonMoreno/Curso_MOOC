# Dado el siguiente conjunto de datos: [4, 8, 6, 5, 3, 2, 8, 9, 7, 10],
# calcula la varianza y la desviación estándar.

datos = [4, 8, 6, 5, 3, 2, 8, 9, 7, 10]
print(f"Los datos son: {datos}")

# Media
media = sum(datos) / len(datos)
print(f"La media es: {media}")

# Varianza
varianza = sum((i - media) ** 2 for i in datos) / len(datos)
print(f"La varianza es: {varianza}")

# Desviación estándar
desviacion_estandar = varianza ** 0.5
print(f"La desviación estándar es: {desviacion_estandar}")

