import socket
import struct
import time
import numpy as np

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8089)
client.connect(server_address)

for _ in range(100):
    # Generate a new random float value
    value = np.random.rand()
    
    # Convert the float value to string and encode it
    str_value = f"{value:.6f}".encode('ascii')  # Format to 6 decimal places to ensure consistency
    size = len(str_value)

    # Send the size of the message
    client.sendall(struct.pack('i', size))

    # Send the actual data
    client.sendall(str_value)

    # Print the sent value
    print(f"Sent value: {str_value.decode('ascii')}")

    # Wait for 1 second before sending the next value
    time.sleep(1)

client.sendall(b'Enough data :) Thanks')  # Sending anything back closes the connection
client.close()
print("Connection closed.")
