
# 📰 Fake News Detection Using NLP and Machine Learning

This project aims to detect fake news using Natural Language Processing (NLP) and Machine Learning algorithms. It leverages techniques such as TF-IDF vectorization and various classifiers (Logistic Regression, Passive Aggressive, etc.) to predict the authenticity of a news headline or article.

## 🔗 Project Link

GitHub Repository: [Fake News Detection](https://github.com/Devendra-Pudi/fake-news-detection-NLP)

Try My Project: 
- GitHub Pages: [Fake News Detector](https://devendra-pudi.github.io/fake-news-detection-using-NLP/)

---

## 🧠 Technologies Used

- Python
- Flask (for web interface)
- HTML/CSS/JavaScript (frontend)
- Scikit-learn
- Pandas / NumPy
- Natural Language Toolkit (NLTK)
- Jupyter Notebook
- Render (for Deployment)

---

## 📁 Folder Structure

```
├── .github/workflows/     # GitHub Actions workflows
├── templates/             # HTML templates
├── static/                # CSS/JS files
├── model/                 # Trained ML model(s)
├── dataset/               # News dataset (CSV)
├── _site/                 # Generated static files for GitHub Pages
├── app.py                 # Flask main application
├── generate_static.py     # Script to generate static files for GitHub Pages
├── README.md              # Project documentation
└── render.yaml            # Configuration for Render deployment
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

## 🚀 Deployment

This project is deployed in two ways:

### 1. GitHub Pages (Static Version)

The static version is deployed using GitHub Actions and GitHub Pages. The workflow:

1. When changes are pushed to the main branch, GitHub Actions is triggered
2. The workflow runs `generate_static.py` to create static HTML files with relative paths
3. The generated files are deployed to GitHub Pages

The static version doesn't have backend functionality but demonstrates the UI.

### 2. Railway App (Full Version)

The full version with backend functionality is deployed on Railway using the configuration in `render.yaml`.

---

## 📌 Future Improvements

- Add deep learning model (e.g., LSTM)
- Add multilingual support
- Improve UI/UX
- Add more deployment options

---

## 🙌 Author

**Devendra Pudi**

GitHub: [@Devendra-Pudi](https://github.com/Devendra-Pudi)

---

## 📃 License

This project is licensed under the MIT License.
