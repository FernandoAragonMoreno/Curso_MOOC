# En un notebook, escribir un programa que calcule el área de un círculo con un radio dado por el usuario y lo imprima en la pantalla.

print("Este programa calcula el área de un círculo")
radio = float(input("Escribe el radio del círculo: "))
area = 3.14159 * (radio ** 2)

print(f"El área del círculo es {area}")