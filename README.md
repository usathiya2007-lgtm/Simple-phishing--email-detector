# Simple Phishing Email Detector

**Author:** Gokulraj  
**Domain:** Cyber Security  
**Project type:** Beginner-friendly Python machine-learning demonstration

## Overview
This project demonstrates how sample text messages can be classified as `phishing` or `legitimate` using TF-IDF text features and Logistic Regression.

## Files
- `Gokulraj_SimplePhishingEmailDetector.py` — standalone Python code.
- `Gokulraj_SimplePhishingEmailDetector.ipynb` — Jupyter Notebook version.
- `requirements.txt` — required Python libraries.
- `Gokulraj_ProjectReport.docx` — project report in Word format.
- `Gokulraj_ProjectReport.pdf` — PDF version of the report.

## Technologies
- Python 3
- pandas
- scikit-learn
- Jupyter Notebook
- TF-IDF Vectorizer
- Logistic Regression

## Dataset
The project uses a small sample dataset included in the code. No separate dataset download is required.

## Setup and Run
1. Install Python 3.
2. Open a terminal in this folder.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Python file:
   ```bash
   python Gokulraj_SimplePhishingEmailDetector.py
   ```
   Or open the `.ipynb` file in Jupyter Notebook and run cells in order.

## Expected Output
The program trains a simple classifier, prints evaluation metrics, and predicts a label for one sample message.

## Limitations and Safe Use
This is a classroom demonstration with a very small dataset. It can misclassify messages and must not be used as the only basis for deciding whether a real email is safe. Never enter real passwords or OTPs.

## GitHub Repository
To publish this project, create a new repository on GitHub (for example, `simple-phishing-email-detector`), then upload these project files or use Git:
```bash
git init
git add .
git commit -m "Add simple phishing email detector project"
git branch -M main
git remote add origin https://github.com/YOUR-GITHUB-USERNAME/simple-phishing-email-detector.git
git push -u origin main
```
Replace `YOUR-GITHUB-USERNAME` with your actual GitHub username.
