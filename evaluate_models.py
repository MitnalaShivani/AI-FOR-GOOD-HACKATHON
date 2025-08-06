import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, roc_curve, auc
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from tensorflow.keras.models import load_model
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

def evaluate_models(file_path):
    df = pd.read_csv(file_path)

    # Preprocessing for both models
    for column in ["blood_type", "location"]:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])

    df_xgboost = df.drop(columns=["donor_id", "donation_date"])
    X_xgboost = df_xgboost.drop("is_available_next_month", axis=1)
    y_xgboost = df_xgboost["is_available_next_month"]

    X_train_xgboost, X_test_xgboost, y_train_xgboost, y_test_xgboost = train_test_split(X_xgboost, y_xgboost, test_size=0.2, random_state=42)

    # Load XGBoost model
    xgboost_model = joblib.load("blood_donation_system/models/xgboost_model.pkl")
    y_pred_xgboost = xgboost_model.predict(X_test_xgboost)
    y_proba_xgboost = xgboost_model.predict_proba(X_test_xgboost)[:, 1]

    print("\n--- XGBoost Model Evaluation ---")
    print(f"Accuracy: {accuracy_score(y_test_xgboost, y_pred_xgboost):.4f}")
    print("Classification Report:\n", classification_report(y_test_xgboost, y_pred_xgboost))

    # Preprocessing for LSTM
    df_lstm = df.drop(columns=["donor_id", "donation_date"])
    X_lstm = df_lstm.drop("is_available_next_month", axis=1)
    y_lstm = df_lstm["is_available_next_month"]

    scaler = joblib.load("blood_donation_system/models/scaler.pkl")
    X_lstm_scaled = scaler.transform(X_lstm)
    X_lstm_reshaped = X_lstm_scaled.reshape(X_lstm_scaled.shape[0], 1, X_lstm_scaled.shape[1])

    X_train_lstm, X_test_lstm, y_train_lstm, y_test_lstm = train_test_split(X_lstm_reshaped, y_lstm, test_size=0.2, random_state=42)

    # Load LSTM model
    lstm_model = load_model("blood_donation_system/models/lstm_model.h5")
    y_pred_proba_lstm = lstm_model.predict(X_test_lstm)
    y_pred_lstm = (y_pred_proba_lstm > 0.5).astype(int)

    print("\n--- LSTM Model Evaluation ---")
    print(f"Accuracy: {accuracy_score(y_test_lstm, y_pred_lstm):.4f}")
    print("Classification Report:\n", classification_report(y_test_lstm, y_pred_lstm))

    # ROC Curve
    fpr_xgboost, tpr_xgboost, _ = roc_curve(y_test_xgboost, y_proba_xgboost)
    roc_auc_xgboost = auc(fpr_xgboost, tpr_xgboost)

    fpr_lstm, tpr_lstm, _ = roc_curve(y_test_lstm, y_pred_proba_lstm)
    roc_auc_lstm = auc(fpr_lstm, tpr_lstm)

    plt.figure(figsize=(10, 8))
    plt.plot(fpr_xgboost, tpr_xgboost, color='darkorange', lw=2, label='XGBoost (AUC = %0.2f)' % roc_auc_xgboost)
    plt.plot(fpr_lstm, tpr_lstm, color='green', lw=2, label='LSTM (AUC = %0.2f)' % roc_auc_lstm)
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend(loc='lower right')
    plt.savefig('blood_donation_system/docs/roc_curve_comparison.png')
    plt.close()

    print("\n--- Model Comparison ---")
    print(f"XGBoost AUC: {roc_auc_xgboost:.4f}")
    print(f"LSTM AUC: {roc_auc_lstm:.4f}")

if __name__ == '__main__':
    evaluate_models('blood_donation_system/data/synthetic_blood_data.csv')

