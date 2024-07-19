import pygds
import time

# Initialize the device
d = pygds.GDS()

# Activate only channel 1 and deactivate the others
for i, channel in enumerate(d.Channels):
    #channel.Acquire = 1
    if i == 0 or i==1:
        channel.Acquire = 1
    else:
        channel.Acquire = 0

# Set the configuration
d.SetConfiguration()
#print(d.GetScaling())

scope = pygds.Scope(1/d.SamplingRate) 
d.GetData(d.SamplingRate,scope)


