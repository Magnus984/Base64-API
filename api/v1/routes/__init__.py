from fastapi import APIRouter
from .base64_routes import encode, decode

api_version_one = APIRouter(prefix=("/api/v1"))

api_version_one.include_router(encode)
api_version_one.include_router(decode)