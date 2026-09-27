from fastapi import FastAPI
import uvicorn
from fastapi import Request

app = FastAPI(
    title="Swiggy Order Service",
    description=(
        "Simple swiggy service"
    ),
    version="1.2.1",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

@app.get("/")
def read_root():
    """Root endpoint - Health Check"""
    ## Fastapi converts dict into json directly
    return {"message": "Welcome to order service", "status": "healthy"}

@app.get("/about")
def about_service():
    """Returns API Metadata"""
    return {
        "service": "order-service",
        "region": "ap-south-1",
        "version": "1.2.1"
    }

@app.get("/debug/request")
async def debug_request(request: Request):
    """Debugging the request parameters"""
    return {
        "method": request.method,
        "request_url": str(request.url),
        "request_headers": dict(request.headers),
        "path_params": dict(request.path_params),
        "query_params": dict(request.query_params),
    }

@app.get("/orders/active",
    summary="Get Active Orders",
    description="Returns all the orders which are currently being prepared",
    tags=["orders"],
    response_description="List all the active orders",
    deprecated=False,
)
def active_orders():
    """This docstring will also appears in docs"""
    return {
        "active_orders": [
            {"id": 1, "item": "HotDog", "status": "out_for_delivery"}
        ]
    }
