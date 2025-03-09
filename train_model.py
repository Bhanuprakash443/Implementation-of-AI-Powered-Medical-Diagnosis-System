import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

# Load dataset (Change file name as needed)
df = pd.read_excel("C:\Users\bhanu\Downloads\heart_disease_data.xlsx")  # Change to "diabetes_data.xlsx" if needed

# Split features and labels
X = df.drop(columns=["target"])  # Replace "target" with actual target column name
y = df["target"]

# Normalize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Build a simple Neural Network model
model = keras.Sequential([
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')  # For binary classification
])

# Compile model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train model
model.fit(X_train, y_train, epochs=20, batch_size=32, validation_data=(X_test, y_test))

# Save model
model.save("medical_model.h5")

# Save scaler
joblib.dump(scaler, "scaler.pkl")

print("Model and scaler saved successfully!")
