import socket
import struct
import random

# Configuración del servidor
HOST = 'localhost'  # El servidor escucha en la dirección localhost
PORT = 6340         # Puerto en el que escucha el servidor

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"Servidor escuchando en {HOST}:{PORT}...")

        conn, addr = server_socket.accept()
        print(f"Conexión establecida desde {addr}")

        with conn:
            try:
                while True:
                    # Generar un array de 50 números aleatorios de tipo double
                    data = [random.random() for _ in range(50)]

                    # Convertir el array de números a bytes (cada double es de 8 bytes)
                    data_bytes = struct.pack(f'{len(data)}d', *data)

                    # Enviar el tamaño del array en bytes (4 bytes para el tamaño)
                    size_bytes = struct.pack('I', len(data_bytes))
                    conn.sendall(size_bytes)

                    # Enviar el array completo de datos en bytes
                    conn.sendall(data_bytes)
                    print(f"Enviado array de 50 números: {data}")

                    # Leer 1 byte del cliente para saber si se debe detener
                    stop_signal = conn.recv(1)
                    if stop_signal == b'S':
                        print("Se recibió señal de detener. Cerrando conexión.")
                        break

            except Exception as e:
                print(f"Error durante la transmisión de datos: {e}")

            print("Conexión cerrada.")

if __name__ == "__main__":
    start_server()
