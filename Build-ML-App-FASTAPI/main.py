from fastapi import FastAPI 

app = FastAPI() 
# my_first_api = FastAPI() 
# path
# POST, PUT, DELETE, GET
# @my_first_api.get("/")
@app.get("/") # path operation decorator
async def root():
    return {"message":"Hello World from FASTAPI"}

@app.get("/demo") # path operation decorator
def demo_func():
    return {"message":"This is output from demo function"}

@app.post("/post_demo") # path operation decorator
def demo_post():
    return {"message":"This is output from post demo function"}

# POST: to create data.
# GET: to read data.
# PUT: to update data.
# DELETE: to delete data.

# @app.post()
# @app.put()
# @app.delete()