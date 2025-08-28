import os
import pandas as pd

# Set the folder containing the files
folder_path = input("Enter your folder path: ")   # Replace with your folder path

# List all CSV files in the folder
all_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# List to store DataFrames
dataframes = []

# Read each file and append to the list
for file in all_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)
    dataframes.append(df)

# Merge all DataFrames into one
merged_df = pd.concat(dataframes, ignore_index=True)

# Save the merged file
merged_df.to_csv("merged_file.csv", index=False)

print("✅ All CSV files have been merged into merged_file.csv")
