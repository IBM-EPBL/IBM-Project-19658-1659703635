
from flask import Flask, render_template, request
import requests,joblib


app = Flask(__name__, static_url_path='')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/checkEligibility')
def checkEligibility():
    return render_template('Demo2.html')

@app.route('/predict', methods=['POST'])
def predict():
    greScore = int(request.form['greScore'])
    toeflScore = int(request.form['toeflScore'])
    univRank = int(request.form['univRank'])
    sop = float(request.form['sop'])
    lor = float(request.form['lor'])
    cgpa = float(request.form['cgpa'])
    research = int(request.form['research'])
    array_of_input_fields = ['greScore', 'toeflScore', 'univRank', 'sop', 'lor', 'cgpa', 'research']
    array_of_values_to_be_scored = [greScore, toeflScore, univRank, sop, lor, cgpa, research]
    
    model = joblib.load('model.pkl')
    result = model.predict(X)[0]
    print(result)

    if result>0.5:
        return render_template('chance.html')
    else:
        return render_template('noChance.html')


if __name__ == "__main__":
    app.run()
