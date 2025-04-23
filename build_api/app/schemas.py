from pydantic import BaseModel


class PredictionResult(BaseModel):
    label: str
    conf_score: float
