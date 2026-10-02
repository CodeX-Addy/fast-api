from fastapi import FastAPI

app = FastAPI(
    title="Pincode Lookup API",
    description="Autofill city and state based on indian pincode during checkout"
)

@app.get("/")
def root():
    return {"message": "Pincode Lookup API"}
