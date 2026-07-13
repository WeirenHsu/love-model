from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.model import MODEL_VERSION, predict

app = FastAPI(title="Love Model API")


class PredictRequest(BaseModel):
    text: str = Field(min_length=1, max_length=500)


class PredictResponse(BaseModel):
    prediction: str
    model_version: str


@app.get("/health")
def health():
    """Health check endpoint"""
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict_endpoint(request: PredictRequest):
    """Predict endpoint"""
    prediction = predict(request.text)
    return PredictResponse(
        prediction=prediction,
        model_version=MODEL_VERSION,
    )
