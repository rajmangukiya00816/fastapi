# fastapi has 2 type of class:
# 1. pydantic model --> known as schemas(BaseModel)
# 2. sqlalchemy model --> known as models

from fastapi import FastAPI
from . import models
from .databse import engine
from .routers import blog,user,authentication

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
    

# @app.post('/blog',status_code=status.HTTP_201_CREATED, tags=['blogs'])
# def create(request : schemas.Blog , db: Session = Depends(get_db)):
#     new_blog = models.Blog(title=request.title , body=request.body,user_id= 1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog


# @app.get('/blog', response_model= List[schemas.showBlog], tags=['blogs'])
# def all(db : Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs


# @app.get('/blog/{id}',status_code=status.HTTP_200_OK, response_model=schemas.showBlog, tags=['blogs']) 
# def show(id : int,response : Response, db : Session = Depends(get_db)):
#     blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blogs:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'blog not avaiable for {id} id') 
#     return blogs


# @app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['blogs'])
# def delete(id : int, db : Session = Depends(get_db)):
#     blogs = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blogs:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'no blog avaiable for {id} id')
#     blogs.delete(synchronize_session=False)
#     db.commit()
#     return "deleted"


# @app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED,tags=['blogs'])
# def update(id:int,request : schemas.Blog , db : Session = Depends(get_db)):
#     blogs = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blogs.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'no blog avaiable for {id} id')
#     blog_Data = dict(request)
#     blogs.update(blog_Data)
#     db.commit()
#     return "updated"


# @app.post('/user',status_code=status.HTTP_201_CREATED, response_model= schemas.showUser, tags=['users'])
# def create(request : schemas.User , db : Session = Depends(get_db)):
#     new_user = models.User(name = request.name, email = request.email, password = Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user


# @app.get('/user/{id}', status_code=status.HTTP_200_OK, response_model=schemas.showUser, tags=['users'])
# def show(id:int, db:Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'user not avaiable for {id} id') 
#     return user