# Simple Phishing Email Detector

**Student:** Gokulraj  
**Program:** IBM SkillsBuild Cyber Security 2026  
**Project type:** Beginner-friendly Python / machine-learning demonstration

## Project description
This project trains a small text-classification model to label example messages as `phishing` or `legitimate`. It uses TF-IDF text features and Logistic Regression from scikit-learn.

## Files
- `Gokulraj_SimplePhishingEmailDetector.ipynb` — complete Jupyter Notebook source code.
- `requirements.txt` — Python dependencies.
- `Gokulraj_ProjectReport.docx` — project documentation.

## Technologies used
- Python 3
- Jupyter Notebook
- pandas
- scikit-learn
- TF-IDF text vectorization
- Logistic Regression

## Dataset
The notebook includes a small, manually written sample dataset, so no separate download is required. It is provided only for learning and demonstration. It is too small to support real-world security conclusions.

## Setup and run
1. Install Python 3.
2. Open a terminal in this folder.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start Jupyter:
   ```bash
   jupyter notebook
   ```
5. Open `Gokulraj_SimplePhishingEmailDetector.ipynb` and run the cells from top to bottom.

## Expected result
The notebook displays the sample data, trains a classifier, prints evaluation metrics, and predicts whether a user-entered example message resembles a phishing or legitimate message. Exact scores may vary with library versions.

## Limitations and safe use
- The dataset is very small and may not represent real phishing messages.
- A prediction can be wrong. Do not rely on this demo to decide whether a real email is safe.
- Never enter real passwords, OTPs, or private information.
- For a stronger project, use a larger labelled dataset from a reputable source, document its licence, and evaluate on a separate test set.

## Author
Gokulraj
