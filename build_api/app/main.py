from fastapi import FastAPI, File, UploadFile

from app.predict import predict_image
from app.schemas import PredictionResult
from app.utils import read_imagefile

app = FastAPI()

@app.post("/predict", response_model=PredictionResult)
async def predict(image: UploadFile = File(...)):
    image = read_imagefile(image)
    label, conf_score = predict_image(image)
    return PredictionResult(label=label, conf_score=conf_score)
