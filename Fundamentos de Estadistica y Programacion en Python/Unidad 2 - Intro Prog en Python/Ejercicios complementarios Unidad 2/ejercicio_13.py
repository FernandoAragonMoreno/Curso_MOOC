# Crear una función que tome una lista como argumento y devuelva una nueva lista que contenga los elementos ordenados de menor a mayor.

def ordenar_lista(lista):
    return sorted(lista)

print(f"la lista [1, 2, 3, 4, 5] ordenada de menor a mayor es: {ordenar_lista([1, 2, 3, 4, 5])}") # [1, 2, 3, 4, 5]
print(f"la lista [10, 20, 30, 40, 50] ordenada de menor a mayor es: {ordenar_lista([10, 20, 30, 40, 50])}") # [10, 20, 30, 40, 50]
print(f"la lista [5, 4, 3, 2, 1] ordenada de menor a mayor es: {ordenar_lista([5, 4, 3, 2, 1])}") # [1, 2, 3, 4, 5]