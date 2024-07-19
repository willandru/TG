import pygds

import numpy as np
import matplotlib.pyplot as plt
from pygds import Scope
import time

# Create an instance of the GDS class
d = pygds.GDS()

f = 10
# Create an instance of Scope with a period of 1/f
scope = Scope(1/f)
# Specify the number of scans you want to obtain from the device
scanCount = 500

# Get data from the device
data = d.GetData(scanCount)
canal = data[:, 0]
print(data)
print(canal)
print(canal.shape)
canal = canal.reshape(-1, 1)

while True:
    data = d.GetData(scanCount)
    canal = data[:, 0]
    canal = canal.reshape(-1, 1)
    scope(canal)
    #time.sleep(0.1)

# Close the connection to the device
d.Close()