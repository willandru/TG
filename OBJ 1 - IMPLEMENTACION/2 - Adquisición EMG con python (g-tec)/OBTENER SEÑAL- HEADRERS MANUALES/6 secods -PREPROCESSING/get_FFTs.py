import os
import numpy as np

# List of folders containing chunks
folders = [
    "10ms_CHUNKS_ABRIR",
    "10ms_CHUNKS_FRUNSIR",
    "10ms_CHUNKS_NADA",
    "25ms_CHUNKS_ABRIR",
    "25ms_CHUNKS_FRUNSIR",
    "25ms_CHUNKS_NADA"
]

# Number of FFT components to extract
fft_components = 8

# Function to perform FFT and extract first 8 components
def process_chunks(folder_path):
    output_data = []
    
    # List all files (chunks) in the folder
    chunk_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    
    for chunk_file in chunk_files:
        # Load the chunk data
        chunk_path = os.path.join(folder_path, chunk_file)
        chunk_data = np.loadtxt(chunk_path, delimiter=',')
        
        # Perform FFT
        fft_result = np.fft.fft(chunk_data)
        
        # Extract the first 8 FFT components (real part)
        fft_components_data = np.real(fft_result[:fft_components])
        
        # Store the FFT components
        output_data.append(fft_components_data)
    
    # Save the FFT components to a new CSV file named after the folder
    output_file = os.path.join(folder_path, f"{os.path.basename(folder_path)}_fft.csv")
    np.savetxt(output_file, output_data, delimiter=',')
    print(f"FFT results saved to {output_file}")

# Process all folders
for folder in folders:
    process_chunks(folder)
