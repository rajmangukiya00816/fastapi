from fastapi import APIRouter, Depends, status, Response,HTTPException
from .. import schemas,models,oauth2
from ..databse import get_db
from typing import List
from sqlalchemy.orm import Session
from ..repository import blog


router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)


@router.post('',status_code=status.HTTP_201_CREATED)
def create(request : schemas.Blog , db: Session = Depends(get_db),current_user : schemas.User = Depends(oauth2.get_current_user)):
    # new_blog = models.Blog(title=request.title , body=request.body,user_id= 1)
    # db.add(new_blog)
    # db.commit()
    # db.refresh(new_blog)
    # return new_blog
    return blog.create(request, db)


@router.get('', response_model= List[schemas.showBlog])
def all(db : Session = Depends(get_db),current_user : schemas.User = Depends(oauth2.get_current_user)):
    # blogs = db.query(models.Blog).all()
    # return blogs
    return blog.get_all(db)

@router.get('/{id}',status_code=status.HTTP_200_OK, response_model=schemas.showBlog) 
def show(id : int, db : Session = Depends(get_db),current_user : schemas.User = Depends(oauth2.get_current_user)):
    # blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    # if not blogs:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'blog not avaiable for {id} id') 
    # return blogs
    return blog.get(id,db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id : int, db : Session = Depends(get_db),current_user : schemas.User = Depends(oauth2.get_current_user)):
    # blogs = db.query(models.Blog).filter(models.Blog.id == id)
    # if not blogs:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'no blog avaiable for {id} id')
    # blogs.delete(synchronize_session=False)
    # db.commit()
    # return "deleted"
    return blog.delete(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id:int,request : schemas.Blog , db : Session = Depends(get_db),current_user : schemas.User = Depends(oauth2.get_current_user)):
    # blogs = db.query(models.Blog).filter(models.Blog.id == id)
    # if not blogs.first():
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'no blog avaiable for {id} id')
    # blog_Data = dict(request)
    # blogs.update(blog_Data)
    # db.commit()
    # return "updated"
    return blog.update(id,request,db)