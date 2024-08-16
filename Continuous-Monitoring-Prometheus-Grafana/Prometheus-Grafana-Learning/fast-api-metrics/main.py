from fastapi import FastAPI 
import os
from prometheus_fastapi_instrumentator import Instrumentator
import uvicorn

app = FastAPI() 
port = int(os.environ.get("PORT", 8005))


@app.get("/") # path operation decorator
async def root():
    return {"message":"Hello World from FASTAPI"}

@app.get("/demo") # path operation decorator
def demo_func():
    return {"message":"This is output from demo function"}

@app.post("/post_demo") # path operation decorator
def demo_post():
    return {"message":"This is output from post demo function"}

if __name__== "__main__":
    uvicorn.run("main:app", host="0.0.0.0",port=port,reload=False)

Instrumentator().instrument(app).expose(app)