from flask import Flask
from flask import render_template 

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

if __name__ == '__main__':
    app.run(debug=True)