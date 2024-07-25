#reciveDatax32
import socket
import json

def start_client():
    """Starts the client to receive data from the server."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 65432))  # Connect to the server

    try:
        while True:
            data = b''
            while True:
                chunk = client_socket.recv(4096)
                if not chunk:
                    break
                data += chunk

                # Check for end of data
                if data.endswith(b'\n'):
                    break

            # Decode received data
            try:
                data_json = json.loads(data[:-1].decode('utf-8'))  # Remove newline character before decoding
                print("Received data:", data_json)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
    except KeyboardInterrupt:
        print("Interrupted. Closing client...")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()
