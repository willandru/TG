import socket
import struct
import random
import time

# Define server parameters
HOST = 'localhost'  # Replace with your server's IP address if different
PORT = 6340
TIMEOUT = 30  # Timeout in seconds for waiting for connection

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        server_socket.settimeout(TIMEOUT)
        print(f"Server listening on {HOST}:{PORT} with timeout {TIMEOUT} seconds...")

        try:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")

                # Generate random double data (N=50)
                data = [random.random() for _ in range(50)]

                # Convert data to string (for simplicity, assuming ASCII encoding)
                data_str = ' '.join(map(str, data))

                # Send data size first
                size_bytes = struct.pack("!I", len(data_str))
                conn.sendall(size_bytes)

                # Send data itself
                conn.sendall(data_str.encode('ascii'))

                # Wait briefly before expecting client response (simulating delay)
                time.sleep(0.1)

                # Receive response from client (1 byte)
                response = conn.recv(1).decode('utf-8')

                # Close connection
                print("Data sent. Closing connection.")
        
        except socket.timeout:
            print(f"Socket timeout ({TIMEOUT} seconds) reached. No client connected.")

if __name__ == "__main__":
    start_server()
