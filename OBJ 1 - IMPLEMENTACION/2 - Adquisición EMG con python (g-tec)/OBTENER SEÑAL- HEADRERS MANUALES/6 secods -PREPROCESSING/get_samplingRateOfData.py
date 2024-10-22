# File path to your EMG data
file_path = 'emg_6_abrir.csv'

# Read the file
with open(file_path, 'r') as f:
    lines = f.readlines()

# Check the number of values in the first few lines
for i in range(5):  # You can change the range to check more lines if needed
    values = lines[i].split(',')
    print(f"Line {i+1} has {len(values)} values.")
