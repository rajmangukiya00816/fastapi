from sqlalchemy.orm import Session
from .. import models,schemas
from fastapi import status,HTTPException

def create(request :  schemas.Blog, db:Session):
    new_blog = models.Blog(title=request.title , body=request.body,user_id= 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def get(id:int,db:Session):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'blog not avaiable for {id} id') 
    return blogs

def delete(id:int, db:Session):
    blogs = db.query(models.Blog).filter(models.Blog.id == id)
    if not blogs.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'no blog avaiable for {id} id')
    blogs.delete(synchronize_session=False)
    db.commit()
    return "deleted"

def update(id:int,request : schemas.Blog , db : Session):
    blogs = db.query(models.Blog).filter(models.Blog.id == id)
    if not blogs.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'no blog avaiable for {id} id')
    blog_Data = dict(request)
    blogs.update(blog_Data)
    db.commit()
    return "updated"