Education Performance Analytics

# Author: Kersha Broussard
# Course: Capstone Project – Data Analytics
# Institution: Northwest Missouri State University

# 🎓 Education Performance Analytics
**Predicting Student Performance Using Attendance and Socioeconomic Factors**

## 📘 Project Overview
This project explores how academic, demographic, and socioeconomic factors influence student performance.  
Using regression-based modeling and exploratory data analysis (EDA), the study identifies key predictors of academic success — particularly attendance and socioeconomic conditions.

The workflow includes:
- Data acquisition from Kaggle  
- Cleaning and preprocessing  
- Exploratory Data Analysis (EDA)  
- Feature engineering  
- Predictive modeling (Linear Regression, Decision Tree Regressor)  
- Visualization and interpretation  

---

## 🧩 Project Structure
education-performance-analytics/
│
├── data/
│ ├── student_performance_socioeconomic.csv
│ ├── student_performance_socioeconomic_cleaned.csv
│
├── notebooks/
│ ├── 01_preprocessing.ipynb
│ ├── 02_eda.ipynb
│
├── visuals/
│ ├── histogram_all_features.png
│ ├── heatmap_correlations.png
│ ├── pairplot_academic_relationships.png
│ ├── feature_importance.png
│ ├── data_cleaning_workflow.png
│
├── scripts/
│ └── data_cleaning.py
│
├── requirements.txt
├── README.md
└── .gitignore


---

## ⚙️ Environment Setup

### Create and Activate Virtual Environment
### Install Dependencies
pip install -r requirements.txt

🧠 Data Source

Dataset Title: Student Performance and Socioeconomic Dataset

Source: Kaggle

Link: https://www.kaggle.com/datasets/zoya77/student-performance-and-socioeconomic-dataset

Observations: 504 (cleaned to 452)

Features: 25

Target Variable: Grade_Average

| Category          | Tools & Libraries         |
| ----------------- | ------------------------- |
| **Data Handling** | pandas, numpy             |
| **Visualization** | matplotlib, seaborn       |
| **Modeling**      | scikit-learn              |
| **Workflow**      | Jupyter Notebook, VS Code |
| **Documentation** | Overleaf (LaTeX)          |

### 📊 Results Summary

* Decision Tree Regressor achieved the best performance with R² = 0.72 and MAE = 2.85.

* Attendance rate, parental income, and semester average grade were the top predictors.

* EDA confirmed a strong positive correlation between attendance and academic outcomes.

### 🧾 References

Kaggle: Student Performance and Socioeconomic Dataset

Koutsampelas, C. & Tsakloglou, P. (2022). Socioeconomic inequality and educational outcomes: Education Economics, 30(4).


# Create virtual environment
python -m venv .venv

# Activate environment
.venv\Scripts\activate  # (Windows)
# OR
source .venv/bin/activate  # (macOS/Linux)

# 🔗 Useful Links

### 📊 Dataset: Kaggle Student Performance Dataset 

{https://www.kaggle.com/datasets/zoya77/student-performance-and-socioeconomic-dataset}{Student Performance and Socioeconomic Dataset (Kaggle)}

### 🧾 Overleaf Report: (h--)

### 💻 GitHub Repository: [(https://github.com/kersha0530/education-performance-analytics/tree/main)]


