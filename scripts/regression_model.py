# regression_model.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import os

# Create output directory if it doesn't exist
os.makedirs("results/model_output", exist_ok=True)

# Load the cleaned dataset
df = pd.read_csv("data/cleaned_movies_data.csv")

# Features (inputs) and target (output)
X = df[['year']]
y = df['Worldwide']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Save results
with open("results/model_output/model_performance.txt", 'w') as f:
    f.write(f"Mean Squared Error: {mse}\n")
    f.write(f"R2 Score: {r2}\n")
print("Model performance saved in results/model_output/")