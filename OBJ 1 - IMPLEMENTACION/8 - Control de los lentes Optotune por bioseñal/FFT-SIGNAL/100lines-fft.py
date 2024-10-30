import os
import pandas as pd
import matplotlib.pyplot as plt

# Set the directory where the files are located
directory = './'  # Replace with the actual path

# Define the file paths for all 6 files and assign colors
file_paths = {
    '10ms_CHUNKS_ABRIR_fft.csv': 'blue',
    '10ms_CHUNKS_FRUNSIR_fft.csv': 'green',
    '10ms_CHUNKS_NADA_fft.csv': 'red',
    '25ms_CHUNKS_ABRIR_fft.csv': 'purple',
    '25ms_CHUNKS_FRUNSIR_fft.csv': 'orange',
    '25ms_CHUNKS_NADA_fft.csv': 'cyan'
}

# Dictionary to store data for each file
data_frames = {}

# Load each file and store the first 100 instances
for file_name in file_paths.keys():
    file_path = os.path.join(directory, file_name)
    try:
        df = pd.read_csv(file_path, header=None).iloc[:100]  # Get first 100 instances
        data_frames[file_name] = df
    except pd.errors.EmptyDataError:
        print(f"The file {file_name} is empty or could not be read properly.")
    except FileNotFoundError:
        print(f"The file {file_name} was not found. Please check the path.")

# Plot the first 100 instances for each file
plt.figure(figsize=(15, 10))

for file_name, color in file_paths.items():
    if file_name in data_frames:
        for i in range(data_frames[file_name].shape[1]):  # Loop through each column (frequency component)
            plt.plot(data_frames[file_name].iloc[:, i], color=color, alpha=0.5, label=file_name if i == 0 else "")

plt.title("First 100 Instances of Frequency Components for Each File")
plt.xlabel("Instance")
plt.ylabel("FFT Magnitude")
plt.legend()
plt.show()
