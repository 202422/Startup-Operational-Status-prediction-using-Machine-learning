from fastapi import FastAPI
from api.router import router

app = FastAPI(
    title="Startup Status Prediction API",
    description="API to predict the operational status of startups (Operating, IPO, Acquired, Closed).",
    version="1.0.0"
)

app.include_router(router)

@app.get("/", tags=["Root"])
def root():
    return {"message": "Welcome to the Startup Prediction API 🚀"}