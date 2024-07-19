import pygds

# Instantiate a GDS object
d = pygds.GDS()

# Get the supported sampling rates
supported_sampling_rates = d.GetSupportedSamplingRates()

# Print the supported sampling rates
print("Supported Sampling Rates: ", supported_sampling_rates)
for device_sampling_rates in supported_sampling_rates:
    for sampling_rate, number_of_scans in device_sampling_rates.items():
        print(f"Sampling Rate: {sampling_rate}, Number of Scans: {number_of_scans}")

# Close the GDS object
d.Close()
