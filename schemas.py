from pydantic import BaseModel

class Attempt(BaseModel):
    code: str
    success: bool

class AnalysisRequest(BaseModel):
    attempts: list[Attempt]
