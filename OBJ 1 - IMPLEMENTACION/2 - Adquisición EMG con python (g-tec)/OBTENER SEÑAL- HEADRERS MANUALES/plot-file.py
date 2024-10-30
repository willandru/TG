import pandas as pd
import matplotlib.pyplot as plt

# Cargar los archivos CSV
file_path1 = "PRUEBA_FRUNSIR_1_5S.csv"
file_path2 = "PRUEBA_ABRIR_1_5S.csv"
file_path3 = "PRUEBA_NADA_1_5S.csv"
data1 = pd.read_csv(file_path1, header=None)
data2 = pd.read_csv(file_path2, header=None)
data3 = pd.read_csv(file_path3, header=None)

# Seleccionar y concatenar las primeras 5 filas en un solo vector para cada archivo
concatenated_vector1 = data1.iloc[:30].values.flatten()
concatenated_vector2 = data2.iloc[:30].values.flatten()
concatenated_vector3 = data3.iloc[:30].values.flatten()

# Graficar los tres vectores concatenados en el mismo gráfico
plt.figure(figsize=(10, 6))
plt.plot(concatenated_vector1, label="PRUEBA_FRUNSIR_1_5S")
plt.plot(concatenated_vector2, label="PRUEBA_ABRIR_3_5S")
plt.plot(concatenated_vector3, label="PRUEBA_NADA_2_5S")
plt.xlabel("Puntos de Datos")
plt.ylabel("Valor")
plt.title("Vectores concatenados de las primeras 5 filas de los tres archivos")
plt.legend()
plt.show()
