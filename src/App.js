import React, { useState } from "react";
import axios from "axios";

function App() {
  const [features, setFeatures] = useState("");
  const [result, setResult] = useState(null);

  const handlePrediction = async () => {
    try {
      const response = await axios.post("http://localhost:8000/predict", {
        features: features.split(",").map(Number),
      });
      setResult(response.data);
    } catch (error) {
      console.error("Error:", error);
      setResult({ error: "Prediction failed!" });
    }
  };

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <h1>AI-Powered Medical Diagnosis</h1>
      <input
        type="text"
        placeholder="Enter features (comma-separated)"
        value={features}
        onChange={(e) => setFeatures(e.target.value)}
      />
      <button onClick={handlePrediction}>Predict</button>
      {result && (
        <div>
          <h2>Diagnosis: {result.prediction}</h2>
          <p>Confidence: {result.confidence}</p>
        </div>
      )}
    </div>
  );
}

export default App;
