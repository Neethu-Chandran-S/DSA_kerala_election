from flask import Flask,render_template,request
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

prediction_values = pd.read_csv("prediction_values (1).csv")
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

@app.route("/prediction", methods = ["GET","POST"])
def predicted():
        if request.method == 'POST':
             
             yr = request.form['yr'] 
             sex = request.form['sex']
             party = request.form['party'] 
             
             cname = request.form['cname']
             ptyp = request.form["ptyp"]
             tcoat = request.form['tcoat']
             icu = request.form['icu']
             

             results=0
             candidate_prediction =  {
                                    "Year": yr,
                                    "Sex": sex,
                                    "Party": party,
                                    
                                    "Constituency_Name": cname,
                                    "Party_Type_TCPD": ptyp,
                                     "Turncoat": tcoat,
                                    "Incumbent": icu,
                                    "Results" :results
                                    
                                    }
             
             #dataframe
             candidate_predictdf = pd.DataFrame([candidate_prediction])

             # encoding
             encoder = pickle.load(open('l_encoder.pkl','rb'))
             encoder.fit_transform(prediction_values["Sex"])
             candidate_predictdf['Sex'] = encoder.transform(candidate_predictdf['Sex'])

             encoder.fit_transform(prediction_values["Party"])
             candidate_predictdf['Party'] = encoder.transform(candidate_predictdf['Party'])

             encoder.fit_transform(prediction_values["Constituency_Name"])
             candidate_predictdf["Constituency_Name"] = encoder.transform(candidate_predictdf["Constituency_Name"])

             encoder.fit_transform(prediction_values["Party_Type_TCPD"])
             candidate_predictdf["Party_Type_TCPD"] = encoder.transform(candidate_predictdf["Party_Type_TCPD"])

             encoder.fit_transform(prediction_values["Turncoat"])
             candidate_predictdf["Turncoat"] = encoder.transform(candidate_predictdf["Turncoat"])

             encoder.fit_transform(prediction_values["Incumbent"])
             candidate_predictdf["Incumbent"] = encoder.transform(candidate_predictdf["Incumbent"])
             x = candidate_predictdf
             print(x)

             #scaling
             scalar = pickle.load(open('std_scalar.pkl','rb'))

             scalar.fit_transform(encoded_values)
             candidate_predict_scaled = scalar.transform(candidate_predictdf)
             
             print("Scaled ", candidate_predict_scaled)
             #x = candidate_predict_scaled

             #modeling
             pickled_model = pickle.load(open('svc_newmodel (1).pkl','rb'))

             results = pickled_model.predict(candidate_predict_scaled)     

             return render_template('pred.html',yr = yr, 
             sex = sex,
             party = party,
             cname = cname,
             ptyp = ptyp,
             tcoat=tcoat,
             icu = icu,
             res = results)
     
             
             
         

if __name__ == "__main__":
    app.run()