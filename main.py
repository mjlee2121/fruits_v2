import uvicorn
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List#, Annotated
# import models
# from database import engine, SessionLocal
# from sqlalchemy.orm import Session

# app = FastAPI()
# models.Base.metadata.create_all(bind=engine)

# class PostBase(BaseModel):
#   title: str
#   content: str
#   user_id:int

# class UserBase(BaseModel):
#   username: str

# def get_db():
#   db = SessionLocal()
#   try:
#     yield db
#   finally:
#     db.close()

# db_dependency = Annotated(Session, Depends(get_db))

class Fruit(BaseModel):
    name: str


class Fruits(BaseModel):
    fruits: List[Fruit]


app = FastAPI(debug=True)

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
    # Add more origins here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Origins that are allowed
    allow_credentials=True,  # Allow cookies to be sent
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

memory_db = {"fruits": []}

@app.get("/", response_model=Fruits)
def get_fruits():
    print(memory_db)
    return Fruits(fruits=memory_db["fruits"])


@app.post("/")
def add_fruit(fruit: Fruit):
    memory_db["fruits"].append(fruit)
    return fruit

# @app.delete("/")
# def delete_fruit(fruit: Fruit):
#     print('delete called')
#     if fruit in memory_db["fruits"]:
#         print('fruit exists')
#         memory_db["fruits"].remove(fruit)

@app.delete("/")
def delete_fruit(fruit: Fruit):
    # Find the fruit in the memory_db
    for existing_fruit in memory_db["fruits"]:
        if existing_fruit.name == fruit.name:
            memory_db["fruits"].remove(existing_fruit)
            return {"message": f"Fruit '{fruit.name}' has been deleted successfully."}
    # Raise error if fruit not found
    raise HTTPException(status_code=404, detail=f"Fruit '{fruit.name}' not found.")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)