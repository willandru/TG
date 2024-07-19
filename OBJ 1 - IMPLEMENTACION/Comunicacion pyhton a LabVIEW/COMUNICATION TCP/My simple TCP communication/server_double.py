import socket
import struct

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

        with conn:
            try:
                # Número de tipo double a enviar
                number_to_send = 123.456  # Puedes cambiar este valor por cualquier número de tipo double

                # Convertir el número a bytes
                number_bytes = struct.pack('d', number_to_send)

                # Enviar el número en bytes
                conn.sendall(number_bytes)
                print(f"Número '{number_to_send}' enviado a {addr}")

            except Exception as e:
                print(f"Error durante la transmisión de datos: {e}")

            print("Conexión cerrada.")

if __name__ == "__main__":
    start_server()
