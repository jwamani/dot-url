from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from typing import Any

def _error_envelop(*, code: str, message: str, details: Any|None = None) -> dict[str, Any]:
    """Wraps the error response in a consistent format."""
    payload = {
        "error": {
            "code": code,
            "message": message,
        }
    }
    if details is not None:
        payload["error"]["details"] = details
    return payload

def register_exception_handlers(app: FastAPI):
    
    
    
    
    
    
    @app.exception_handler(Exception)
    async def generic_exception_handler(request: Request, exc: Exception) -> JSONResponse:
        """Handles all uncaught exceptions"""
        details = str(exc)
        return JSONResponse(
            status_code=500,
            content=_error_envelop(
                code="internal_server_error",
                message="An unexpected error occurred.",
                details=details
            )
        )
        