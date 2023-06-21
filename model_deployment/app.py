from flask import Flask, request, render_template, jsonify
import joblib
import pandas as pd


# Load the trained model
model = joblib.load('model/rf_classifier_model.pkl')

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('main.html')

@app.route("/submit", methods=['POST', 'GET'])
def form_submit():
    name = request.json['name']
    Age = request.json['age']
    Course = request.json['course']
    Tuition = request.json['tuition']
    Curricular1A = request.json['curricular1A']
    Curricular1EV = request.json['curricular1EV']
    Curricular1ER = request.json['curricular1ER']
    Curricular2A = request.json['curricular2A']
    Curricular2ER = request.json['curricular2ER']
    Curricular2EV = request.json['curricular2EV']
    Curricular2G = request.json['curricular2G']

    data = {
        0: Curricular1A,
        1: Curricular2A,
        2: Tuition,
        3: Course,
        4: Curricular2ER,
        5: Age,
        6: Curricular1EV,
        7: Curricular2EV,
        8: Curricular2G,
        9: Curricular1ER
    }

    df = pd.DataFrame.from_dict([data])

    prediction = model.predict(df)

    if int(prediction) == 0:
        result = 'Dropout'
    elif int(prediction) == 1:
        result = 'Enrolled'
    else:
        result = 'Graduate'
    return jsonify(result=result, name=name)

    #name = data.get('name', '')
    # return redirect(url_for('show_result', result=result, name=name))

@app.route("/result")
def show_result():
    result = request.args.get("result", "")
    name = request.args.get("name", "")
    return render_template("result.html", result=result, name=name)
    #eturn render_template("result.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)
