from fastapi import FastAPI
from exceptions import (
    PincodeNotFoundError,
    pincode_not_found_handler,
    InvalidPincodeError,
    invalid_pin_code_handler
)
from models import (
    PincodeRequest,
    LocationResponse,
    BulkRequest,
    BulkResponse
)
from data import pincode_db

app = FastAPI(
    title="Pincode Lookup API",
    description="Autofill city and state based on indian pincode during checkout"
)

## register custom exceptions
app.add_exception_handler(PincodeNotFoundError, pincode_not_found_handler)
app.add_exception_handler(InvalidPincodeError, invalid_pin_code_handler)

@app.get("/")
def root():
    return {"message": "Pincode Lookup API"}

@app.get("/pincode/{code}", response_model=LocationResponse)
def lookup_pincode(code: str):
    if len(code) != 6 or not code.isdigit():
        raise InvalidPincodeError(code, "Must be exactly 6 digits")
    if code not in pincode_db:
        raise PincodeNotFoundError(code)
    return pincode_db[code]

@app.post("/pincode/bulk", response_model=BulkResponse)
def pincode_bulk(request: BulkRequest):
    results = []
    missing = []

    for code in request.pincodes:
        if code in pincode_db:
            results.append(pincode_db[code])
        else:
            missing.append(code)

    return BulkResponse(
        found=len(results),
        not_found=len(missing),
        result=results,
        missing=missing
    )
