# Crear una función que tome dos tuplas como argumentos y devuelva una nueva tupla que contenga los elementos de ambas tuplas.

def unir_tuplas(tupla1, tupla2):
    return tupla1 + tupla2

print(f"la unión de las tuplas (1, 2, 3) y (4, 5, 6) es: {unir_tuplas((1, 2, 3), (4, 5, 6))}") # (1, 2, 3, 4, 5, 6)
print(f"la unión de las tuplas (10, 20, 30) y (40, 50, 60) es: {unir_tuplas((10, 20, 30), (40, 50, 60))}") # (10, 20, 30, 40, 50, 60)