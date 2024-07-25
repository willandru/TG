import socket
import struct
import random

# Define the array of doubles (size 50)
data_array = [random.random() for _ in range(50)]

# Convert array to bytes
data_bytes = struct.pack(f"{len(data_array)}d", *data_array)

# Connect to the LabVIEW client (replace 'localhost' and 6340 with your actual LabVIEW server address and port)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 6340)  # Adjust port and address as needed
client.connect(server_address)

# Send the size of the data first
size_bytes = struct.pack("!I", len(data_bytes))
client.sendall(size_bytes)

# Send the data itself
client.sendall(data_bytes)

# Close the connection
client.close()
