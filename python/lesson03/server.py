from fastapi import FastAPI
# For model definitions
from pydantic import BaseModel

# MODEL
# Defne the data model for the request body
class Project(BaseModel):
    _id: int
    name: str
    due_date: str
    status: str

# Mock some data
projects_list = [
    Project(_id=1, name="LAB01 GitHub Setup", due_date="2023-06-30", status="Completed"),
    Project(_id=2, name="LAB02 Contact Manager API", due_date="2023-07-15", status="In Progress"),
    Project(_id=3, name="Assignment 01", due_date="2023-08-01", status="Not Started")
]

# Declare the app object
# Add metadata to the FastAPI app, including title, description, and version to document with OpenAPI/Swagger
# Swagger UI will be available at http://localhost:3000/docs and ReDoc at http://localhost:3000/redoc
app = FastAPI(title="Project Management API", description="Demo API for managing projects", version="1.0.0")


# CONTROLLER
# Create a GET endpoint to retrieve all items
# Rpite is defined using @app.get decorator, which specifies the HTTP method and the path (/api/projects)
@app.get("/api/projects", response_model=list[Project], description="Retrieve all projects", summary="Get all projects")
# functionality is degined as a python function that returns the list of projects
def list_projects() -> list[Project]:
    # here would be bussiness logic, like database acces, processing, filter, pagination, sorting, etc.
    # for now just return the list we have.
    # VIEW fastapi will handle the serialization of the list of project objects to JJSON and return it as the response body
    return projects_list
