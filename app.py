from flask import Flask, render_template, request
import joblib
import re
import numpy as np
import warnings
import os

warnings.filterwarnings("ignore", category=UserWarning)

app = Flask(__name__, static_folder='static', template_folder='templates')

# Load model and vectorizer
try:
    model = joblib.load('model/model.pkl')
    vectorizer = joblib.load('model/vectorizer.pkl')
except Exception as e:
    raise RuntimeError(f"Model or vectorizer couldn't be loaded: {e}")

# Preprocessing
def preprocess(text):
    text = re.sub('[^a-zA-Z]', ' ', text)
    return text.lower()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        text = request.form.get('message', '')
        if not text.strip():
            return render_template('result.html', prediction="No input provided", text=text)

        processed_text = preprocess(text)
        vectorized_text = vectorizer.transform([processed_text])
        prediction = model.predict(vectorized_text)[0]
        confidence = model.predict_proba(vectorized_text)[0][prediction] * 100

        label = "Fake" if prediction == 1 else "Real"
        return render_template('index.html', pred=label, confidence=round(confidence, 2), text=text)

if __name__ == '__main__':
    app.run(debug=True)
