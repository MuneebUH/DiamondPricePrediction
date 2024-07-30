# Diamond Price Prediction

## Project Overview

This project aims to predict the price of diamonds based on various features such as carat, cut, color, clarity, depth, table, and dimensions. The primary goal is to build a predictive model that can accurately estimate diamond prices, utilizing machine learning techniques and feature engineering.

## Dataset

- **Features**: 
  - Numerical: `carat`, `depth`, `table`, `x`, `y`, `z`
  - Categorical: `cut`, `color`, `clarity`
- **Target Variable**: `price`

## Preprocessing
Ordinal encoding was used for categorical features

## Model Selection

### Evaluated Models

| Model                        | Mean Absolute Error | R-squared |
|------------------------------|---------------------|-----------|
| Linear Regression            | 805.27              | 0.90      |
| Decision Tree Regressor      | 354.55              | 0.96      |
| Random Forest Regressor      | 266.02              | 0.98      |
| XGBoost Regressor            | 276.58              | 0.98      |

### Selected Model

- **Model**:  XGBoost Regressor
- **Reason**: Achieved the R-squared value (0.98) and competitive Mean Absolute Error (276.58), with lightweight model size as compared to Random Forest


## Training and Evaluation

- **Training Data**: 80% of the dataset
- **Test Data**: 20% of the dataset

