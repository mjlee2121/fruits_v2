# from fastapi import FastAPI
# import uvicorn
# from fastapi.middleware.cors import CORSMiddleware

# from pydantic import BaseModel
# from typing import List

# class Fruit(BaseModel):
#   name: str

# class Fruits(BaseModel):
#   fruits: List[Fruit]

# app = FastAPI()

# origins = [
#   "http://localhost:3000"
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,  # Origins that are allowed
#     allow_credentials=True,  # Allow cookies to be sent
#     allow_methods=["*"],  # Allow all HTTP methods
#     allow_headers=["*"],  # Allow all headers
# )

# # in memory database
# memory_db = {"fruits":[]}


# @app.get('/fruits', response_model=Fruits)
# def get_fruits():
#   return Fruits(fruits=memory_db["fruits"])

# @app.post("/fruits", response_model=Fruits)
# def add_fruit(fruit: Fruit):
#   memory_db["fruits"].append(fruit)
#   return fruit

# if __name__=="__main__":
#   uvicorn.run(app, host="0.0.0.0", port=8000)

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List


class Fruit(BaseModel):
    name: str


class Fruits(BaseModel):
    fruits: List[Fruit]


app = FastAPI(debug=True)

origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000"
    # Add more origins here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

memory_db = {"fruits": []}

@app.get("/fruits", response_model=Fruits)
def get_fruits():
    return Fruits(fruits=memory_db["fruits"])


@app.post("/fruits")
def add_fruit(fruit: Fruit):
    memory_db["fruits"].append(fruit)
    return fruit


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)