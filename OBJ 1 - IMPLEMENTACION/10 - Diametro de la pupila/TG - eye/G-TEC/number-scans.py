import pygds

# Instantiate a GDS object
d = pygds.GDS()

# Calculate the number of scans for each configuration
d.NumberOfScans_calc()

# Print the number of scans for each configuration
for i, config in enumerate(d.Configs):
    print(f"Configuration {i+1}: Sampling Rate = {config.SamplingRate}, Number of Scans = {config.NumberOfScans}")

# Close the GDS object
d.Close()
