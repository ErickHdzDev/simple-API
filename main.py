from fastapi import FastAPI
import platform

app = FastAPI()

@app.get("/")
def hello():
    return {"body":f"Hello from {platform.node()}"}

@app.post("/echo")
def echo(body:dict):
    msg = body.get("msg", None)
    if not msg:
        return {"body":"msg is required"}
    
    return {"body":f"Message: {msg}"}