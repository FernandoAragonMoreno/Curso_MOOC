# Crear una función que tome una lista de números como argumento y devuelva la media de los números.

def media_lista(lista):
    return sum(lista) / len(lista)

print(f"la media de los elementos de la lista [1, 2, 3, 4, 5] es: {media_lista([1, 2, 3, 4, 5])}") # 3.0
print(f"la media de los elementos de la lista [10, 20, 30, 40, 50] es: {media_lista([10, 20, 30, 40, 50])}") # 30.0