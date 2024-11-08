import pygds
import socket
import struct
import time
import numpy as np

# Server configuration
HOST = 'localhost'
PORT = 6340
BLOCK_SIZE = 25  # Block size for 20 ms intervals at 1200 Hz

# Initialize pygds and device
gNEEDaccessHeaders = [
    r"C:/Users/willa/OneDrive/Documents/gtec/gNEEDaccessClientAPI/C/GDSClientAPI.h",
    r"C:/Users/willa/OneDrive/Documents/gtec/gNEEDaccessClientAPI/C/GDSClientAPI_gHIamp.h",
    r"C:/Users/willa/OneDrive/Documents/gtec/gNEEDaccessClientAPI/C/GDSClientAPI_gUSBamp.h"
]
pygds.Initialize(gds_headers=gNEEDaccessHeaders)
device = pygds.GDS()

# Configure device with a sampling rate and enable the first channel
device.SamplingRate, device.NumberOfScans = sorted(device.GetSupportedSamplingRates()[0].items())[6]

# Activate a specific channel
for i, channel in enumerate(device.Channels):
    if i == 0:
        channel.Acquire = 1
        channel.BandpassFilterIndex = 123
        channel.NotchFilterIndex = 9
    else:
        channel.Acquire = 0
device.SetConfiguration()

# Start TCP server
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"Server listening on {HOST}:{PORT}...")
        conn, addr = server_socket.accept()
        print(f"Connection established with {addr}")

        # Function to handle each block of acquired data
        def handle_samples(samples):
            # Flatten samples and pack as double precision
            data = np.array(samples).flatten()
            data_bytes = struct.pack(f"!{len(data)}d", *data)
            # Send the length of the data in bytes, followed by the actual data
            data_length = len(data_bytes)
            conn.sendall(struct.pack('!I', data_length))
            conn.sendall(data_bytes)
            print("Sent data block:", data)
            # Return True to continue acquisition indefinitely
            return True
        # Acquire and send data blocks indefinitely
        try:
            while True:
                device.GetData(BLOCK_SIZE, more=handle_samples)
        except Exception as e:
            print(f"Transmission error: {e}")
        finally:
            print("Closing connection...")
            conn.close()

    device.Close()
    print("Data acquisition complete.")

if __name__ == "__main__":
    start_server()
