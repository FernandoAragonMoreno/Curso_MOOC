# Dado el conjunto de datos sobre la edad y el ingreso anual de 10 personas, calcula el coeficiente de correlación de Pearson y dibuja el diagrama de dispersión.
# Datos: Edad: [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
# Ingreso Anual: [30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000, 70000, 75000].


# Version 1.

#datos
edad = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
ingreso_anual = [30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000, 70000, 75000]

#coeficiente de correlación de Pearson
media_edad = sum(edad) / len(edad)
media_ingreso_anual = sum(ingreso_anual) / len(ingreso_anual)

numerador = sum((edad[i] - media_edad) * (ingreso_anual[i] - media_ingreso_anual) for i in range(len(edad)))
denominador = (sum((edad[i] - media_edad) ** 2 for i in range(len(edad))) * sum((ingreso_anual[i] - media_ingreso_anual) ** 2 for i in range(len(ingreso_anual))) ) ** 0.5

coeficiente_correlacion = numerador / denominador
print(f"El coeficiente de correlación de Pearson es: {coeficiente_correlacion}")


#diagrama de dispersión
import matplotlib.pyplot as plt

plt.scatter(edad, ingreso_anual, color='blue', marker='o')
plt.grid(True)
plt.title("Diagrama de dispersión")
plt.xlabel("Edad")
plt.ylabel("Ingreso Anual")
plt.show()


# Version 2.

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Datos
edad = np.array([25, 30, 35, 40, 45, 50, 55, 60, 65, 70])
ingreso_anual = np.array([30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000, 70000, 75000])

# Cálculo del coeficiente de correlación de Pearson
coef_pearson, _ = pearsonr(edad, ingreso_anual)

# Diagrama de dispersión
plt.scatter(edad, ingreso_anual, color='blue', label='Datos')
plt.plot(edad, np.poly1d(np.polyfit(edad, ingreso_anual, 1))(edad), color='red', label='Tendencia lineal')
plt.title('Diagrama de Dispersión: Edad vs Ingreso Anual')
plt.xlabel('Edad')
plt.ylabel('Ingreso Anual')
plt.legend()
plt.grid(True)
plt.show()

coef_pearson


# Version 3.

import numpy as np
import matplotlib.pyplot as plt

# Datos
edad = np.array([25, 30, 35, 40, 45, 50, 55, 60, 65, 70])
ingreso = np.array([30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000, 70000, 75000])

# Calcular el coeficiente de correlación de Pearson
coef_corr = np.corrcoef(edad, ingreso)[0, 1]

# Crear el diagrama de dispersión
plt.scatter(edad, ingreso, color='blue', label=f'Coef. Pearson = {coef_corr:.2f}')
plt.title("Diagrama de dispersión: Edad vs Ingreso Anual")
plt.xlabel("Edad")
plt.ylabel("Ingreso Anual")
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()

# Retornando el coeficiente de correlación
coef_corr
