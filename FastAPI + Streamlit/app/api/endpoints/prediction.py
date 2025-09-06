from fastapi import APIRouter, HTTPException
from models.schema import StartupStatusRequest, StartupStatusResponse
from services.preprocess_prediction import predict_process

router = APIRouter()

@router.post("/predict", response_model=StartupStatusResponse)
def predict(data: StartupStatusRequest):
    try:
        data_dict = data.dict()  # Convert to dict
        val = predict_process(data= data_dict)
        return {"predicted_status": val}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
