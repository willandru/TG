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


BLOCK_SIZE = 25 # 1200/48

# Activate a specific channel
for i, channel in enumerate(d.Channels):
    if i == 0:
        channel.Acquire = 1
        channel.BandpassFilterIndex = 123
        channel.NotchFilterIndex = 9
    else:
        channel.Acquire = 0

# Set the configuration on the device
d.SetConfiguration()

###

record_duration = 10  # Duration in seconds for the acquisition
start_time = time.time()

# Function to handle each block of acquired data
def handle_samples(samples):
    print("Data block received:")
    print(samples)
    
    # Continue acquisition until record_duration is reached
    return time.time() - start_time < record_duration

# Loop to acquire data blocks continuously for the specified duration
try:
    while time.time() - start_time < record_duration:
        d.GetData(BLOCK_SIZE, more=handle_samples)
except KeyboardInterrupt:
    print("Acquisition interrupted by user.")

# Close the device connection
d.Close()
del d

print("Data acquisition complete.")