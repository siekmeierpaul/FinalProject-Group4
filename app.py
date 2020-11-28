import numpy as np 
import pickle
from flask import Flask, request
from flask import render_template

app = Flask(__name__)

# Load the pickled model 
with open("pickle_model.pkl", 'rb') as file:
    pickle_model = pickle.load(file)

@app.route('/')
def IndexRoute():
    webpage = render_template("index.html")
    return webpage

@app.route('/data')
def DataPage():
    webpage = render_template("data.html")
    return webpage

@app.route('/results')
def ResultsPage():
    webpage = render_template("results.html")
    return webpage

@app.route('/predict',methods=['POST'])
def predict():
    # get the list from the website
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)] 
    print(final_features)


    # make a prediction
    prediction = pickle_model.predict(final_features)
    print(prediction)

    webpage = render_template("data.html")
    return webpage

if __name__ == '__main__':
    app.run(debug=True)