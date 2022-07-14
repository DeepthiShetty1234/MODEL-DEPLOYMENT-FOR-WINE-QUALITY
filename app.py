import numpy as np
from flask import Flask, request, render_template
import pickle


app = Flask(__name__)



def main():
    return render_template('index.html')


    
    output = round(predict([0], 2))
     
    return render_template('index.html', prediction_text='quality is {}'.format(output))
     
    if __name__ == "__main__":
        
        app.run()