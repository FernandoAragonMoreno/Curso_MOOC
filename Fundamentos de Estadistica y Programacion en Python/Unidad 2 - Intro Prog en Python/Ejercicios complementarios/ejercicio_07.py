# En un notebook, escribir un programa creando un diccionario cuyas claves sean los nombres de sus familiares más cercanos
# y los valores sean sus respectivas edades.
# El programa debe imprimir el número de familiares en su diccionario y la edad promedio de ellos.

familia = {"padre":60, "madre":55, "hermano":30, "hermana":25, "abuela":85, "abuelo":90}

print(f"El número de familiares en el diccionario es {len(familia)}")
print(f"La edad promedio de mis familiares es {sum(familia.values()) / len(familia)}")
