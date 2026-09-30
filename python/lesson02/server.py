# Import fastapi module
from fastapi import FastAPI

# Create an instance of FastAPI and provide a title for the API as well as version
app = FastAPI(title="Lesson 02 - First FastAPI application", description="A simple API using FastAPI and uvicorn", version="0.1.0")

# configure the routes and there logic for the API
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def sayHello(name: str):
    return {"message": f"Hellow {name}!"}

@app.get("/calculate")
def calculate(x: float, y: float):
    return {
        "x": x,
        "y": y,
        f"sum of {x} and {y} is": x + y,
    }

#  No need to configure ports, uvicorn will handle that. uvicorn will be ran using cmd cmd : uvicorn server:app --reload --port 3000