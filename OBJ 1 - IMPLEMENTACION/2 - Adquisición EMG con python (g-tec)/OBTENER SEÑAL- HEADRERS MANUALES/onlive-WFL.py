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
BLOCK_SIZE = d.SamplingRate//48
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

# Initialize plot for live waveform length
fig, ax = plt.subplots()
x_data, y_data = [], []
line_plot, = ax.plot([], [], lw=2)

ax.set_ylim(0, 1)  # Initial y-axis limit, will adjust dynamically
ax.set_xlim(0, 50)  # Show 50 samples in the x-axis at a time
ax.set_title("Live Waveform Length Over Time")
ax.set_xlabel("Time (40 ms intervals)")
ax.set_ylabel("Waveform Length")

# Function to calculate waveform length and update the plot
def update_waveform_length(data):
    # Calculate waveform length (WL)
    wl_result = np.sum(np.abs(np.diff(data.flatten())))
    
    # Update data lists
    y_data.append(wl_result)
    x_data.append(len(x_data))

    # Adjust plot limits if needed
    ax.set_ylim(0, max(y_data[-50:]) * 1.1)  # Fit y-axis to recent data
    if len(x_data) > 50:
        ax.set_xlim(len(x_data) - 50, len(x_data))  # Slide x-axis

    # Update line plot data
    line_plot.set_data(x_data, y_data)

# Signal acquisition loop with live waveform length plot
def acquire_and_plot():
    data = d.GetData(BLOCK_SIZE)
    update_waveform_length(data)

# Set up the live animation update
ani = FuncAnimation(fig, lambda frame: acquire_and_plot(), interval=40)
plt.show()

# Close the connection with the g-tec device after acquisition
d.Close()
del d

print('Data acquisition complete.')
