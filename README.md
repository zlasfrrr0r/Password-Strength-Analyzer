# 🔐 Password Strength Analyzer (with NumPy)

This is a mini-project to evaluate the strength of passwords using Python and NumPy.  
It scores passwords based on basic rules, classifies them as **Weak**, **Medium**, or **Strong**, and can process thousands at once — including real-world common passwords.

## 🚀 Features

- Analyze individual or bulk passwords from `.csv` files.
- Uses NumPy vectorization for fast evaluation.
- Detects uppercase, lowercase, digits, and minimum length.
- Returns verdicts for each password.

## 📂 Data

Includes a file: `data/common_passwords.csv` — a list of 10,000 common passwords, with their features too (Kaggle source).
