<<<<<<< HEAD
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
=======
# Import fastapi library
from fastapi import FastAPI
# Create an app object using FastAPI, provide a title for the API
app = FastAPI(title="Example API with FastAPI and Uvicorn", description="This is an example API built using FastAPI and Uvicorn.", version="1.0.0")
# Configure app with handlers for different routes, and define the logic for each route
@app.get("/") # root
def hello_world():
    return { "message": "Bonjour le monde!" }

@app.get("/hello/{name}") # dynamic route
def hello_name(name: str):
    # string interpolation > use f-string and curly brackets to insert the value 
    return { "message": f"Bonjour {name}!" }

@app.get("/calculate") # passing query parameters
def calculate(x: int, y: int): # param validation is done by FastAPI based on the type declarations
    # examples: 
    # http://127.0.0.1:3000/calculate?x=10&y=xyz > validation error
    # http://127.0.0.1:3000/calculate?x=10&y=5 > correct response
    return { "result": f"The sum of {x} and {y} is {x + y}"}

# No need to configure ports or listening, uvicorn will handle that
>>>>>>> dcc6708aa03e8b2d8350bd0410287f6c92eb39cf
