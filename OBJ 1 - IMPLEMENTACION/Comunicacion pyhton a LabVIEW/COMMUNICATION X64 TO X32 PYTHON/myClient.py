#myClient.py

import socket
import struct

# Definir parámetros del servidor
HOST = socket.gethostname()
PORT = 1234

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print(f"Conectado al servidor en {HOST}:{PORT}")

        # Recibir datos del servidor
        for _ in range(50):
            data_bytes = client_socket.recv(4096)

            # Desempaquetar los datos en números (suponiendo que son números de doble precisión)
            data = struct.unpack("d", data_bytes)[0]  # [0] para obtener el primer elemento de la tupla

            # Imprimir el número recibido
            print(f"Número recibido: {data}")

if __name__ == "__main__":
    start_client()
