import socket
import json
import numpy as np
import time

def generate_random_data():
    """Generates a 1D array of 256 random data points."""
    return np.random.rand(256).tolist()  # Convert to a 1D list

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
            if conn is None:
                conn, addr = server_socket.accept()
                print(f'Connected by {addr}')

            data = generate_random_data()  # Generate 1D array data
            serialized_data = json.dumps(data).encode('utf-8')

            if conn:
                try:
                    conn.sendall(serialized_data + b'\n')  # Send data with newline delimiter
                    print("Sent data:", data)
                except (ConnectionAbortedError, ConnectionResetError, BrokenPipeError) as e:
                    print(f"Connection error: {e}. Waiting for new connection...")
                    conn.close()
                    conn = None
            time.sleep(1)  # Adjust this delay based on your requirements
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
