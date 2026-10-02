from fastapi.responses import JSONResponse
from fastapi import Request

class PincodeNotFoundError(Exception):
    def __init__(self, pincode: str):
        self.pincode = pincode

class InvalidPincodeError(Exception):
    def __init__(self, pincode:str, reason: str = "Invalid format"):
        self.pincode = pincode
        self.reason = reason

## custom handlers
async def pincode_not_found_handler(request: Request, exc: PincodeNotFoundError):
    return JSONResponse(
        status_code=404,
        content={
            "error": "pin code not found",
            "message": f"No location can be found for this pincode: {exc.pincode}",
            "pincode": exc.pincode
        }
    )

async def invalid_pin_code_handler(request: Request, exc: InvalidPincodeError):
    return JSONResponse(
        status_code=400,
        content={
            "error": "invalid pin code",
            "reason": f"Format is wrong: {exc.reason}"
        }
    )
