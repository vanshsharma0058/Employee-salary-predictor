#  Employee Salary Predictor

A machine learning web application built with **Flask** that predicts an employee's salary based on their years of experience using a **Linear Regression** model.

---

## 📌 Project Description

This project is a simple ML-based web app where the user enters their years of experience, and the model predicts their expected salary. It is trained on a sample dataset (`hiring.csv`) and saves the model using `pickle` for fast real-time predictions.

---

## 📁 Project Structure

Employee_salary_pred/
│
├── app.py # Main Flask app
├── train_model.py # Script to train Linear Regression model
├── model.pkl # Saved ML model (pickle format)
├── hiring.csv # Sample training dataset
├── requirements.txt # Python package dependencies
└── templates/
└── index.html # Frontend form (HTML + Jinja2)

---


---

## 🚀 How to Run the Project Locally

### 1. Clone the Repository


git clone https://github.com/vanshsharma0058/Employee-salary-predictor.git
cd Employee-salary-predictor

### 2. Install Dependencies

pip install -r requirements.txt

### 3. Run the Application

python app.py
Go to http://127.0.0.1:5000 in your browser to access the app.

---

### 🧠 Machine Learning Model
Algorithm Used: Linear Regression

Library: scikit-learn

Training Script: train_model.py

Model Output: model.pkl (used in app.py)

---

### 🛠️ Technologies Used
Frontend: HTML, Jinja2 (inside templates/)

Backend: Python with Flask

ML: scikit-learn, pandas

Deployment Ready: Yes (for platforms like Heroku, Render)

---

### 📬 Contact
Made by Vansh Sharma

📧 Email: vanshsharmagi288@gmail.com

🧑‍💻 GitHub: vanshsharma0058

---

### ✅ Future Improvements
Add multiple input features (e.g., education, location)

Add frontend validation and error handling

Deploy to cloud (Heroku / Render / Replit)
