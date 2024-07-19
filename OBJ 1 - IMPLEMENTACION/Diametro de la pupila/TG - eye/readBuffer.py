import struct
import time

# Abre el archivo binario en modo lectura binaria
with open('mybinary.bin', 'rb') as file:
    while True:
        # Lee 8 bytes (double-precision) del archivo
        data = file.read(8)
        
        # Verifica si se ha alcanzado el final del archivo
        if not data:
            break
        
        # Desempaqueta los bytes en un número de punto flotante de doble precisión
        signalX = struct.unpack('d', data)[0]
        
        # Imprime el número de punto flotante de doble precisión
        print(signalX)
        
        # Pausa para controlar la velocidad de transmisión de datos
        time.sleep(0.1)
