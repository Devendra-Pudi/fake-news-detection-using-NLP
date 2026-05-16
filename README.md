<div align="center">

# 📰 Fake News Detection using NLP
### ML-powered misinformation classifier with a live web demo

[![Live Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-222222?style=for-the-badge&logo=github)](https://devendra-pudi.github.io/fake-news-detection-using-NLP/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Stars](https://img.shields.io/github/stars/Devendra-Pudi/fake-news-detection-using-NLP?style=for-the-badge)](https://github.com/Devendra-Pudi/fake-news-detection-using-NLP/stargazers)

> *Paste any news article. Our NLP model tells you if it's real or fake — in seconds.*

</div>

---

## 📖 Overview

**Fake News Detection** is a machine learning web application that classifies news articles as **Real** or **Fake** using Natural Language Processing techniques. It includes a complete ML pipeline — from data preprocessing and model training to a Flask web interface deployed via GitHub Pages.

---

## ✨ Features

- 🧠 **NLP-powered classification** — TF-IDF vectorization + ML classifier
- 📊 **Trained on real datasets** — high accuracy on benchmark fake news datasets
- 🌐 **Web interface** — clean Flask UI for easy text input and results
- 🚀 **CI/CD pipeline** — automated deployment via GitHub Actions to GitHub Pages
- 📦 **Modular codebase** — separate scripts for training, inference, and serving

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python |
| ML Framework | Scikit-learn |
| NLP | TF-IDF Vectorization, NLTK |
| Web Framework | Flask |
| Deployment | GitHub Pages + GitHub Actions |
| Data | CSV-based news datasets |

---

## 🚀 Getting Started

### Installation

```bash
# Clone the repository
git clone https://github.com/Devendra-Pudi/fake-news-detection-using-NLP.git
cd fake-news-detection-using-NLP

# Install dependencies
pip install -r requirements.txt

# Train the model
python train_model.py

# Run the Flask app
python app.py
```

Open `http://localhost:5000` in your browser.

---

## 📁 Project Structure

```
fake-news-detection-using-NLP/
├── dataset/            # Training & test datasets
├── model/              # Saved ML model files
├── static/             # CSS & JS assets
├── templates/          # HTML templates (Jinja2)
├── .github/workflows/  # CI/CD pipeline for GitHub Pages
├── app.py              # Flask web application
├── train_model.py      # Model training script
├── generate_static.py  # Static site generator for GH Pages
└── requirements.txt    # Python dependencies
```

---

## 🌍 Live Demo

**→ [devendra-pudi.github.io/fake-news-detection-using-NLP](https://devendra-pudi.github.io/fake-news-detection-using-NLP/)**

---

## 📄 License

This project is open-source. Feel free to fork, improve, and use it.

---

<div align="center">

Built with 🔍 by [Devendra Prasad Pudi](https://github.com/Devendra-Pudi)

⭐ Star this repo if you found it useful!

</div>
