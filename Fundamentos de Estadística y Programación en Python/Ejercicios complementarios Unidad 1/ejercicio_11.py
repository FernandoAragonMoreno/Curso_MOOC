# Calcula el coeficiente de variación para los datos: [10, 15, 20, 25, 30].

datos = [10, 15, 20, 25, 30]
print(f"Los datos son: {datos}")

# Media
media = sum(datos) / len(datos)
print(f"La media es: {media}")

# Desviación estándar
varianza = sum((i - media) ** 2 for i in datos) / len(datos)
desviacion_estandar = varianza ** 0.5
print(f"La desviación estándar es: {desviacion_estandar}")

# Coeficiente de variación
coeficiente_variacion = (desviacion_estandar / media) * 100
print(f"El coeficiente de variación es: {coeficiente_variacion}%")

