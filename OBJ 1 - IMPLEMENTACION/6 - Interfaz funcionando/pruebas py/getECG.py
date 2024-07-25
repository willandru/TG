# Crear una nueva lista para almacenar solo los valores numéricos
numeric_values = []

# Abrir el archivo y leer cada línea
with open('data.txt', 'r') as file:
    for line in file:
        # Separar la línea en palabras
        words = line.split()
        # Verificar si hay suficientes palabras en la línea
        if len(words) >= 4:
            # Obtener el valor numérico y convertirlo a flotante
            ecg_value = float(words[3])
            # Agregar el valor ECG a la lista de valores numéricos
            numeric_values.append(ecg_value)
        else:
            print("Error: la línea no tiene el formato esperado:", line)

# Si se han encontrado errores, puedes decidir cómo manejarlos, como ignorar la línea o mostrar un mensaje de advertencia.
