import pygds

# Initialize the device
d = pygds.GDS()

# Access channel information
for channel in d.Channels:
    print("Channel:", channel)

# Close the device
d.Close()
del d
