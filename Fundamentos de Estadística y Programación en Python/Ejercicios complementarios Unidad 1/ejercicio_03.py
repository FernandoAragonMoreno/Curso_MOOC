# Dado el conjunto de datos [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],
# crea una tabla de frecuencias acumuladas.

datos = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(f"Los datos son: {datos}")

# Tabla de frecuencias acumuladas

frecuencias = {}
for i in datos:
    if i in frecuencias:
        frecuencias[i] += 1
    else:
        frecuencias[i] = 1

print("Tabla de frecuencias acumuladas:")

acumulado = 0
for i in frecuencias:
    acumulado += frecuencias[i]
    print(f"Valor: {i}; Frecuencia Absoluta: {frecuencias[i]}; Frecuencia acumulada: {acumulado}")



