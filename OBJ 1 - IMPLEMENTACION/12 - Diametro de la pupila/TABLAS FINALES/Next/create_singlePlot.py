import pandas as pd
import matplotlib.pyplot as plt

# List of files to process
files = ["diameters_U1.csv", "diameters_U2.csv", "diameters_U3.csv", "diameters_U4.csv"]

# Create the figure and subplots
fig, axs = plt.subplots(2, 2, figsize=(15, 10))  # 2x2 grid
axs = axs.flatten()  # Flatten the array for easier iteration
fig.suptitle("Moda vs. Row Index for All Files", fontsize=16)

for i, file in enumerate(files):
    # Read the current file
    df = pd.read_csv(file)
    
    # Use the row index as the X-axis values
    x_values = range(len(df))  # Generate a range from 0 to the number of rows
    
    # Plot a horizontal line for the Moda_Diameters
    axs[i].hlines(y=df['Moda_Diameters'].iloc[0], xmin=min(x_values), xmax=max(x_values), colors='blue', label='Moda')
    
    # Configure the subplot
    axs[i].set_title(f"{file}")
    axs[i].set_xlabel("Row Index")
    axs[i].set_ylabel("Moda (Diameter)")
    axs[i].grid(True)
    axs[i].legend()

# Adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Save the combined figure
plt.savefig("combined_2x2_horizontal_line_plots.png")
plt.show()

print("Combined figure with 4 plots generated and saved as 'combined_2x2_horizontal_line_plots.png'.")
