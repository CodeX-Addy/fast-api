from fastapi import FastAPI
import uvicorn

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
