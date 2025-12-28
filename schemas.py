from pydantic import BaseModel
from typing import List

class Attempt(BaseModel):
    time: float
    code: str
    error: str
    success: bool

class AnalysisRequest(BaseModel):
    task_goal: str
    attempts: List[Attempt]
