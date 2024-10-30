import os
import numpy as np

# File and output directory
file_path = 'emg_6_abrir.csv'
output_dir = '10ms_CHUNKS_ABRIR'
os.makedirs(output_dir, exist_ok=True)

# Chunking parameters
sampling_rate = 1200  # 1200 Hz
chunk_size = int(sampling_rate * 0.01)  # 25ms

# Read the file
with open(file_path, 'r') as f:
    lines = f.readlines()

# Skip the first line (header)
data_lines = lines[1:]

# Initialize counter for chunk filenames
chunk_counter = 0

# Process each second of data
for line in data_lines:  # Use data_lines to skip the header
    values = [float(val) for val in line.split(',') if val.strip()]  # Skip empty strings
    
    # Split into 10ms chunks
    for i in range(0, len(values), chunk_size):
        chunk = values[i:i + chunk_size]
        
        # Save if chunk has the correct size
        if len(chunk) == chunk_size:
            chunk_filename = os.path.join(output_dir, f'chunk_{chunk_counter}.csv')
            np.savetxt(chunk_filename, chunk, delimiter=',')
            chunk_counter += 1

print(f"Total chunks created: {chunk_counter}")
