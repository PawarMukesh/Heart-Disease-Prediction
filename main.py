from flask import Flask, render_template, request # importing library
import jsonify
import pickle # it helps to load the model
import numpy as np
from sklearn.preprocessing import StandardScaler

app = Flask(__name__) # Creating app

model = pickle.load(open("Logistic_regression_model.pkl","rb")) # open model in read mode
@app.route('/',methods=['GET']) # If someone hitting the webside that time method will be get
def Home():
    return render_template('index.html') #Pushing the UI or html code

# Start Preprocessing
standard_to = StandardScaler()
@app.route("/predict",methods=['POST']) # Collect the inputs
def predict():
    if request.method == 'POST':
        sop = int(request.form['sop'])
        thal_normal = request.form['thal_normal']
        if (thal_normal == 'normal'):
            thal_normal = 2
            thal_reversible_defect = 1
            fixed_defect = 0
        else:
            thal_normal = 0
            thal_reversible_defect = 2
            thal_fixed_defect = 1

        resting_bp= float(request.form['resting_bp'])
        cpt = int(request.form['cpt'])
        major_vessels = int(request.form['major_vessels'])
        fasting_blood_sugar = int(request.form['fasting_blood_sugar'])
        ekg_result = int(request.form['ekg_result'])
        serum_cholesterol = float(request.form['serum_cholesterol'])
        oldpeak_st_depression= float(request.form['oldpeak_st_depression'])
        sex = int(request.form['sex'])
        age = float(request.form['age'])
        max_heart_rate = float(request.form['max_heart_rate'])
        exercise_induced_angina = int(request.form['exercise_induced_angina'])


        prediction = model.predict(np.array([[sop,thal_normal , resting_bp, cpt, major_vessels, fasting_blood_sugar, ekg_result, serum_cholesterol, oldpeak_st_depression, sex, age, max_heart_rate, exercise_induced_angina ]]).reshape(1,13))

        output = round(prediction[0],2) # Predict the model with condition

        if output == 0: # Condition for output
            return render_template('index.html',pred="The Patient Has Not heart Disease") # Connect ot html page and app
        else:
            pred = "The Patient has Heart Disease ".format(output)
            return render_template('index.html', pred=pred)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)





