import socket

def udp_server():
    # Set up the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 1111)  # Replace 'localhost' with your LabVIEW client's IP if needed
    server_socket.bind(server_address)

    print(f"UDP server up and listening on {server_address}")

    while True:
        # Prepare the message to send
        message = "Hello from Python UDP server!"

        # Send the message to the LabVIEW client
        client_address = ('127.0.0.1', 1113)  # Replace with the LabVIEW client's IP and port
        server_socket.sendto(message.encode(), client_address)


if __name__ == "__main__":
    udp_server()
