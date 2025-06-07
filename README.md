# Movie Box Office Analysis

This project analyses box office earnings of movies from 2010 to 2023 to explore trends over time. Due to the unavailability of `Budget` and `Genre` in the dataset, the analysis focuses on predicting and visualizing `Worldwide` earnings using `year` as a feature. It demonstrates core data analysis skills including data cleaning, visualization, and regression modeling using Python.

## Dataset
The dataset used is sourced from [Kaggle: Movies Box Office Collection Data 2000-2024](https://www.kaggle.com/datasets/parthdande/movies-box-office-collection-data-2000-2024). It includes columns like `Rank`, `Release Group`, `Worldwide` earnings, `Domestic` earnings, `Foreign` earnings, and `year`.

**Note**: The original intent was to predict earnings based on `Budget` and `Genre`, but these columns are absent, so the analysis was adapted to use `year`.

## Installation
1. **Clone or Download**: If using Git, clone this repository. Otherwise, download the project files.
2. **Set Up Virtual Environment** (Recommended):
   ```bash
   python -m venv movie_analysis_env
   movie_analysis_env\Scripts\activate  # On Windows
   # or
   source movie_analysis_env/bin/activate  # On macOS/Linux
3. **Install Dependencies** 
    ```bash
    pip install -r requirements.txt
    # The requirements.txt includes libraries like pandas, numpy, matplotlib, seaborn, and scikit-learn.
4. **Place Dataset:** Download the dataset from the Kaggle link above and place the CSV file as data/movies_box_office_collection_data.csv.

## Usage
Run the scripts in the following order from the project root directory:

1. **Data Cleaning:**
    ```bash
    python scripts\data_cleaning.py

    Cleans the dataset by handling missing values and formatting numbers.
    Outputs data/cleaned_movies_data.csv.
2. **Exploratory Analysis:**
    ```bash
    python scripts\exploratory_analysis.py

    Generates visualizations of Worldwide earnings over year.
    Outputs plots to results/visualizations/.
3. **Regression Model:**
    ```bash
    python scripts\regression_model.py
    
    Builds a linear regression model to predict Worldwide earnings using year.
    Outputs performance metrics to results/model_output/model_performance.txt.

## Outputs

Cleaned Data: data/cleaned_movies_data.csv
Visualizations: Scatterplot and boxplot of earnings over years in results/visualizations/
Model Results: Mean Squared Error and R² Score in results/model_output/model_performance.txt

## Project Structure

movie-box-office-analysis/
│
├── data/                      # Dataset files (ignored by Git)
├── scripts/                   # Python scripts for analysis
│   ├── data_cleaning.py
│   ├── exploratory_analysis.py
│   └── regression_model.py
├── results/                   # Output files (ignored by Git)
│   ├── visualizations/
│   └── model_output/
├── movie_analysis_env/        # Virtual environment (ignored by Git)
├── requirements.txt           # List of required libraries
├── .gitignore                # Git ignore file
└── README.md                 # Project documentation

## Requirements

Python 3.10 or 3.11 (3.13 may have compatibility issues)
Libraries listed in requirements.txt
