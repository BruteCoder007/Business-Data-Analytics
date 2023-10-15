
import pandas as pd

# List of CSV file paths to combine
csv_files = ['TELIA1.HE.csv', 'TSCO.L.csv', 'TSLA.csv']

# Initialize an empty DataFrame to store the combined data
combined_data = pd.DataFrame()

# Loop through the CSV files and append their data to the combined_data DataFrame
for file in csv_files:
    data = pd.read_csv(file)
    combined_data = combined_data.append(data, ignore_index=True)

# Save the combined data to a new CSV file
combined_data.to_csv('combined.csv', index=False)

print("CSV files combined and saved as 'combined.csv'")
