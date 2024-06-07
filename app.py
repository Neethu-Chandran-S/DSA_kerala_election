from flask import Flask
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'hello'

if __name__ == "__main__":
    app.run()