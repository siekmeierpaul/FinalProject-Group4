from flask import Flask, jsonify
from flask import render_template 
import pandas as pd
import numpy as np

app = Flask(__name__)

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

@app.route('/Survey/<answers>')
def TakeSurvey(answers):
    data = []
    for answer in answers:
        data.append(answer)
    dataDF = np.array(data)

    result = 'divorce'
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)