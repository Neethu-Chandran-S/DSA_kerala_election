from flask import Flask,render_template
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()