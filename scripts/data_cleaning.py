# data_cleaning.py
import pandas as pd

# Load the dataset
data_path = "data/movies_box_office_collection_data.csv"
df = pd.read_csv(data_path)

# Display the first few rows to understand the data
print("Original Data Preview:")
print(df.head())

# Handle missing values (fill or drop based on column)
# Note: 'Budget' and 'Genre' are not in the dataset, so skip those for now
df = df.dropna(subset=['Worldwide'])  # Drop rows with missing worldwide collection

# Convert 'Worldwide' to numeric (remove commas or symbols if present)
df['Worldwide'] = df['Worldwide'].replace(r'[,\$]', '', regex=True).astype(float)

# Save the cleaned dataset
cleaned_path = "data/cleaned_movies_data.csv"
df.to_csv(cleaned_path, index=False)
print(f"Cleaned data saved to {cleaned_path}")