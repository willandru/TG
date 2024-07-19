#sendDatax64.py
import socket
import json
import numpy as np
import time

def generate_random_data():
    """Generates random data of shape (1, 256)."""
    return np.random.rand(1, 256).tolist()

def start_server():
    """Starts the server to send random data over a socket."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65432))  # Bind to localhost and port 65432
    server_socket.listen(1)
    print("Server listening on port 65432...")

    conn, addr = server_socket.accept()
    print('Connected by', addr)

    try:
        while True:
            data = generate_random_data()
            serialized_data = json.dumps(data).encode('utf-8')  # Serialize to JSON string
            conn.sendall(serialized_data + b'\n')  # Send data with newline delimiter
            print("Sent data:", data)
            time.sleep(1)  # Wait for 1 second before sending the next data
    except KeyboardInterrupt:
        print("Interrupted. Closing server...")
    finally:
        conn.close()
        server_socket.close()

if __name__ == "__main__":
    start_server()
