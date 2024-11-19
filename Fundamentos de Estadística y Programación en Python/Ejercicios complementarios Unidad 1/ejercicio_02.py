# Crea una tabla de frecuencias para los siguientes datos: [1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6].

datos = [1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6]
print(f"Los datos son: {datos}")

# Tabla de frecuencias
frecuencias = {}
for i in datos:
    if i in frecuencias:
        frecuencias[i] += 1
    else:
        frecuencias[i] = 1

print("Tabla de frecuencias:")

for i in frecuencias:
    print(f"Valor: {i}; Frecuencia: {frecuencias[i]}")

