from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector
from mysql.connector import Error
from fastapi.middleware.cors import CORSMiddleware

## Creating fastapi app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],  
)

## MySQL Database connection details
DB_HOST = "127.0.0.1"
DB_USER = "root"
DB_PASSWORD = "aditya"
DB_NAME = "FastAPI"

class QueryRequest(BaseModel):
    query:str

def execute_query(query: str):
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = connection.cursor()
        cursor.execute(query)
        if query.lower().startswith("select"):
            result = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            return {"columns": columns, "rows": result}
        else:
            connection.commit()
            return {"message": "Query executed...."}
    except Error as e:
        return {"error": str(e)}
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

##End point for the query
@app.post("/run_query/")
async def run_query(request: QueryRequest):
    response = execute_query(request.query)
    if "error" in response:
        raise HTTPException(status_code=400, detail=response["error"])
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)