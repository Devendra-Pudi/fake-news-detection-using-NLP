import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os
import re

# Load datasets
true = pd.read_csv('dataset/true.csv')
fake = pd.read_csv('dataset/fake.csv')

# Label datasets
true['label'] = 0
fake['label'] = 1
data = pd.concat([true, fake])

# Preprocessing
data['text'] = data['title'] + ' ' + data['text']
data = data.sample(frac=1).reset_index(drop=True)

# Clean text
def clean_text(text):
    text = re.sub('[^a-zA-Z]', ' ', text)
    return text.lower()

data['text'] = data['text'].apply(clean_text)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(data['text'])
y = data['label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model training
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Save model and vectorizer
os.makedirs('model', exist_ok=True)
joblib.dump(model, 'model/model.pkl')
joblib.dump(vectorizer, 'model/vectorizer.pkl')
