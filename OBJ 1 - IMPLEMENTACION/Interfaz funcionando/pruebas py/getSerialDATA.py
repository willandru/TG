import serial

# Open serial port
ser = serial.Serial('COM6', 115200)  # Adjust baud rate as per your Arduino code

try:
    while True:
        # Read data from serial port
        data = ser.readline().decode().strip()
        
        # Check if the received data contains skin sensor measurements
        if "Conductance" in data:
            # Extract the skin conductance value
            conductance = data.split(":")[-1].strip()
            print("Skin Conductance:", conductance)
        elif "Resistance" in data:
            # Extract the skin resistance value
            resistance = data.split(":")[-1].strip()
            print("Skin Resistance:", resistance)
        elif "Conductance Voltage" in data:
            # Extract the skin conductance voltage value
            conductance_voltage = data.split(":")[-1].strip()
            print("Skin Conductance Voltage:", conductance_voltage)
        
except KeyboardInterrupt:
    # Close serial port when program is interrupted
    ser.close()
    print("Serial port closed.")
