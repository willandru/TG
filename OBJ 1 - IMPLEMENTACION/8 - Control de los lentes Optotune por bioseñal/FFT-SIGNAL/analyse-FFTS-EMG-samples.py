import os
import pandas as pd
import matplotlib.pyplot as plt

# Set the directory where the files are located
directory = './'  # Replace with the actual path

# Define the file paths and assign a color for each file
file_paths = {
    '10ms_CHUNKS_ABRIR_fft.csv': 'blue',
    '10ms_CHUNKS_FRUNSIR_fft.csv': 'green',
    '10ms_CHUNKS_NADA_fft.csv': 'red',
    '25ms_CHUNKS_ABRIR_fft.csv': 'purple',
    '25ms_CHUNKS_FRUNSIR_fft.csv': 'orange',
    '25ms_CHUNKS_NADA_fft.csv': 'cyan'
}

# Dictionary to store mean values for each file
mean_values = {}

# Load each file, calculate mean of each column, and store in the dictionary
for file_name, color in file_paths.items():
    file_path = os.path.join(directory, file_name)
    try:
        df = pd.read_csv(file_path, header=None)
        mean_values[file_name] = df.mean(axis=0)
    except pd.errors.EmptyDataError:
        print(f"The file {file_name} is empty or could not be read properly.")
    except FileNotFoundError:
        print(f"The file {file_name} was not found. Please check the path.")

# Plot the mean values for each file
plt.figure(figsize=(12, 8))

for file_name, color in file_paths.items():
    if file_name in mean_values:
        plt.plot(mean_values[file_name], marker='o', color=color, label=file_name)

plt.title("Mean of Each Frequency Component (8 columns) for 25ms Files")
plt.xlabel("Frequency Component")
plt.ylabel("Mean FFT Magnitude")
plt.legend()
plt.show()
