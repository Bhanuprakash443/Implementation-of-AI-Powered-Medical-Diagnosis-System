# AI-Powered Medical Diagnosis System
An AI-based medical diagnosis system that predicts diseases like heart disease and diabetes using machine learning models.
## Features
 Predicts medical conditions based on user input  
 Uses a trained deep learning model for accuracy  
 FastAPI backend for real-time predictions  
 React.js frontend for user-friendly experience  
 Deployed on Render (Backend) and Vercel (Frontend)  
 Dockerized for easy deployment 
 ## Tech Stack
 Backend:FastAPI, TensorFlow, Scikit-Learn  
 Frontend:React.js, Axios  
 Deployment:Render, Vercel, Docker  
 Database (Optional):PostgreSQL / Firebase
 ## Installation Guide
### 🔹 Clone the repository

git clone https://github.com/yourusername/medical-diagnosis-system.git
cd medical-diagnosis-system

cd backend
pip install -r requirements.txt
python train_model.py  # Train the model
uvicorn app:app --reload  # Run the API
## Deployment
### 🔹 Deploy Backend (Render)
- Push backend code to GitHub
- Go to **Render.com**, create a new Web Service
- Connect repository and deploy

### 🔹 Deploy Frontend (Vercel)
- Push frontend code to GitHub
- Go to **Vercel.com**, import repo, and deploy
- 






