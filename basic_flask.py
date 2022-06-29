from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "The default route shown by slash"

@app.route('/project')
def project():
    return "Heart Disease Prediction"

if __name__ == '__main__':
    app.run()