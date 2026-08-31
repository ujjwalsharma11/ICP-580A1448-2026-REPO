# Project 2 Final Report – Regression for Price Prediction

## 1. Problem Statement
The objective of this project is to predict house values using machine learning regression techniques.

## 2. Dataset
The California Housing dataset available through scikit-learn was used. The target variable is median house value.

## 3. Methodology
The data was inspected and preprocessed before creating additional ratio-based features. The dataset was divided into training and testing sets.

Two regression models were evaluated:
- Linear Regression as the baseline model
- Random Forest Regression as the main nonlinear model

Five-fold cross-validation was used to check model consistency. GridSearchCV was then used to tune the Random Forest hyperparameters.

## 4. Model Evaluation

### Linear Regression
- MAE: 0.4862
- RMSE: 0.6753
- R²: 0.6519

### Random Forest Regression
- MAE: 0.3276
- RMSE: 0.5034
- R²: 0.8066

The Random Forest model performed substantially better than the Linear Regression baseline.

## 5. Cross-Validation
- Mean CV RMSE: 0.5112

## 6. Hyperparameter Tuning
The best Random Forest parameters were:
- `n_estimators`: 200
- `max_depth`: 25
- `min_samples_split`: 2

Best cross-validation RMSE: 0.51718

## 7. Final Model Results
- Final MAE: 0.3278
- Final RMSE: 0.5037
- Final R²: 0.8064

The final Random Forest model achieved an R² of approximately 0.81.

## 8. Error Analysis
The mean residual was -0.01178. Residuals were analyzed using actual-versus-predicted and residual-distribution plots.

## 9. Feature Importance
The most important features were:
1. MedInc – 0.522553
2. AveOccup – 0.127483
3. Latitude – 0.083648
4. Longitude – 0.083616
5. HouseAge – 0.051987
6. BedroomsPerRoom – 0.029416
7. Population – 0.026808
8. RoomsPerHousehold – 0.026436
9. AveRooms – 0.025392
10. AveBedrms – 0.022661

## 10. Model Saving
The trained model was successfully saved as `house_price_model.joblib`.

## 11. Conclusion
This project demonstrates a complete regression workflow from data preparation to model evaluation and tuning. Linear Regression was used as a baseline, while Random Forest provided stronger predictive performance.

Feature engineering, cross-validation, hyperparameter tuning, and error analysis were applied to assess and improve the model. The final trained model achieved an MAE of 0.3278, RMSE of 0.5037, and R² of 0.8064 on the test set.
