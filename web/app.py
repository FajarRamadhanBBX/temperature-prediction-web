from flask import Flask, render_template, request
import json
import joblib
import pandas as pd
from service.prediction import *
from service.get_last_date import *

app = Flask(__name__, template_folder='templates', static_folder='static')

MODEL_PATH = 'project/temperature-prediction-w-arima/model/model_prediction.joblib'
MODEL = joblib.load(MODEL_PATH)
NEW_DATA_PATH = 'project/temperature-prediction-w-arima/data/tambahan.csv'
NEW_DATA = pd.read_csv(NEW_DATA_PATH)

@app.route('/')
def index():
    date = tomorrow_date()
    return render_template('index.html', tomorrow_date=date)

@app.route('/predict', methods=['POST'])
def predict():
    predict_date = request.form['predict_date']
    last_date = get_last_date()
    date = date_range(last_date, predict_date)
    days = n_days_predicted(last_date, predict_date)
    pred = forecast(MODEL, days)
    return render_template('predict.html', date=date, pred=pred)

@app.route('/add_data', methods=['POST'])
def add_data():
    global NEW_DATA
    date = tomorrow_date()
    data = request.form['new-data']
    new_row = pd.DataFrame({'Tanggal':[date], 'Tavg':[data]})
    NEW_DATA = pd.concat([NEW_DATA, new_row], ignore_index=True)
    NEW_DATA.to_csv(NEW_DATA_PATH, index=False)
    date_after_add = after_tomorrow_date()
    return render_template('index.html', tomorrow_date=date_after_add)

if __name__ == '__main__':
    app.run(debug=True)