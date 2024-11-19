# Dados los siguientes datos: [3, 7, 8, 5, 12, 14, 21, 13, 18, 15],
# calcula la media, mediana y moda.

datos = [3, 7, 8, 5, 12, 14, 21, 13, 18, 15]
print(f"Los datos son: {datos}")

# Media
media = sum(datos) / len(datos)
print(f"La media es: {media}")

# Mediana
datos.sort()
if len(datos) % 2 == 0:
    mediana = (datos[len(datos)//2 - 1] + datos[len(datos)//2]) / 2
else:
    mediana = datos[len(datos)//2 + 1]
print(f"La mediana es: {mediana}")

# Moda
repeticiones = 0
for i in datos:
    apariciones = datos.count(i)
    if apariciones > repeticiones:
        repeticiones = apariciones

moda = []
for i in datos:
    apariciones = datos.count(i)
    if apariciones == repeticiones and i not in moda:
        moda.append(i)

if moda.count(i) == datos.count(i):
    print("No hay una moda. Este conjunto de datos es amodal.")
elif len(moda) == 1:
    print(f"La moda es: {moda} Este conjunto de datos es unimodal.")
elif len(moda) > 1:
    print(f"La moda es: {moda} Este conjunto de datos es multimodal.")