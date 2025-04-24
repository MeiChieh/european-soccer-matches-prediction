# ⚽ European Soccer Matches Prediction

## 📊 Overview

This project analyzes European soccer match data from 2008 to 2016 to predict game outcomes using machine learning techniques. The goal is to create a logistic regression model that predicts match results for the 2015/2016 season based on data from previous seasons. The analysis is structured in three main phases: data cleaning and feature extraction, exploratory data analysis (EDA) with feature selection, and modeling.

## 📚 Dataset

The project uses the [European Soccer Matches](https://www.kaggle.com/datasets/prajitdatta/ultimate-25k-matches-football-database-european) dataset from Kaggle, stored in a SQLite database (`database.sqlite`). The data includes:

- Match results from multiple European leagues
- Team statistics and attributes
- Player performance metrics
- Formation data
- Historical game records
- Bookmaker odds

## ⭐ Key Findings

### 1. 🎯 Feature Selection

The analysis identified three key predictors:

- `player_score_mean_diff`: Difference in player performance metrics
- `past_game_result_diff`: Historical game results difference
- `formation_win_rate_diff`: Formation effectiveness difference

### 2. 🏆 Model Performance

- Logistic Regression implementation with balanced and imbalanced approaches
- League-specific vs. general model comparison
- Home advantage effects consideration
- Historical performance metrics integration
- Hyperparameter tuning using RandomSearch
- Cross-validation implementation

### 3. 📈 Data Analysis Insights

- Home advantage detection and analysis
- Formation combination impact on match outcomes
- Player performance correlation with results
- Team attributes influence on game results
- Past performance correlation with future results

## 📁 Project Structure

```
├── 1_data_cleaning_and_feature_extraction.ipynb
├── 2_eda_and_feature_selection.ipynb
├── 3_modeling.ipynb
├── helper/                    # Helper functions and utilities
│   ├── helper_function.py
│   └── __init__.py
├── data/                      # Data directory
│   └── database.sqlite
├── Pipfile                    # Pipenv dependencies
├── requirements.txt           # Python package requirements
└── README.md                  # Project documentation
```

## 🛠️ Technologies Used

- Python
- Key Libraries:
  - pandas
  - numpy
  - seaborn
  - matplotlib
  - scikit-learn
  - duckdb
  - scipy
- Tableau for visualization

## 🚀 Setup and Installation

1. Clone the repository
2. Download the soccer SQLite data and place it in `/data/database.sqlite`
3. Install dependencies using either:

   ```bash
   # Using pip
   pip install -r requirements.txt

   # OR using Pipenv
   pipenv install
   ```

## 💡 Project Structure

The analysis is organized in three main notebooks:

1. `1_data_cleaning_and_feature_extraction.ipynb`

   - Detect null values and duplicates
   - Combine relevant tables
   - Convert player coordinate columns to formations
   - Extract relevant player scores and team attributes

2. `2_eda_and_feature_selection.ipynb`

   - Feature distribution analysis
   - Home advantage detection and hypothesis testing
   - Formation combination analysis
   - Player score comparison
   - Team attributes correlation
   - Past performance analysis

3. `3_modeling.ipynb`
   - Train-test split
   - Missing value imputation and standardization
   - Multiple logistic regression models
   - Hyperparameter tuning
   - Cross-validation
   - Model performance comparison
   - Bookmaker odds comparison

## 🔄 Future Improvements

1. Implement additional machine learning models for comparison
2. Add more sophisticated feature engineering
3. Include real-time prediction capabilities
4. Develop a web interface for predictions
5. Expand to include more leagues and seasons
6. Enhance visualization capabilities
7. Implement automated model retraining

## 📦 Dependencies

Key dependencies include:

- numpy
- pandas
- seaborn
- matplotlib
- scikit-learn
- duckdb
- scipy

For a complete list of dependencies, see `requirements.txt` or `Pipfile`.

## 📝 Notes

- The analysis specifically focuses on predicting the 2015/2016 season
- Training data is limited to seasons 2008/2009 through 2014/2015 to prevent data leakage
- Home advantage effects are accounted for in the feature engineering process
- Model performance is compared against bookmaker predictions
- Additional visualizations available in [Tableau Dashboard](https://public.tableau.com/app/profile/mei.chieh.chien/viz/soccerprediction/Dashboard1?publish=yes)
