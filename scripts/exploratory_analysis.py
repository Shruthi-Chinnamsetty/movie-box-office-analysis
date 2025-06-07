# exploratory_analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create output directory if it doesn't exist
os.makedirs("results/visualisations", exist_ok=True)

# Load the cleaned dataset
df = pd.read_csv("data/cleaned_movies_data.csv")

# Basic statistics
print("Basic Statistics:")
print(df.describe())

# Plot 1: Worldwide Earnings over Year
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='year', y='Worldwide', alpha=0.6)
plt.title('Worldwide Earnings Over Years')
plt.xlabel('Year')
plt.ylabel('Worldwide Earnings ($)')
plt.savefig("results/visualisations/worldwide_over_year.png")
plt.close()

# Plot 2: Boxplot of Worldwide Earnings by Year (limited to top years if too many)
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='year', y='Worldwide')
plt.title('Worldwide Earnings by Year')
plt.xticks(rotation=45)
plt.savefig("results/visualisations/worldwide_by_year_boxplot.png")
plt.close()

print("visualisations saved in results/visualisations/")