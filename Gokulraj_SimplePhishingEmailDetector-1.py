"""
Project: Simple Phishing Email Detector
Student: Gokulraj
Domain: Cyber Security

Educational demonstration only. This small example dataset is not suitable
for making real-world email security decisions.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Small sample dataset for demonstration
messages = [
    ("Urgent: verify your account now using this link", "phishing"),
    ("You won a prize. Send your password to claim it", "phishing"),
    ("Your account will close today. Click here immediately", "phishing"),
    ("Confirm your bank details to avoid suspension", "phishing"),
    ("Unusual login detected. Open this link to secure your account", "phishing"),
    ("You have been selected for a free gift. Claim now", "phishing"),
    ("Please provide your OTP to receive a refund", "phishing"),
    ("Download the attached invoice and enable macros", "phishing"),
    ("Your password expires today. Sign in through this link", "phishing"),
    ("Immediate action required to unlock your wallet", "phishing"),
    ("The class meeting starts at 10 AM tomorrow", "legitimate"),
    ("Your library book is due next Monday", "legitimate"),
    ("Please review the project report before submission", "legitimate"),
    ("The college timetable is available on the student portal", "legitimate"),
    ("Thank you for attending the training session", "legitimate"),
    ("Your appointment is confirmed for Friday afternoon", "legitimate"),
    ("The team meeting notes are attached for your review", "legitimate"),
    ("Your course registration has been completed", "legitimate"),
    ("Please submit your assignment by the due date", "legitimate"),
    ("The monthly newsletter is ready to read", "legitimate"),
]

df = pd.DataFrame(messages, columns=["message", "label"])
X_train, X_test, y_train, y_test = train_test_split(
    df["message"], df["label"], test_size=0.30, random_state=42, stratify=df["label"]
)

model = make_pipeline(
    TfidfVectorizer(),
    LogisticRegression(max_iter=1000)
)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print("Model training completed.")
print("Accuracy:", round(accuracy_score(y_test, predictions), 2))
print("\nClassification report:\n")
print(classification_report(y_test, predictions, zero_division=0))
print("Confusion matrix (rows = actual, columns = predicted):")
print(confusion_matrix(y_test, predictions, labels=["legitimate", "phishing"]))

# Try a sample message. Change this text to test another example.
new_message = "Urgent: your account is locked. Verify your password now"
prediction = model.predict([new_message])[0]
print("\nMessage:", new_message)
print("Prediction:", prediction.upper())
print("Note: This is a basic educational demo, not a final security verdict.")
