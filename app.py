from fastapi import FastAPI
from schemas import AnalysisRequest
from analyzer import analyze

app = FastAPI()

@app.post("/analyze")
def analyze_code(req: AnalysisRequest):
    return analyze(req)
