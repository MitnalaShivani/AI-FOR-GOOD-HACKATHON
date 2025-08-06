import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping
import joblib

def train_lstm_model(file_path):
    df = pd.read_csv(file_path)

    # Preprocessing
    # Convert categorical features to numerical using Label Encoding
    for column in ["blood_type", "location"]:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])

    # Drop donor_id and donation_date for now, as LSTM expects numerical sequences
    # For a more robust LSTM, we would need to create sequences per donor_id
    df = df.drop(columns=["donor_id", "donation_date"])

    X = df.drop("is_available_next_month", axis=1)
    y = df["is_available_next_month"]

    # Scale numerical features
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    # Reshape data for LSTM (samples, timesteps, features)
    # Assuming each sample is a single timestep for simplicity. For true time series, we'd need to group by donor and create sequences.
    X_reshaped = X_scaled.reshape(X_scaled.shape[0], 1, X_scaled.shape[1])

    X_train, X_test, y_train, y_test = train_test_split(X_reshaped, y, test_size=0.2, random_state=42)

    # Build LSTM model
    model = Sequential()
    model.add(LSTM(units=50, activation='relu', input_shape=(X_train.shape[1], X_train.shape[2])))
    model.add(Dropout(0.2))
    model.add(Dense(units=1, activation='sigmoid'))

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    # Early stopping to prevent overfitting
    early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

    history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.1, callbacks=[early_stopping], verbose=0)

    # Evaluate the model
    y_pred_proba = model.predict(X_test)
    y_pred = (y_pred_proba > 0.5).astype(int)

    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    print(f"LSTM Model Accuracy: {accuracy:.4f}")
    print("LSTM Classification Report:\n", report)

    # Save the model and scaler
    model.save('blood_donation_system/models/lstm_model.h5')
    joblib.dump(scaler, 'blood_donation_system/models/scaler.pkl')
    print('LSTM model saved to blood_donation_system/models/lstm_model.h5')
    print('Scaler saved to blood_donation_system/models/scaler.pkl')

if __name__ == '__main__':
    train_lstm_model('blood_donation_system/data/synthetic_blood_data.csv')


