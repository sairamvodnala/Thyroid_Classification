# -*- coding: utf-8 -*-
"""
Created on Friday Nov 12 14:11:36 2021

@author: Sairam Vodnala
"""
import traceback
import numpy as np
from flask import Flask,request,render_template
import pickle
try:
    app = Flask(__name__,template_folder='template')
    model = pickle.load(open('model.pkl', 'rb'))
    @app.route("/")
    def home():
     return render_template("index.html")
    @app.route("/form")
    def form():
     return render_template("form.html")
    @app.route("/output")
    def output(prediction):
     return render_template("output.html",prediction)
    @app.route("/about")
    def about():
     return render_template('about.html')
    @app.route('/predict',methods=['POST','GET'])
    def predict():
        features=[]
        tsh=request.form['TSH']
        age=request.form['age']
        onthy=request.form['onthyroxine']
        qhypo=request.form['queryhypothyroid']
        qhyper=request.form['queryhyperthyroid']
        fti=request.form['FTI']
        psych=request.form['psych']
        features.append(int(age))
        features.append(int(onthy))
        features.append(int(qhypo))
        features.append(int(qhyper))
        features.append(float(tsh))
        features.append(float(psych))
        features.append(float(fti))
        final_features = [np.array(features)]
        print(final_features)
        prediction = model.predict(final_features)
        print(prediction)
        if prediction[0]==1:
         return render_template('output.html', prediction='HypoThyroid!')
        elif prediction[0]==2:
         return render_template('output.html', prediction='HyperThyroid!')
        else:
            return render_template('output.html',prediction='Negative')
    if __name__ == "__main__":
        app.run(debug=True)
except :
    traceback.print_exc()

 
