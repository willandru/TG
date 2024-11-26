import pandas as pd
import matplotlib.pyplot as plt

# List of files to process
files = ["diameters_U1.csv", "diameters_U2.csv", "diameters_U3.csv", "diameters_U4.csv"]

for file in files:
    # Read the current file
    df = pd.read_csv(file)
    
    # Use the row index as the X-axis values
    x_values = range(len(df))  # Generate a range from 0 to the number of rows
    
    # Plot a horizontal line for the Moda_Diameters
    plt.figure(figsize=(10, 5))
    plt.hlines(y=df['Moda_Diameters'].iloc[0], xmin=min(x_values), xmax=max(x_values), colors='blue', label='Moda')

    # Configure plot
    plt.title(f"Moda vs. Row Index - {file}")
    plt.xlabel("Row Index")
    plt.ylabel("Moda (Diameter)")
    plt.grid(True)
    plt.legend()
    
    # Save the plot
    output_file = file.replace('.csv', '_horizontal_line_plot_by_row.png')
    plt.savefig(output_file)
    plt.close()
    print(f"Horizontal line plot generated: {output_file}")

print("All plots have been generated.")
