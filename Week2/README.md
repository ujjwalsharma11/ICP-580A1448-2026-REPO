# Project 2 – Regression for Price Prediction

## Objective
Build a regression model to estimate house values and evaluate its performance.

## Models
- Linear Regression (baseline)
- Random Forest Regression

## Techniques
- Data inspection and preprocessing
- Feature engineering
- Train/test split
- 5-fold cross-validation
- Hyperparameter tuning with GridSearchCV
- MAE, RMSE and R² evaluation
- Residual/error analysis
- Random Forest feature importance
- Model serialization with Joblib

## Dataset
California Housing dataset provided through `sklearn.datasets.fetch_california_housing`.

## How to Run

```bash
pip install -r requirements.txt
jupyter notebook project2_house_price_prediction.ipynb
```

Run all cells from top to bottom. The dataset is fetched by scikit-learn when the notebook runs.

## Output
The notebook produces:
- Model comparison
- Cross-validation results
- Best hyperparameters
- Final MAE/RMSE/R²
- Actual-vs-predicted plot
- Residual distribution
- Feature importance
- `house_price_model.joblib`
  
The trained model is saved as `house_price_model.joblib` for future predictions and experimentation.
