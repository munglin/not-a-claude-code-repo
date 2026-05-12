from fastapi import FastAPI
from functions.add import add

app = FastAPI()


@app.post("/add")
def add_endpoint(a: int, b: int) -> dict:
    return {"sum": add(a, b)}
