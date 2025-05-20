from fastapi import FastAPI, File, UploadFile

from app.predict import predict_image
from app.schemas import PredictionResult
from app.telegram_bot import TelegramBot
from app.utils import read_imagefile

app = FastAPI()
bot = TelegramBot()

@app.post("/predict", response_model=PredictionResult)
async def predict(image: UploadFile = File(...)):
    image = read_imagefile(image)
    label, conf_score, viz_image = predict_image(image)
    bot.send_photo(viz_image, f'{label}: {conf_score}')
    return PredictionResult(label=label, conf_score=conf_score)
