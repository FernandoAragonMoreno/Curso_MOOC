# Calcula el rango para el siguiente conjunto de datos: [5, 10, 15, 20, 25].

# Version 1
datos = [5, 10, 15, 20, 25]
print(f"Los datos son: {datos}")

rango = max(datos) - min(datos)
print(f"El rango es: {rango}")


# Version 2
def calcular_rango(numeros):
    return max(numeros) - min(numeros)

rango = calcular_rango(datos)
print(f"El rango por funcion es: {rango}")