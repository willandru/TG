# Lista con los nombres de tus archivos .txt
file_names = ['texto_limpio_1.txt', 'texto_limpio_2.txt', 'texto_limpio_3.txt', 'texto_limpio_4.txt', 'texto_limpio_5.txt']

# Archivo de salida donde se unirá todo el contenido
output_file = 'texto_final.txt'

# Abre el archivo de salida en modo de escritura
with open(output_file, 'w', encoding='utf-8') as outfile:
    # Itera sobre cada archivo de la lista
    for file_name in file_names:
        # Abre cada archivo en modo lectura
        with open(file_name, 'r', encoding='utf-8') as infile:
            # Lee el contenido y escríbelo en el archivo de salida
            outfile.write(infile.read())
            # Añade una nueva línea entre archivos (opcional)
            outfile.write("\n")
            
print("Archivos unidos correctamente en", output_file)
