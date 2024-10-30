# William Andrés Gómez Roa
# @willandru
# 07/10/2024

import pygds
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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
BLOCK_SIZE = 1200  # 40 ms window

# Activate only the first channel and configure filters
for i, channel in enumerate(d.Channels):
    if i == 0:
        channel.Acquire = 1
        channel.BandpassFilterIndex = 123
        channel.NotchFilterIndex = 9
    else:
        channel.Acquire = 0

# Increase the scaling for the first channel
current_scaling = d.GetScaling()
current_scaling[0].ScalingFactor = [1.0] * 16
d.SetScaling(current_scaling)

# Set the configuration on the device
d.SetConfiguration()

# Initialize plot for live FFT of the first 3 components
fig, ax = plt.subplots()
frequencies = np.fft.fftfreq(BLOCK_SIZE, d=1/d.SamplingRate)[:3]  # Only the first 3 FFT components
fft_values = np.zeros(3)
bar_plot = ax.bar(frequencies, fft_values)

ax.set_ylim(0, 1)  # Initial y-axis limit, will adjust dynamically
ax.set_title("Live FFT (First 3 Components)")
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Amplitude")

# Function to calculate FFT and update the plot
def update_fft_plot(data):
    # Calculate FFT and update plot
    fft_result = np.abs(np.fft.fft(data.flatten()))[:3]  # Only first 3 components

    # Update the height of each bar
    for bar, y in zip(bar_plot, fft_result):
        bar.set_height(y)

    ax.set_ylim(0, max(fft_result) * 1.1)  # Adjust y-axis to fit data

# Signal acquisition loop with live FFT plot
def acquire_and_plot():
    data = d.GetData(BLOCK_SIZE)
    update_fft_plot(data)

# Set up the live animation update
ani = FuncAnimation(fig, lambda frame: acquire_and_plot(), interval=40)
plt.show()

# Close the connection with the g-tec device after acquisition
d.Close()
del d

print('Data acquisition complete.')
