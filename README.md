# Time Series Analysis of Algiers Temperature Data

## Overview
This repository contains an individual project for Time Series Analysis Course (TSAC) that examines historical temperature data from Algiers spanning from 2002 to 2023. The project applies time series analysis techniques to model, analyze, and forecast temperature patterns.

## Project Objective
The main objectives of this project are:
- Analyze historical temperature patterns in Algiers
- Identify seasonal components and trends in temperature variations
- Develop and validate SARIMA models for temperature prediction
- Evaluate forecast accuracy and model performance
- Apply time series analysis techniques in a meteorological context

## Data
The dataset (`data/algiers_temp.csv`) contains daily temperature readings from Algiers from January 2002 to August 2023, providing over 20 years of historical data for analysis. This extensive time range allows for thorough examination of seasonal patterns, trends, and potential climate change effects.

## Methodology
The project follows these analytical steps:
1. **Data Exploration and Preprocessing**:
   - Time series visualization
   - Testing for stationarity
   - Transformation and differencing
   - Analysis of monthly vs. daily patterns

2. **Model Specification**:
   - Identification of potential SARIMA parameters
   - ACF and PACF analysis
   - Testing multiple model specifications
   - Model selection based on information criteria (AIC, BIC, AICc)

3. **Model Fitting and Diagnostics**:
   - Residual analysis
   - Testing for normality and autocorrelation
   - Assessing model adequacy

4. **Forecasting**:
   - Generation of temperature forecasts
   - Confidence interval analysis
   - Evaluation using accuracy metrics (RMSE, MAE, MAPE)

## Repository Structure
```
.
├── data/
│   └── algiers_temp.csv       # Algiers historical temperature data
├── notebooks/
│   └── tsa.ipynb              # Main analysis notebook
├── README.md                  # Project description and documentation
└── [additional files]
```

## Setup and Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/LyesHADJAR/TSAC-Individual-Project.git
   cd TSAC-Individual-Project
   ```

2. The analysis is performed in R within Jupyter Notebook. Make sure you have the following libraries installed:
   ```r
   install.packages(c("ggplot2", "forecast", "TSA", "tseries", "dplyr",
                     "knitr", "gridExtra", "MASS", "lawstat",
                     "FinTS", "ggthemes"))
   ```

3. Open and run the notebook:
   ```bash
   jupyter notebook notebooks/tsa.ipynb
   ```
   
4. The final project report will be available as a Google Colab notebook.

## Dependencies
- R (>= 4.0)
- R packages:
  - forecast
  - tseries
  - ggplot2
  - dplyr
  - gridExtra
  - knitr
  - MASS
  - lawstat
  - FinTS
- Jupyter Notebook

## Project Status
🏁 Final stages - Due on March 29, 2025 (5 days remaining) 🏁

## Author
- Lyes HADJAR

## License
This project is created for educational purposes as part of a course assignment.

## Acknowledgments
- All data sources are properly cited within the project notebook
- Temperature data obtained from historical weather archives for Algiers