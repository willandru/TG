import pygds as g

# Initialize the g.tec EEG system
d = g.GDS()

# Get the supported sampling rates and select the minimum one
minf_s = sorted(d.GetSupportedSamplingRates()[0].items())[0] 

d.SamplingRate, d.NumberOfScans = minf_s 
print(sorted(d.GetSupportedSamplingRates()[0].items())[2])
# Configure the g.tec EEG system to acquire data from all channels
for ch in d.Channels: 
    ch.Acquire = True 
d.SetConfiguration()

# Acquire data from all channels
data_all_channels = d.GetData(d.SamplingRate)

# Close the connection to the g.tec EEG system
d.Close()

# Specify the channel you want to extract data from (e.g., channel 2)
desired_channel_index = 1  # Assuming channel indexing starts from 0
desired_channel_data = data_all_channels[:, desired_channel_index]

# Print or process the data from the desired channel as needed
scope = g.Scope(1/d.SamplingRate)
d.GetData(d.SamplingRate,scope)
