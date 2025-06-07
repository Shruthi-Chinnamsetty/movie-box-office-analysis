# Movie Box Office Analysis

This project analyses box office earnings of movies from 2010 to 2023 to explore trends over time. The analysis focuses on predicting and visualizing `Worldwide` earnings using `year` as a feature. It demonstrates core data analysis skills including data cleaning, visualisation, and regression modeling using Python.

## Dataset
The dataset used is sourced from [Kaggle: Movies Box Office Collection Data 2000-2024](https://www.kaggle.com/datasets/parthdande/movies-box-office-collection-data-2000-2024). It includes columns like `Rank`, `Release Group`, `Worldwide` earnings, `Domestic` earnings, `Foreign` earnings, and `year`.


## Installation
1. **Clone or Download:** If using Git, clone this repository. Otherwise, download the project files.

2. **Set Up Virtual Environment** (Recommended):

   ```bash
   python -m venv movie_analysis_env
   
3. ``` bash
   movie_analysis_env\Scripts\activate  # On Windows
   ```
   ```bash
   source movie_analysis_env/bin/activate  # On macOS/Linux
4. **Install Dependencies:**
    The requirements.txt includes libraries like pandas, numpy, matplotlib, seaborn, and scikit-learn.

    ```bash
    pip install -r requirements.txt
   
5. **Place Dataset:** Download the dataset from the Kaggle link above and place the CSV file as data/movies_box_office_collection_data.csv.

## Usage
Run the scripts in the following order from the project root directory:

1. **Data Cleaning:**
   - Cleans the dataset by handling missing values and formatting numbers.
   - Outputs data/cleaned_movies_data.csv.

    ```bash
    python scripts\data_cleaning.py

2. **Exploratory Analysis:**
   - Generates visualizations of Worldwide earnings over year.
   - Outputs plots to results/visualisations/.

    ```bash
    python scripts\exploratory_analysis.py
    
3. **Regression Model:**
   - Builds a linear regression model to predict Worldwide earnings using year.
   - Outputs performance metrics to results/model_output/model_performance.txt.

    ```bash
    python scripts\regression_model.py
   
## Outputs

- Cleaned Data: data/cleaned_movies_data.csv
- Visualisations: Scatterplot and boxplot of earnings over years in results/visualizations/
- Model Results: Mean Squared Error and R² Score in results/model_output/model_performance.txt

## Project Structure

```text
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
├── .gitignore                 # Git ignore file
└── README.md                  # Project documentation
```


## Requirements

- Python 3.10 or 3.11 (3.13 may have compatibility issues)
- Libraries listed in requirements.txt
