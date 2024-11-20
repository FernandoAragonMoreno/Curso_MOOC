# En un notebook, escribir un programa que pida al usuario dos números y luego imprima cuál es el mayor.

print("Este programa imprime el mayor de dos números dados por el usuario")

numero1 = float(input("Escribe el primer número: "))
numero2 = float(input("Escribe el segundo número: "))

if numero1 > numero2:
    print(f"El número mayor es {numero1}")
elif numero1 < numero2:
    print(f"El número mayor es {numero2}")
else:
    print("Los números son iguales")
