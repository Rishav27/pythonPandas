import pandas as pd

# Load the JSON data
df = pd.read_csv("data/data.csv")

# Display basic info
print(f"Dataset shape: {df.shape}")
print(f"Columns: {list(df.columns)}")
print("\nFirst 5 rows:")
print(df.head())
