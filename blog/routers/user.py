from fastapi import APIRouter,status,HTTPException,Depends
from .. import schemas,models
from ..databse import get_db
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..repository import user

router = APIRouter(
    prefix='/user',
    tags=['Users']
)

@router.post('',status_code=status.HTTP_201_CREATED, response_model= schemas.showUser)
def create(request : schemas.User , db : Session = Depends(get_db)):
    # new_user = models.User(name = request.name, email = request.email, password = Hash.bcrypt(request.password))
    # db.add(new_user)
    # db.commit()
    # db.refresh(new_user)
    # return new_user
    return user.create(request,db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.showUser)
def show(id:int, db:Session = Depends(get_db)):
    # user = db.query(models.User).filter(models.User.id == id).first()
    # if not user:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'user not avaiable for {id} id') 
    # return user
    return user.get(id,db)