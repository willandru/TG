import pandas as pd
from statistics import mode

# Lista de archivos a procesar
files = ["diameters_U1.csv", "diameters_U2.csv", "diameters_U3.csv", "diameters_U4.csv"]

for file in files:
    # Leer el archivo actual
    df = pd.read_csv(file)
    
    # Convertir la columna "Diameters" a listas de enteros
    df['Diameters'] = df['Diameters'].apply(lambda x: list(map(int, x.split(', '))))
    
    # Calcular la moda de los diámetros
    df['Moda_Diameters'] = df['Diameters'].apply(lambda diameters: mode(diameters))
    
    # Guardar el DataFrame actualizado en el mismo archivo
    df.to_csv(file, index=False)
    print(f"Archivo procesado y guardado: {file}")

print("Todos los archivos han sido procesados y actualizados.")
