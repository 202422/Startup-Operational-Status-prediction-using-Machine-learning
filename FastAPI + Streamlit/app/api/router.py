from fastapi import APIRouter
from app.api.endpoints import prediction

router = APIRouter()
router.include_router(prediction.router, prefix="/api", tags=["Prediction"])