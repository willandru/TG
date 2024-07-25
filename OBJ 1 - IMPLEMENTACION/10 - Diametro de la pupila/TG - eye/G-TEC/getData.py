import pygds

# Initialize the device
d = pygds.GDS()

# Activate only channel 1 and deactivate the others

f_s_2 = sorted(d.GetSupportedSamplingRates()[0].items())[6]

d.SamplingRate, d.NumberOfScans = f_s_2


for i, channel in enumerate(d.Channels):
    #channel.Acquire=1
    if i == 0:
        channel.Acquire = 1
        #print(channel)
    else:
        channel.Acquire = 0

# Set the configuration
#print( 'Impadancias: ' ,d.GetImpedance())
#print('Bandpass Filters: ', d.GetBandpassFilters())
#print('Notch Filters: ', d.GetNotchFilters())
#print('Scaling..', d.GetScaling())


current_scaling = d.GetScaling()
current_scaling[0].ScalingFactor = [100.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
d.SetScaling(current_scaling)


d.SetConfiguration()



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

# Close the device (make sure to do this when you're done)
d.Close()
del d
