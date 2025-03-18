"""Entry point for application"""
from fastapi import FastAPI, status
import uvicorn
from api.v1.schemas.response_model import (
                                SuccessResponse,
                                StandardResponse
                                )
from api.v1.routes import api_version_one   

app = FastAPI()

app.include_router(api_version_one)

@app.get("/",
         tags=["Home"],
         response_model=StandardResponse,
         responses={
             200: {
                 "model": StandardResponse,
                 "description": "Welcome response"
             }
         })
async def get_root() -> dict:
    """
    Root endpoint for the API
    
    Returns:
        Standardized success response with welcome message
    """
    success_response = SuccessResponse(
        status_code=status.HTTP_200_OK,
        message="Welcome to Base64-API",
        data={}
    )
    return success_response


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=7001,
        reload=True
    )