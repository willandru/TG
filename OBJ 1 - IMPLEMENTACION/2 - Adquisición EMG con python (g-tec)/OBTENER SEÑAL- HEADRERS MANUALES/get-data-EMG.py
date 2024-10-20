# William Andrés Gómez Roa
# @willandru
# 07/10/2024

'''
This script configures one or more channels, applies filters, increases scaling for each channel, and acquires data for 1 minute.
The acquired data is saved to a file.
'''

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

# Select 'Sampling Rate' and 'Number of Scans'
f_s_2 = sorted(d.GetSupportedSamplingRates()[0].items())[6]
d.SamplingRate, d.NumberOfScans = f_s_2

# Activate a specific channel
for i, channel in enumerate(d.Channels):
    if i == 0:
        channel.Acquire = 1
        channel.BandpassFilterIndex = 123
        channel.NotchFilterIndex = 9
    else:
        channel.Acquire = 0

# Increase the scaling of a specific channel
current_scaling = d.GetScaling()
current_scaling[0].ScalingFactor = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
d.SetScaling(current_scaling)

# Set the configuration on the device
d.SetConfiguration()

# Define file to save the data
output_file = 'emg_200_abrir_3.csv'

# Initialize variables for data acquisition
samples_received = 0
record_duration = 100  # seconds
start_time = time.time()

# Open the file to write data
with open(output_file, 'w') as f:
    f.write('SampleData\n')  # Write header for the CSV file

    # Function to handle data acquisition and saving to the file
    def save_samples(s):
        global samples_received
        samples_received += 1
        
        # Flatten and save the data as a single row in the file
        flattened_data = ','.join(map(str, s.flatten()))
        f.write(f"{flattened_data}\n")

        # Continue acquisition for 1 minute
        return time.time() - start_time < record_duration

    # Signal acquisition loop
    while time.time() - start_time < record_duration:
        data = d.GetData(d.SamplingRate, more=save_samples)
        if time.time() - start_time >= record_duration:
            break

# Close the connection with the g-tec device
d.Close()
del d

print(f'Data acquisition complete. Data saved to {output_file}')
