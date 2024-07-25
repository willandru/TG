import serial.tools.list_ports

def print_com_devices():
    com_ports = serial.tools.list_ports.comports()
    if com_ports:
        print("Available COM devices:")
        for port in com_ports:
            print(port.device)
    else:
        print("No COM devices found.")

# Print the current COM devices
print_com_devices()
