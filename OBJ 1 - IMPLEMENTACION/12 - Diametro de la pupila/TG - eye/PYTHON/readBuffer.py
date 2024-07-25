import time

# Abre el archivo binario en modo lectura
with open('mybinary.bin', 'rb') as file:
    while True:
        # Lee un byte del archivo
        signalX = file.read(1)
        
        # Verifica si se ha alcanzado el final del archivo
        if not signalX:
            break
        
        # Convierte el byte a un entero
        signalX = int.from_bytes(signalX, byteorder='little', signed=True)
        
        # Imprime el entero
        print(signalX)
        
        # Pausa para controlar la velocidad de transmisión de datos
        time.sleep(0.1)
