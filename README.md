# 🏥 Diabetes Readmission Prediction

A machine learning project to predict 30-day hospital readmissions and segment patients into risk groups using real-world healthcare data. This project is designed to support personalized care, reduce avoidable readmissions, and improve hospital efficiency.

---

## 📖 Table of Contents

- [Description](#-description)
- [Installation](#-installation)
- [Usage](#-usage)
- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [Contributing](#-contributing)
- [Contact](#-contact)
- [Acknowledgements](#-acknowledgements)

---

## 📌 Description

Hospital readmissions are costly and often preventable. This project uses both supervised and unsupervised learning to:

- 🔍 **Predict** which patients are at risk of being readmitted within 30 days.
- 🧠 **Cluster** patients into distinct groups for personalized care strategies.
- 📊 **Analyze** healthcare data for trends and insights.

Built using a real-world dataset containing 100,000+ diabetic patient records, this project walks through the full machine learning workflow — from data cleaning to model deployment-ready evaluation.

---

## ⚙️ Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/ImanFasasi/diabetes-readmission-ml.git
cd diabetes-readmission-ml
pip install -r requirements.txt
```

---

## 🚀 Usage

Open the notebooks in order to follow the pipeline:

```bash
jupyter notebook
```

Recommended order:

1. `Data Cleaning.ipynb`
2. `Data Preprocessing and Feature Selection.ipynb`
3. `EDA.ipynb`
4. `Clustering.ipynb`
5. `Final codes.ipynb`

---

## ✨ Features

- End-to-end machine learning pipeline
- Outlier detection and handling
- Feature engineering and encoding
- Model comparison across 10+ algorithms
- Hyperparameter tuning with GridSearchCV
- ROC, F1-score, precision, and recall metrics
- K-Means, Hierarchical, and DBSCAN clustering
- Visualizations including PCA and silhouette plots

---

## 🛠️ Technologies Used

- Python
- pandas, numpy
- scikit-learn
- matplotlib, seaborn
- xgboost, lightgbm
- Jupyter Notebook

---

## 🤝 Contributing

Contributions are welcome! If you'd like to collaborate:

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

---

## 👤 Contact

**Iman Fasasi**  
GitHub: [@ImanFasasi](https://github.com/ImanFasasi)  
Email: [imanbusayo@gmail.com]

---

## 🙏 Acknowledgements

- UCI ML Repository: Diabetes 130-US Hospitals Dataset
- Scikit-learn documentation
- Open-source community contributions on Kaggle and GitHub
```
