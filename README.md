# Time Series Analysis of Bitcoin Prices

## Overview
This repository contains an individual project for Time Series Analysis Course (TSAC) that examines historical Bitcoin price data from 2014 to 2024. The project applies time series analysis techniques, specifically SARIMA models, to analyze patterns, build forecasting models, and predict future Bitcoin price movements.

## Project Objective
The main objectives of this project are:
- Analyze historical Bitcoin price trends and patterns
- Identify seasonal components in Bitcoin price movements
- Develop and validate SARIMA models for Bitcoin price prediction
- Evaluate forecast accuracy and model performance
- Apply time series analysis techniques in a real-world financial context

## Data
The dataset (`data/bitcoin_data.csv`) contains daily Bitcoin closing prices from September 2014 to 2024, providing approximately 10 years of historical data for analysis. This extensive time range allows for identification of both short-term fluctuations and long-term trends in the cryptocurrency market.

## Methodology
The project follows these analytical steps:
1. **Data Exploration and Preprocessing**:
   - Time series visualization
   - Testing for stationarity
   - Transformation and differencing
   - Analysis of Bitcoin returns

2. **Model Specification**:
   - Identification of potential SARIMA parameters
   - ACF and PACF analysis
   - Testing multiple model specifications
   - Model selection based on information criteria

3. **Model Fitting and Diagnostics**:
   - Residual analysis
   - Testing for normality and autocorrelation
   - Assessing model adequacy

4. **Forecasting**:
   - Generation of price forecasts
   - Confidence interval analysis
   - Evaluation using accuracy metrics (RMSE, MAE, MAPE)

## Repository Structure
```
.
├── data/
│   └── bitcoin_data.csv       # Bitcoin historical price data
├── notebooks/
│   └── bitcoin-prices-analysis.ipynb  # Main analysis notebook
├── README.md                  # Project description and documentation
└── [additional files]
```

## Setup and Usage
1. Clone this repository:
   ```
   git clone https://github.com/LyesHADJAR/TSAC-Individual-Project.git
   cd TSAC-Individual-Project
   ```

2. The analysis is performed in R within Jupyter Notebook. Make sure you have the following libraries installed:
   - ggplot2
   - forecast
   - tseries
   - Metrics
   - urca

3. Open and run the notebook:
   ```
   jupyter notebook notebooks/bitcoin-prices-analysis.ipynb
   ```
   
4. The final project report will be available as a Google Colab notebook.

## Dependencies
- R (>= 4.0)
- R packages:
  - forecast
  - tseries
  - ggplot2
  - Metrics
  - urca
- Jupyter Notebook

## Project Status
🚧 In progress - Due on March 29, 2025 🚧

## Author
- Lyes HADJAR

## License
This project is created for educational purposes as part of a course assignment.

## Acknowledgments
- All data sources are properly cited within the project notebook