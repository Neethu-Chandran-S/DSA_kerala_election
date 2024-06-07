from flask import Flask,render_template
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

prediction_values = pd.read_csv("prediction_values.csv")
encoded_values = pd.read_csv("tobe_scaled.csv")

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/knowledge_center')
def knowledge_center():
    return render_template('Knowledge.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

if __name__ == "__main__":
    app.run()