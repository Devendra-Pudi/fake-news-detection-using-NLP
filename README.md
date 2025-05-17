
# 📰 Fake News Detection Using NLP and Machine Learning

This project aims to detect fake news using Natural Language Processing (NLP) and Machine Learning algorithms. It leverages techniques such as TF-IDF vectorization and various classifiers (Logistic Regression, Passive Aggressive, etc.) to predict the authenticity of a news headline or article.

## 🔗 Project Link

GitHub Repository: [Fake News Detection](https://github.com/Devendra-Pudi/fake-news-detection-NLP)

---

## 🧠 Technologies Used

- Python
- Flask (for web interface)
- HTML/CSS/JavaScript (frontend)
- Scikit-learn
- Pandas / NumPy
- Natural Language Toolkit (NLTK)
- Jupyter Notebook

---

## 📁 Folder Structure

```
├── app/                   # Flask backend
├── templates/             # HTML templates
├── static/                # CSS/JS files
├── model/                 # Trained ML model(s)
├── dataset/               # News dataset (CSV)
├── main.ipynb             # Jupyter Notebook for model training
├── app.py                 # Flask main application
└── README.md              # Project documentation
```

---

## 🧪 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/Devendra-Pudi/fake-news-detection-NLP.git
cd fake-news-detection-NLP
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask App

```bash
python app.py
```

Then go to your browser and open: `http://127.0.0.1:5000/`

---

## 🔍 Features

- Detect fake news from input text
- Clean UI built using HTML/CSS/JS
- TF-IDF Vectorization
- Logistic Regression and Passive Aggressive Classifier
- Easy-to-use Flask interface

---

## 📊 Sample Dataset

The project uses a dataset with news headlines and labels (`REAL` or `FAKE`). You can replace this with any custom dataset in CSV format.

---

## 📌 Future Improvements

- Add deep learning model (e.g., LSTM)
- Add multilingual support
- Improve UI/UX
- Deploy using Docker or cloud services (e.g., Heroku)

---

## 🙌 Author

**Devendra Pudi**

GitHub: [@Devendra-Pudi](https://github.com/Devendra-Pudi)

---

## 📃 License

This project is licensed under the MIT License.
