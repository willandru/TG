import csv

# Abre el archivo CSV
with open('emg_6_abrir.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    
    # Lee la segunda línea (la primera línea es el encabezado)
    next(reader)  # Salta el encabezado
    segunda_linea = next(reader)  # Lee la segunda línea

    # Cuenta cuántos datos hay en la segunda línea
    conteo_datos = len(segunda_linea)

print(f"Número de datos en la segunda línea: {conteo_datos}")
