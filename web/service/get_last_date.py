import pandas as pd

NEW_DATA_PATH = 'project/temperature-prediction-w-arima/data/tambahan.csv'
NEW_DATA = pd.read_csv(NEW_DATA_PATH)

def get_last_date():
    """
    Get the last date in the dataset
    """
    last_date = NEW_DATA['Tanggal'].iloc[-1]
    # print(last_date)
    return last_date

def tomorrow_date():
    """
    Get the last date in the dataset
    """
    last_date = NEW_DATA['Tanggal'].iloc[-1]
    date = pd.to_datetime(last_date) + pd.DateOffset(days=1)
    date = date.strftime("%Y-%m-%d")
    return date

def after_tomorrow_date():
    """
    Get the last date in the dataset
    """
    last_date = NEW_DATA['Tanggal'].iloc[-1]
    date = pd.to_datetime(last_date) + pd.DateOffset(days=2)
    date = date.strftime("%Y-%m-%d")
    return date