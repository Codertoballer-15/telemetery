from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Models for analysis (adjust as needed)
class Attempt(BaseModel):
    time: float
    code: str
    error: str
    success: bool

class AnalysisRequest(BaseModel):
    task_goal: str
    attempts: List[Attempt]

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/analyze")
def analyze_code(req: AnalysisRequest):
    # simple example analysis — replace with your logic
    total = len(req.attempts)
    progress_scores = []
    for i, a in enumerate(req.attempts):
        # simple scoring: success = 100, failure scales with attempt count
        progress = 100 if a.success else min(90, i * 20)
        progress_scores.append(progress)

    final = max(progress_scores) if progress_scores else 0
    return {
        "timeline": progress_scores,
        "final_score": final
    }
