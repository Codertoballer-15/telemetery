from fastapi import FastAPI
from app import analyze_code  # import your function from app.py

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/analyze")
def analyze(request_data: dict):
    return analyze_code(request_data)
