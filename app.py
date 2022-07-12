import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open("C:/Users/G Guruvaiah/Desktop/MACHINE LEARNING PROJECTS/Wine Deployment/model/wine_model.pkl", 'rb'))

def home():
    return render_template('index.html')
    
    def predict():

    int_features = [float(x) for x in request.form.values()] 
    features = [np.array(int_features)]  
    prediction = model.predict(features) 
    
     output = round(predict([0], 2))
     
     return render_template('index.html', prediction_text='quality is {}'.format(output))
     
     if __name__ == "__main__":
    app.run()