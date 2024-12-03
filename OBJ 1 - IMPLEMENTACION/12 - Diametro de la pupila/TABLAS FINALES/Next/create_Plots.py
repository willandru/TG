import pandas as pd
import matplotlib.pyplot as plt

# List of files to process
files = ["diameters_U1.csv", "diameters_U2.csv", "diameters_U3.csv", "diameters_U4.csv"]

# Create a 2x2 subplot figure
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Flatten the axes array for easier indexing
axes = axes.flatten()

# Loop through files and plot in each subplot
for i, file in enumerate(files):
    # Read the current file
    df = pd.read_csv(file)
    
    # Use the row index as the X-axis values
    x_values = range(len(df))  # Generate a range from 0 to the number of rows
    
    # Scatter plot for the current file
    axes[i].scatter(x_values, df['Moda_Diameters'], alpha=0.7)
    axes[i].set_title(f"Diámetros U{i+1}")  # Title with file-specific name
    axes[i].set_xlabel("Tiempo (minutos)")
    axes[i].set_ylabel("Moda (Diámetro)")
    axes[i].grid(True)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Save the complete figure
output_file = "matrix_scatter_plot_by_row.png"
plt.savefig(output_file)
plt.close()
print(f"Matrix scatter plot generated: {output_file}")
