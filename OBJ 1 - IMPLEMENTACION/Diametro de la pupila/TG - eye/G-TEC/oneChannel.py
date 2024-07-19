
import pygds
import time

# Initialize the device
d = pygds.GDS()

# Activate only channel 1 and deactivate the others
for i, channel in enumerate(d.Channels):
    #channel.Acquire=1
    if i == 0:
        channel.Acquire = 1
    else:
        channel.Acquire = 0

# Set the configuration
print( 'Impadancias: ' ,d.GetImpedance())
print('Bandpass Filters: ', GetBandpassFilters())
print('Notch Filters: ', GetNotchFilters())
 
d.Close()
del d
