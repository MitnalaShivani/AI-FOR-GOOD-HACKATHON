import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
import joblib

def train_xgboost_model(file_path):
    df = pd.read_csv(file_path)

    # Preprocessing
    # Convert categorical features to numerical using Label Encoding
    for column in ["blood_type", "location"]:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])

    # Drop donor_id and donation_date as they are not directly used in prediction for this model
    df = df.drop(columns=["donor_id", "donation_date"])

    X = df.drop("is_available_next_month", axis=1)
    y = df["is_available_next_month"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train XGBoost Classifier
    model = xgb.XGBClassifier(objective='binary:logistic', eval_metric='logloss', use_label_encoder=False, random_state=42)
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    print(f"XGBoost Model Accuracy: {accuracy:.4f}")
    print("XGBoost Classification Report:\n", report)

    # Save the model
    joblib.dump(model, 'blood_donation_system/models/xgboost_model.pkl')
    print('XGBoost model saved to blood_donation_system/models/xgboost_model.pkl')

if __name__ == '__main__':
    train_xgboost_model('blood_donation_system/data/synthetic_blood_data.csv')


