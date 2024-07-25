import socket

# Configuración del servidor
HOST = 'localhost'  # Dirección del servidor
PORT = 1234         # Puerto en el que escucha el servidor

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"Servidor escuchando en {HOST}:{PORT}...")

        conn, addr = server_socket.accept()
        print(f"Conexión establecida desde {addr}")

        with conn:
            try:
                # Mensaje a enviar
                message = "hello"
                # Convertir el mensaje a bytes
                message_bytes = message.encode('utf-8')
                # Enviar el mensaje
                conn.sendall(message_bytes)
                print(f"Mensaje '{message}' enviado a {addr}")

            except Exception as e:
                print(f"Error durante la transmisión de datos: {e}")

            print("Conexión cerrada.")

if __name__ == "__main__":
    start_server()
