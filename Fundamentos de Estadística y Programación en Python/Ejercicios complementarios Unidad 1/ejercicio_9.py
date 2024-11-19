# Calcula el primer y tercer cuartil del siguiente conjunto de datos: [7, 15, 36, 39, 40, 41, 42, 43, 47, 49].

# Version 1.

import numpy as np

datos = [7, 15, 36, 39, 40, 41, 42, 43, 47, 49]
print(f"Los datos son: {datos}")

q1 = np.quantile(datos, 0.25)  # First quartile (25%)
q3 = np.quantile(datos, 0.75)  # Third quartile (75%)

print("Q1:", q1)
print("Q3:", q3)


# Version 2.

import pandas as pd # type: ignore

data = [7, 15, 36, 39, 40, 41, 42, 43, 47, 49]
series = pd.Series(data)
q1 = series.quantile(0.25)  # First quartile
q3 = series.quantile(0.75)  # Third quartile

print("Q1:", q1)
print("Q3:", q3)
