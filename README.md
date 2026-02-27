# Smart School IT Helpdesk Analyzer

## Overview

This project simulates a real-world school IT Helpdesk system and demonstrates how data analysis and machine learning can improve ICT support operations.

It combines IT support concepts with data science techniques using Python.

---

## Objectives

- Analyse common IT issues across school departments
- Measure resolution time patterns
- Identify department-level ticket trends
- Predict ticket priority using machine learning

---

## Technologies Used

- Python
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- joblib
- Git & GitHub

---

## Dataset

The dataset contains 250 simulated IT helpdesk tickets with:

- Department
- Device Type
- Issue Type
- Resolution Time (minutes)
- Ticket Priority (High, Medium, Low)

File location:
data/raw/helpdesk_tickets.csv

---

## Exploratory Data Analysis

The project identifies:

- Most frequent IT issues
- Average resolution time
- Resolution time differences by priority
- Issue distribution by department

Charts are saved in:
reports/figures/

---

## Machine Learning Model

Model: Logistic Regression  
Preprocessing: OneHotEncoder + Pipeline  
Evaluation: Accuracy, Confusion Matrix  

Saved model:
models/priority_model.pkl

---

## How to Run

Generate dataset:
python src/generate_data.py

Run EDA:
python src/eda.py

Train model:
python src/train_model.py

Predict priority:
python src/predict_priority.py

---

## Skills Demonstrated

- Data analysis and visualisation
- Machine learning pipeline creation
- Feature encoding
- Model saving and reuse
- Professional project structure
- Version control with Git