from datetime import datetime, date
import joblib
import pandas as pd

def date_range(last_date, predict_date):
    """
    Range of date from last date to predict date
    """
    last_date = datetime.strptime(last_date, "%Y-%m-%d")
    predict_date = datetime.strptime(predict_date, "%Y-%m-%d")
    date = pd.date_range(last_date, predict_date)
    date = date[1:]
    date = [d.strftime("%Y-%m-%d") for d in date]
    return date

def n_days_predicted(last_date, predict_date):
    """
    Counting the days from today to predict day
    """
    last_date = datetime.strptime(last_date, "%Y-%m-%d")
    predict_date = datetime.strptime(predict_date, "%Y-%m-%d")
    n = predict_date-last_date
    n = n.days
    return n


def forecast(model, days):
    """
    Forecasting the average temperature
    """
    forecast = model.forecast(days)
    forecast = forecast.tolist()
    return forecast

def predict(model, last_date, predict_date):
    """
    Predicting the average temperature
    """
    date = date_range(last_date, predict_date)
    days = n_days_predicted(last_date, predict_date)
    pred = forecast(model, days)
    return date, pred