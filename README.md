# USU CalFire: California Weather and Fire Prediction

Short notebook for exploring and modeling daily California fire starts using combined NOAA weather and CAL FIRE data (1984–2023). It builds features (including cyclic day-of-year), checks multicollinearity (VIF), trains multiple classifiers , and provides a simple prediction example.

- Notebook: USU_Calfire.ipynb (+ printed pdf)
- Data: CA_Weather_Fire_Dataset_1984-2025.csv (public)
  - Source: https://scholars.georgiasouthern.edu/en/datasets/california-weather-and-fire-prediction-dataset-19842025-with-engi

## Requirements
- Python 3.9+
- Packages: pandas, numpy, seaborn, matplotlib, scikit-learn, statsmodels, jupyter

Install:
```
pip install pandas numpy seaborn matplotlib scikit-learn statsmodels jupyter
```

## Usage
1. Place CA_Weather_Fire_Dataset_1984-2025.csv in the project root.
2. Open USU_Calfire.ipynb in Jupyter/Lab.
3. Run cells sequentially.
4. Optional: adjust the “Prediction” cell inputs and choose model ('logreg'|'svc'|'rf'|'gb').

Notes:
- The split is chronological (no shuffling) to respect time order.
- Models: Logistic Regression, SVC, RandomForest, GradientBoosting with StandardScaler in pipelines.
- Metrics include F1, ROC AUC, PR AUC, and log loss.

## Future steps:
- Load automatically the weather forecast from https://api.weather.gov/points/ using requests library and create a prediction for next week.
