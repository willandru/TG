# William Andrés Gómez Roa
# @willandru
# 07/10/2024

import pygds
import time
import numpy as np

# Define the paths to the headers
gNEEDaccessHeaders = [
    r"C:/Users/willa/OneDrive/Documents/gtec/gNEEDaccessClientAPI/C/GDSClientAPI.h",
    r"C:/Users/willa/OneDrive/Documents/gtec/gNEEDaccessClientAPI/C/GDSClientAPI_gHIamp.h",
    r"C:/Users/willa/OneDrive/Documents/gtec/gNEEDaccessClientAPI/C/GDSClientAPI_gNautilus.h",
    r"C:/Users/willa/OneDrive/Documents/gtec/gNEEDaccessClientAPI/C/GDSClientAPI_gUSBamp.h"
]

# Initialize pygds with headers
result = pygds.Initialize(gds_headers=gNEEDaccessHeaders)
print(result)

d = pygds.GDS()

# Set sampling rate and block size for 40 ms window
f_s_2 = sorted(d.GetSupportedSamplingRates()[0].items())[6]
d.SamplingRate, d.NumberOfScans = f_s_2
BLOCK_SIZE = d.SamplingRate // 48  # 40 ms window

# Activate only the first channel and configure filters
for i, channel in enumerate(d.Channels):
    if i == 0:
        channel.Acquire = 1
        channel.BandpassFilterIndex = 123
        channel.NotchFilterIndex = 9
    else:
        channel.Acquire = 0

# Set the configuration on the device
d.SetConfiguration()

# Define parameters
record_duration = 5         # seconds for each recording period
pause_duration = 5          # seconds to pause between recordings
total_duration = 60         # total recording duration in seconds
num_cycles = total_duration // (record_duration + pause_duration)

# Start data acquisition
for cycle in range(num_cycles):
    # Define the output file for this cycle
    output_file = f"PRUEBA_ABRIR_{cycle+1}_5S.csv"
    
    print(f"Starting recording for {output_file}")

    # Open file to write data for this cycle
    with open(output_file, 'w') as f:
        cycle_start_time = time.time()
        
        # Function to handle data acquisition and save to file
        def save_samples(s):
            # Flatten and save the data as a single row in the file
            flattened_data = ','.join(map(str, s.flatten()))
            f.write(f"{flattened_data}\n")
            return time.time() - cycle_start_time < record_duration
        
        # Record data for 5 seconds
        while time.time() - cycle_start_time < record_duration:
            data = d.GetData(BLOCK_SIZE, more=save_samples)
            if time.time() - cycle_start_time >= record_duration:
                break

    print(f"Recording for {output_file} complete. Pausing for {pause_duration} seconds.")
    time.sleep(pause_duration)  # Pause for 5 seconds

# Close the connection with the g-tec device
d.Close()
del d

print("Data acquisition complete.")
