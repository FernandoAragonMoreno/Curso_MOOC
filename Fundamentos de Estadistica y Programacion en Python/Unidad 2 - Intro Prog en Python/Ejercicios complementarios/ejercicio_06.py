# En un notebook, escribir un programa que almacene en una lista el valor de al menos 20 productos que recuerde o desee.
# El programa debe imprimir cuántos productos tienen un costo mayor o igual a 20.000 pesos.

datos = [
  {'cuaderno': 10000},
  {'lápiz': 20000},
  {'esfera': 30000},
  {'PC': 20001},
  {'mouse': 10000},
  {'monitor': 15000},
  {'TV': 18000},
  {'tenis': 22000},
  {'Zapatos': 19000},
  {'Camisa': 21000},
  {'reloj': 50000},
  {'gafas': 70000},
  {'maleta': 40000},
  {'termo': 30000},
  {'mesa': 20000},
  {'llanta': 25000},
  {'carro': 27000},
  {'juego': 00000},
  {'cable': 60000},
  {'silla': 20000}
];

contador = 0
for dato in datos:
  for key, value in dato.items():
    if value >= 20000:
      contador += 1

print(f"Productos con costo mayor o igual a 20.000: {contador}")

