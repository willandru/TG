import numpy as np
import matplotlib.pyplot as plt
from pygds import Scope
import time

# Sampling frequency
f = 10

# Create an instance of Scope with a period of 1/f
scope = Scope(1/f)

# Create an example data set 't'
t = np.linspace(0, 100, 100) / f

# Send data to Scope and visualize in real time
for i in range(2, 6):
    # Generate example data using sine waves with different frequencies
    data = np.array([np.sin(t + i/j) for j in range(2, 6)])
    # Send data to Scope
    print(data.shape)
    scope(data)
    # Wait for a longer period of time before sending the next set of data
    time.sleep(1)  # Adjust sleep time here to make it last longer

# Delete the Scope instance
del scope
