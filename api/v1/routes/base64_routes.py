"""Base64 routes module"""
from fastapi import APIRouter, status
from api.v1.schemas.response_model import (
                            SuccessResponse,
                            ErrorResponse,
                            ErrorData)
from api.v1.schemas.base64_schemas import (
                            EncodeText,
                            DecodeText)
import base64


encode = APIRouter(prefix="/encode", tags=["encode"])
@encode.post("/",
            response_model=SuccessResponse,
            responses={
                        200: {
                            "model": SuccessResponse,
                            "description": "Encoding successfull"
                          },
                        500: {
                            "model": ErrorResponse,
                            "description": "Failed to encode text"
                          }
            })
def text_to_base64(request: EncodeText):
    """Converts text to base64 encoding"""
    try:
        # converts text to bytes
        bytes_data = request.text.encode()
        # perform encoding on bytes-like object
        encoded_data = base64.b64encode(bytes_data)
        
        success_response = SuccessResponse(
            status_code=status.HTTP_200_OK,
            message="Encoding successfull",
            data={
                "encoded_data": f"{encoded_data.decode()}"
            }
        )
        return success_response
    except Exception as e:
        error_response = ErrorResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Failed to encode text",
            data=ErrorData(
                str(e), type(e).__name
            )
        )
        return error_response



decode = APIRouter(prefix="/decode", tags=["decode"])

@decode.post("/",
            response_model=SuccessResponse,
            responses={
                        200: {
                            "model": SuccessResponse,
                            "description": "Decoding successfull"
                          },
                        500: {
                            "model": ErrorResponse,
                            "description": "Failed to decode text"
                          }
            })
def base64_to_text(request: DecodeText):
    """Converts base64 encoding to text"""
    try:
        # convert encoding to bytes
        bytes_data = request.base64_string.encode()

        # perform decoding on encoded bytes-like string
        decoded_data = base64.b64decode(bytes_data)

        success_response = SuccessResponse(
            status_code=status.HTTP_200_OK,
            message="Encoding successfull",
            data={
                "decoded_data": f"{decoded_data.decode()}"
            }
        )
        return success_response
    except Exception as e:
        error_response = ErrorResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Failed to decode text",
            data=ErrorData(
                str(e), type(e).__name
            )
        )
        return error_response