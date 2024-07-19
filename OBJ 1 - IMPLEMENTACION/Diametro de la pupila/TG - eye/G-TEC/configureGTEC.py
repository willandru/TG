import pygds
import numpy as np
# Initialize the device
d = pygds.GDS()

# Configurar la frecuencia de muestreo y el número de escaneos.
f_s_2 = sorted(d.GetSupportedSamplingRates()[0].items())[6] 
d.SamplingRate, d.NumberOfScans = f_s_2
print(f_s_2)

#Busca los filtros: ___0-60--500___ [Hz]
 # get all applicable filters
 
N = [x for x in d.GetNotchFilters()[0] if x['SamplingRate']
         == d.SamplingRate]
BP = [x for x in d.GetBandpassFilters()[0] if x['SamplingRate']
          == d.SamplingRate]
print('NOTHC ', N[1])
print('BAND PASS', BP[9])

for i, channel in enumerate(d.Channels):
    #channel.Acquire=1
    if i == 0 or i==1:
        channel.Acquire = 1
        channel.BandpassFilterIndex = 123
        channel.NotchFilterIndex = 9
    else:
        channel.Acquire = 0

current_scaling = d.GetScaling()
current_scaling[0].ScalingFactor = [1000.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
d.SetScaling(current_scaling)



d.SetConfiguration()

scope = pygds.Scope(1/d.SamplingRate) 
d.GetData(d.SamplingRate,scope)
'''

# Define a function to handle the samples and control data acquisition
samples_received = 0
max_samples = 5  # Number of samples to receive

def print_samples(s):
    global samples_received
    samples_received += 1
    print(s)
    return samples_received < max_samples  # Continue acquisition until max_samples is reached

# Continuous data acquisition loop

while True:
    # Call GetData to acquire data every second
    data = d.GetData(d.SamplingRate, more=print_samples)
    if samples_received >= max_samples:
        break

'''
# Close the device (make sure to do this when you're done)
d.Close()
del d
