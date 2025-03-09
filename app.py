from fastapi import FastAPI
import numpy as np
import tensorflow as tf
import joblib
from pydantic import BaseModel

# Load trained model and scaler
model = tf.keras.models.load_model("medical_model.h5")
scaler = joblib.load("scaler.pkl")

app = FastAPI()

# Define input schema
class InputData(BaseModel):
    features: list

@app.post("/predict")
def predict(data: InputData):
    try:
        features = np.array(data.features).reshape(1, -1)
        scaled_features = scaler.transform(features)
        prediction = model.predict(scaled_features)[0][0]
        diagnosis = "Positive" if prediction > 0.5 else "Negative"
        return {"prediction": diagnosis, "confidence": float(prediction)}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
