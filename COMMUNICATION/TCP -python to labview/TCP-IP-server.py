import socket
import struct
import random
import time

def tcp_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 6340)
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)
    print(f"TCP server up and listening on {server_address}")

    while True:
        # Wait for a connection
        connection, client_address = server_socket.accept()
        try:
            print(f"Connection from {client_address}")

            # Send 10 samples of data
            for _ in range(10):
                # Create a vector of 10 random double numbers
                data_to_send = [random.random() for _ in range(10)]

                # Pack the vector into a binary format (struct.pack) for sending
                packed_data = struct.pack('10d', *data_to_send)

                # Send the packed data to the client
                connection.sendall(packed_data)
                print(f"Sent data: {data_to_send}")

                # Optional: Delay between samples (e.g., 1 second)
                time.sleep(1)

        finally:
            # Clean up the connection
            connection.close()

if __name__ == "__main__":
    tcp_server()
