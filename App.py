from flask import Flask, request, render_template
import numpy as np
import pickle

# Load the model
model = pickle.load(open("BreastCancerModel.pkl", "rb"))

# Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = request.form['feature']
    features = features.split(',')

    # Strip whitespace and convert to float
    try:
        np_features = np.asarray([float(f.strip()) for f in features], dtype=np.float32)
    except ValueError:
        message = ["Please enter valid numeric values."]
        return render_template('index.html', message=message)

    # Check if the number of features is correct
    if len(np_features) != 31:
        message = ["Please enter exactly 31 features."]
        return render_template('index.html', message=message)

    # Prediction
    pred = model.predict(np_features.reshape(1, -1))
    message = ['Cancerous' if pred[0] == 1 else 'Not Cancerous']

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
