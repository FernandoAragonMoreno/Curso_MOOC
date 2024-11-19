# Dibuja un gráfico circular que represente la distribución de colores de un conjunto de 100 M&M's (rojo, azul, verde, amarillo, marrón).

import matplotlib.pyplot as plt
from collections import Counter

# Datos
mms = ['red', 'blue', 'green', 'yellow', 'brown']

# Crear el gráfico circular
plt.pie(Counter(mms).values(), labels=Counter(mms).keys(), colors=mms, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title("Distribución de colores de 100 M&M's")
plt.show()

