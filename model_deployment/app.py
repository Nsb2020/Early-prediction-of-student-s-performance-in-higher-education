from flask import Flask, request, render_template
import sklearn
import pickle
import joblib
import pandas as pd


# Use pickle to load in the trained model
# with open(f'model/titanic_model_stkd.pkl', 'rb') as f:
model = joblib.load('model/ensemble_classifier_model.pkl')

app = Flask(__name__, template_folder='templates',
            static_folder='static')


@app.route('/')
def index():
    return render_template('main.html')


@app.route("/submit", methods=['POST'])
def form_submit():
    Age = request.json['age']
    Course = request.json['course']
    Tuition = request.json['tuition']
    Pclass = request.json['pclass']
    Curricular1A = request.json['curricular1A']
    Curricular1E = request.json['curricular1E']
    Curricular1G = request.json['curricular1G']
    Curricular2A = request.json['curricular2A']
    Curricular2E = request.json['curricular2E']
    Curricular2G = request.json['curricular2G']

    data = {
        'Age': Age,
        #'Curricular units for 1st semester': 
    }
    print(data)

    # df = pd.DataFrame.from_dict([data])
    # print(df)
    # return render_template('main.html')

    # Get the model prediction
    # prediction = model.predict(df)
    # print(prediction)
    # To render the form again, but add in the predictions and remind the user of previous input
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)
