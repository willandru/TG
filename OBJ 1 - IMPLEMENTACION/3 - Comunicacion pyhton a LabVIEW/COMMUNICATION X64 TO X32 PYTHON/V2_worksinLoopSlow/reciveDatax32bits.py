import socket
import json
import time

def receive_data():
    """Receives data from the server and returns it as a Python object."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect(('localhost', 65432))  # Connect to the server
        print("Connected to the server.")
    except (ConnectionRefusedError, socket.error) as e:
        print(f"Connection failed: {e}. Retrying...")
        return None

    client_socket.setblocking(False)  # Set non-blocking mode
    received_data = b''
    data_json = None

    try:
        while True:
            try:
                chunk = client_socket.recv(4096)  # Attempt to receive data
                if chunk:
                    received_data += chunk

                    # Check if we have received a full message
                    if received_data.endswith(b'\n'):
                        try:
                            data_json = json.loads(received_data[:-1].decode('utf-8'))
                            print("Received data:", data_json)
                            received_data = b''  # Reset buffer after successful reception
                            return data_json
                        except json.JSONDecodeError as e:
                            print(f"Error decoding JSON: {e}")
                            received_data = b''  # Reset buffer on decode error
            except BlockingIOError:
                # No data received, continue the loop
                pass
            except socket.timeout:
                print("Timeout: No data received in the given interval.")
                break
    finally:
        client_socket.close()

def start_client():
    """Wrapper function to start the client and return data."""
    data = None
    while data is None:
        data = receive_data()
        if data is None:
            time.sleep(0.05)  # Short wait before retrying, reduce to minimal required
    return data

if __name__ == "__main__":
    print(start_client())
