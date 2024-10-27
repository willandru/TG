import socket
import struct
import random
import time

# Server configuration
HOST = 'localhost'  # or your LabVIEW IP
PORT = 1234

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"Server listening on {HOST}:{PORT}...")

        conn, addr = server_socket.accept()
        print(f"Connection established from {addr}")

        try:
            while True:
                # Generate a random integer (0, 1, or 2)
                number = random.randint(0, 2)
                print(f"Sending number: {number}")

                # Convert the integer to bytes (using integer format)
                number_bytes = struct.pack("!I", number)  # Use "!I" for unsigned int

                # Send the number
                conn.sendall(number_bytes)

                # Wait for one second before sending the next number
                time.sleep(0.1)

        except Exception as e:
            print(f"Error during data transmission: {e}")
        finally:
            print("Closing connection...")
            conn.close()

if __name__ == "__main__":
    start_server()
