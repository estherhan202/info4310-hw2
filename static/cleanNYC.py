import pandas as pd

# Load the CSV file
df = pd.read_csv("NYC311data.csv", dtype=str)

# Select relevant columns
columns_to_keep = ["Borough", "Complaint Type", "Descriptor", "Created Date", "Latitude", "Longitude", "Unique Key"]
df_cleaned = df[columns_to_keep]

# Drop rows with missing latitude or longitude
df_cleaned = df_cleaned.dropna(subset=["Latitude", "Longitude"])

# Filter out rows that are do not start with "Noise - " in the "Complaint Type" column
df_cleaned = df_cleaned[df_cleaned["Complaint Type"].str.startswith("Noise - ", na=False)]

# Remove "Others" in the Complaint Type column
df_cleaned = df_cleaned[~df_cleaned["Complaint Type"].str.contains("Others", na=False)]

# Save to a new CSV file
df_cleaned.to_csv("CleanedNYC311data.csv", index=False)

print("CleanedNYC311data.csv has been created successfully.")
