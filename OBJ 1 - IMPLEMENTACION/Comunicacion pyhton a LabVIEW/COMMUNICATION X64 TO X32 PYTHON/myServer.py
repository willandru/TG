#myServer.py
import socket
import struct
import random
import time

# Definir parámetros del servidor
HOST = socket.gethostname()
PORT = 1234

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"Servidor escuchando en {HOST}:{PORT}...")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Conexión establecida desde {addr}")

            # Bucle para enviar un número en cada iteración
            for _ in range(50):
                # Generar un número aleatorio (double)
                data = random.random()

                # Empaquetar el número en bytes
                data_bytes = struct.pack("d", data)

                # Enviar los datos al cliente
                conn.sendall(data_bytes)

                # Simular un tiempo de espera antes de la siguiente iteración (opcional)
                time.sleep(1)  # Ajustar según sea necesario

            print("Datos enviados. Cerrando conexión.")

if __name__ == "__main__":
    start_server()
