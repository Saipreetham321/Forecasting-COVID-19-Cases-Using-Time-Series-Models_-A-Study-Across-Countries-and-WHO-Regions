# Forecasting COVID-19 Cases Using Time Series Models 📈

This project focuses on building and evaluating time series models (ARIMA and SARIMAX) to forecast the number of confirmed COVID-19 cases. The analysis is conducted on both a global scale and for a specific country (India) to compare model performance and understand underlying data patterns.

***

## 📜 Table of Contents
* [Project Objective](#project-objective)
* [Getting Started](#getting-started)
* [Project Structure](#project-structure)
* [Methodology](#methodology)
* [Results](#results)
* [Contributing](#contributing)
* [License](#license)

***

## 🎯 Project Objective
The primary goal of this project is to leverage time series forecasting techniques to predict future trends in COVID-19 cases. The key objectives include:
* Exploring and visualizing trends, seasonality, and other patterns in COVID-19 data.
* Building, training, and evaluating ARIMA and SARIMAX models.
* Comparing the performance of the models to determine which is better suited for this type of data.
* Discussing the implications of the forecasts for public health planning and resource allocation.

***

## 🚀 Getting Started
Follow these instructions to set up the project environment and run the analysis on your local machine.

### Prerequisites
Make sure you have **Python 3.7** or a newer version installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation
1.  Clone the repository:
    ```bash
    git clone https://github.com/Saipreetham321/Forecasting-COVID-19-Cases-Using-Time-Series-Models_-A-Study-Across-Countries-and-WHO-Regions.git
    cd Forecasting-COVID-19-Cases-Using-Time-Series-Models_-A-Study-Across-Countries-and-WHO-Region
    ```
2.  Install the required Python libraries:
    A `requirements.txt` file is included for easy installation.
    ```bash
    pip install -r requirements.txt
    ```

### Usage
To run the complete analysis, simply execute the main Python script from your terminal:
```bash
python your_script_name.py
```
# COVID-19 Time Series Forecasting Analysis

This script will:

* Load and preprocess the `covid_19_clean_complete.csv` dataset.
* Perform a full analysis (stationarity tests, model building, evaluation, and visualization) for both global and India-specific data.
* Print the results, including model summaries and evaluation tables, to the console.
* Display the forecast graphs.

## 📁 Project Structure

The repository is organized as follows:
```

├── data/
│   └── covid_19_clean_complete.csv    # The dataset used for the analysis
├── Source_code.py                # The main Python script for the analysis
├── requirements.txt                   # A list of required Python libraries
└── README.md                          # This README file
```
## 🛠️ Methodology

### Data Exploration

* **Trend Analysis:** Moving averages were used to identify long-term trends in the data.
* **Seasonality Analysis:** Seasonal decomposition and box plots revealed a strong weekly pattern in the data.
* **Stationarity Test:** The Augmented Dickey-Fuller (ADF) test was used to check if the data was stationary.

### Models Used

* **ARIMA (Autoregressive Integrated Moving Average):** A standard model for non-seasonal time series data.
* **SARIMAX (Seasonal ARIMA with eXogenous variables):** An extension of ARIMA that is capable of modeling seasonality, making it well-suited for this dataset.

### Evaluation Metrics

* **RMSE (Root Mean Squared Error):** Measures the average magnitude of the forecast errors.
    $RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}$

* **MAPE (Mean Absolute Percentage Error):** Measures the average percentage difference between predicted and actual values.
    $MAPE = \frac{1}{n}\sum_{i=1}^{n}\left|\frac{y_i - \hat{y}_i}{y_i}\right| \times 100$

## 📊 Results

The analysis demonstrated that the SARIMAX model consistently outperformed the ARIMA model for both global and country-specific forecasts. This is primarily due to SARIMAX's ability to effectively capture the strong weekly seasonality present in the COVID-19 case data.

| Dataset | Model   | RMSE     | MAPE    |
| :------ | :------ | :------- | :------ |
| Global  | ARIMA   | 2434.70  | 3.25%   |
| Global  | SARIMAX | 1898.33  | 2.51%   |
| India   | ARIMA   | 1341.13  | 3.11%   |
| India   | SARIMAX | 852.47   | 1.98%   |

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improving this project, please feel free to fork the repository and submit a pull request. You can also open an issue with the "enhancement" tag.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📝 License

This project is distributed under the MIT License. See the `LICENSE` file for more information.
