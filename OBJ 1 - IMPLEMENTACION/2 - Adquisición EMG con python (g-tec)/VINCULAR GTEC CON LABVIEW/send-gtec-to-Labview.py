import pygds
import socket
import struct
import time
import numpy as np

# Configuración del servidor
HOST = 'localhost'
PORT = 6340
BLOCK_SIZE = 25  # Tamaño de 1 bloque para que con 1200 Hz se envien 48 bloques por segundo.

# Inicializar pygds y el dispositivo
gNEEDaccessHeaders = [
    r"C:/Users/willa/OneDrive/Documents/gtec/gNEEDaccessClientAPI/C/GDSClientAPI.h",
    r"C:/Users/willa/OneDrive/Documents/gtec/gNEEDaccessClientAPI/C/GDSClientAPI_gHIamp.h",
    r"C:/Users/willa/OneDrive/Documents/gtec/gNEEDaccessClientAPI/C/GDSClientAPI_gUSBamp.h"
]
pygds.Initialize(gds_headers=gNEEDaccessHeaders)
device = pygds.GDS()

# Configurar el dispositivo con una tasa de muestreo y habilitar el primer canal
device.SamplingRate, device.NumberOfScans = sorted(device.GetSupportedSamplingRates()[0].items())[6]

# Activar un canal específico
for i, channel in enumerate(device.Channels):
    if i == 0:
        channel.Acquire = 1
        channel.BandpassFilterIndex = 123
        channel.NotchFilterIndex = 9
    else:
        channel.Acquire = 0
device.SetConfiguration()

# Iniciar el servidor TCP
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"Servidor escuchando en {HOST}:{PORT}...")
        conn, addr = server_socket.accept()
        print(f"Conexión establecida con {addr}")

        # Función para manejar cada bloque de datos adquiridos
        def handle_samples(samples):
            # Aplanar los datos y empaquetarlos como precisión doble
            data = np.array(samples).flatten()
            data_bytes = struct.pack(f"!{len(data)}d", *data)
            # Enviar la longitud de los datos en bytes, seguido por los datos reales
            data_length = len(data_bytes)
            conn.sendall(struct.pack('!I', data_length))
            conn.sendall(data_bytes)
            print("Bloque de datos enviado:", data)
            # Devolver True para continuar la adquisición indefinidamente
            return True
        # Adquirir y enviar bloques de datos indefinidamente
        try:
            while True:
                device.GetData(BLOCK_SIZE, more=handle_samples)
        except Exception as e:
            print(f"Error de transmisión: {e}")
        finally:
            print("Cerrando conexión...")
            conn.close()

    device.Close()
    print("Adquisición de datos completada.")

if __name__ == "__main__":
    start_server()
