from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from app.apis.users import models, schemas, operations
from app.core.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

route = APIRouter(prefix="/users", tags=["Users"])


@route.get("/")
def get_all():
    return {"todo": "get_all_users"}


@route.post("/",)
def register(user_in: schemas.UserIn, db: Session = Depends(get_db)):
    return operations.register(user_in, db)