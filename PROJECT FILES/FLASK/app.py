import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib
import json
import matplotlib
import matplotlib.pyplot as plt
import pandas
import os
app = Flask(__name__)
model = joblib.load("model.save")
trans=joblib.load('transform.save')





@app.route('/')
def predict():
    return render_template('sensors_predict.html')

@app.route('/y_predict',methods=['POST','GET'])
def y_predict():
    
    x_test = [[float(x) for x in request.form.values()]]
    print('actual',x_test)
    x_test=trans.transform(x_test)
    print(x_test)
    pred = model.predict(x_test)
    print(pred)

    return render_template('sensors_predict.html', prediction_text=('Permanent Magnet surface temperature: ',pred[0]))


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
   