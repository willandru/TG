import socket
import struct

# Define the array of doubles (size 50)
data_array = [1.23, 4.56, 7.89, 9.01, 2.34, 5.67, 8.91, 0.12, 3.45, 6.78,
              9.87, 6.54, 3.21, 0.98, 7.65, 4.32, 1.09, 8.76, 5.43, 2.10,
              0.11, 9.88, 7.65, 5.43, 3.21, 1.09, 8.76, 6.54, 4.32, 2.10,
              1.23, 4.56, 7.89, 9.01, 2.34, 5.67, 8.91, 0.12, 3.45, 6.78,
              9.87, 6.54, 3.21, 0.98, 7.65, 4.32, 1.09, 8.76, 5.43, 2.10]

# Convert array to bytes
data_bytes = struct.pack(f"{len(data_array)}d", *data_array)

# Connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8089)  # Adjust port and address as needed
client.connect(server_address)

# Send the size of the data first
size_bytes = struct.pack("!I", len(data_bytes))
client.sendall(size_bytes)

# Send the data itself
client.sendall(data_bytes)

# Receive acknowledgment from the server
acknowledgment = client.recv(1024)
print(f"Server acknowledgment: {acknowledgment.decode('ascii')}")

# Close the connection
client.close()
