import socket
import struct
import random
import time

# Configuración del servidor
HOST = 'localhost'
PORT = 1234

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"Servidor escuchando en {HOST}:{PORT}...")

        conn, addr = server_socket.accept()
        print(f"Conexión establecida desde {addr}")

        try:
            while True:
                # Generar un array de N números aleatorios de tipo double
                data = [random.uniform(0.0, 1.0) for _ in range(100)]
                print(f"Enviando datos: {data}")

                # Convertir el array a bytes
                data_bytes = struct.pack(f"!{len(data)}d", *data)

                # Enviar la longitud de los datos
                data_length = len(data_bytes)
                #conn.sendall(struct.pack('!I', data_length))

                # Enviar los datos
                conn.sendall(data_bytes)

                

                # Esperar un segundo antes de enviar el siguiente conjunto de datos
                time.sleep(1)

        except Exception as e:
            print(f"Error durante la transmisión de datos: {e}")
        finally:
            print("Cerrando conexión...")
            conn.close()

if __name__ == "__main__":
    start_server()
