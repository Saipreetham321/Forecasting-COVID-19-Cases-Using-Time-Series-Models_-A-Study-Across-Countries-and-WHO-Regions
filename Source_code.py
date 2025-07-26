import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.api import ARIMA, SARIMAX
from sklearn.metrics import mean_squared_error
from prettytable import PrettyTable # type: ignore
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")

def perform_adf_test(series, series_name):
    result = adfuller(series.dropna())
    
    table = PrettyTable()
    table.title = f"Augmented Dickey-Fuller Test for {series_name}"
    table.field_names = ["Metric", "Value"]
    table.align["Metric"] = "l"
    table.align["Value"] = "r"
    
    table.add_row(["ADF Statistic", f"{result[0]:.4f}"])
    table.add_row(["p-value", f"{result[1]:.4f}"])
    table.add_row(["-"*15, "-"*15])
    table.add_row(["Critical Values:", ""])
    for key, value in result[4].items():
        table.add_row([f"    {key}", f"{value:.4f}"])
    table.add_row(["-"*15, "-"*15])
    
    conclusion = "Data is likely stationary." if result[1] <= 0.05 else "Data is likely non-stationary."
    table.add_row(["Conclusion", conclusion])
    
    print(table)
    print("\n")


def evaluate_forecast(y_true, y_pred, model_name, data_name):
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mape = np.mean(np.abs((y_true - y_pred) / np.where(y_true == 0, 1, y_true))) * 100
    
    table = PrettyTable()
    table.title = f"{model_name} Model Evaluation for {data_name}"
    table.field_names = ["Metric", "Value"]
    table.align["Metric"] = "l"
    table.align["Value"] = "r"
    
    table.add_row(["RMSE", f"{rmse:.4f}"])
    table.add_row(["MAPE", f"{mape:.4f}%"])
    
    print(table)
    print("\n")

def run_forecasting_analysis(data_series, name):
    print(f"\n{'='*20} Running Analysis for: {name} {'='*20}\n")

    perform_adf_test(data_series, name)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    plot_acf(data_series.dropna(), ax=ax1, lags=40)
    plot_pacf(data_series.dropna(), ax=ax2, lags=40)
    plt.suptitle(f'ACF and PACF for Daily New Cases in {name}', fontsize=16)
    plt.show()
    
    train_size = int(len(data_series) * 0.9)
    train, test = data_series[0:train_size], data_series[train_size:]

    try:
        arima_model = ARIMA(train, order=(7, 1, 1)).fit()
        print(arima_model.summary())
        arima_pred = arima_model.forecast(steps=len(test))
        
        evaluate_forecast(test, arima_pred, "ARIMA", name)
        
        plt.figure(figsize=(14, 7))
        plt.plot(train.index, train, label='Training Data')
        plt.plot(test.index, test, label='Actual Cases (Test Data)', color='orange')
        plt.plot(test.index, arima_pred, label='ARIMA Forecast', color='green', linestyle='--')
        plt.title(f'ARIMA Model Forecast for {name}', fontsize=16)
        plt.legend()
        plt.show()
    except Exception as e:
        print(f"Could not run ARIMA model for {name}. Error: {e}")

    try:
        sarimax_model = SARIMAX(train, order=(6, 1, 1), seasonal_order=(1, 1, 1, 7)).fit(disp=False)
        print(sarimax_model.summary())
        sarimax_pred = sarimax_model.get_forecast(steps=len(test)).predicted_mean

        evaluate_forecast(test, sarimax_pred, "SARIMAX", name)

        plt.figure(figsize=(14, 7))
        plt.plot(train.index, train, label='Training Data')
        plt.plot(test.index, test, label='Actual Cases (Test Data)', color='orange')
        plt.plot(test.index, sarimax_pred, label='SARIMAX Forecast', color='red', linestyle='--')
        plt.title(f'SARIMAX Model Forecast for {name}', fontsize=16)
        plt.legend()
        plt.show()
    except Exception as e:
        print(f"Could not run SARIMAX model for {name}. Error: {e}")


def analyze_and_forecast(file_path='covid_19_clean_complete.csv'):
    try:
        df = pd.read_csv(file_path)
        df['Date'] = pd.to_datetime(df['Date'])
        
        global_cases = df.groupby('Date')['Confirmed'].sum().reset_index()
        global_cases.set_index('Date', inplace=True)
        global_cases['Daily New Cases'] = global_cases['Confirmed'].diff().fillna(0)
        global_data_series = global_cases['Daily New Cases']['2020-03-01':'2020-07-27']
        run_forecasting_analysis(global_data_series, "Global")

        country_name = 'India'
        country_cases = df[df['Country/Region'] == country_name].copy()
        country_cases = country_cases.groupby('Date')['Confirmed'].sum().reset_index()
        country_cases.set_index('Date', inplace=True)
        country_cases['Daily New Cases'] = country_cases['Confirmed'].diff().fillna(0)
        country_data_series = country_cases['Daily New Cases']['2020-03-01':'2020-07-27']
        run_forecasting_analysis(country_data_series, f"Country: {country_name}")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    analyze_and_forecast()
