# fastapi provide 2 type of documentation : 
# 1.swagger ui , 2.redoc

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/blog')
def index(limit = 10,published:bool = True, sort : Optional[str] = None):
    if published:
        return {'data' : f'{limit} published blogs from databse'}
    return {'data' : f'{limit} unpublished blogs from the db'}

@app.get('/about')
def about():
    return {'data' : 'about page'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data' : 'blog are unpublished'}

@app.get('/blog/{id}')
def show(id : int):
    # return {'data' : f'block of id is {id}'}
    return {'data' : id}

@app.get('/blog/{id}/comments')
def comments(id, limit =10):
    # return limit
    return {'data' : {'1','2'}}


class Blog(BaseModel):
    title : str
    body : str
    published : Optional[bool]

@app.post('/blog')
def create(request : Blog):
    return {'data' : f'blog is created as title is {request.title}'} 