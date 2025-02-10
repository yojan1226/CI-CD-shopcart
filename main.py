from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI() #crate an instance of fastapi

#the app instance is the main component of our fastapi application.it is used to configure the application
class Custom(BaseModel):
    name: str
    age: int

@app.get("/ping")
async def root():
    return{"message":"hello world!!!!"}

#the @app.get() decorator is used to define an endpoint
@app.get("/")
async def root():
    return{"message":"welcome"}

@app.get("/blogs/comments")
async def read_blog_comments():
    return {"comments":"no comments yet!"}

@app.post("/blogs/{blog_id}")
async def read_blog(blog_id:int, request_body:Custom,q:str = None, name:str = ''):
    print(request_body)
    print(q)
    return{"blog_id":blog_id}

