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
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 65432))  # Bind to localhost and port 65432
    server_socket.listen(1)
    print("Server listening on port 65432...")

    conn = None
    while True:
        try:
            # Check for new connections
            if conn is None:
                conn, addr = server_socket.accept()
                print(f'Connected by {addr}')

            # Generate and send data
            data = generate_random_data()
            serialized_data = json.dumps(data).encode('utf-8')  # Serialize to JSON string

            # Send data if a connection exists
            if conn:
                try:
                    conn.sendall(serialized_data + b'\n')  # Send data with newline delimiter
                    print("Sent data:", data)
                except (ConnectionAbortedError, ConnectionResetError, BrokenPipeError) as e:
                    print(f"Connection error: {e}. Waiting for new connection...")
                    conn.close()
                    conn = None
            time.sleep(1)  # Wait for 1 second before sending the next data
        except KeyboardInterrupt:
            print("Interrupted. Closing server...")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")
            if conn:
                conn.close()
                conn = None

    if conn:
        conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
