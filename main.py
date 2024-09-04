from fastapi import FastAPI
import platform

app = FastAPI()

@app.get("/")
def echo():
    return {"body":f"Hello from {platform.node()}"}