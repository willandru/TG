import struct
import time

while True:
    # Open the binary file in read mode
    with open('mybinary.bin', 'rb') as file:
        while True:
            # Read 8 bytes (double-precision) from the file
            data = file.read(8)
            
            # Check if the end of the file is reached
            if not data:
                break
            
            # Unpack the bytes to a double-precision floating-point number
            signalX = struct.unpack('d', data)[0]
            
            # Print the double-precision floating-point number
            print(signalX)
            
            # Pause to control the data streaming rate
            time.sleep(0.1)
