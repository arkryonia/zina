from fastapi import APIRouter

from app.apis.users import models
from app.core.database import engine

models.Base.metadata.create_all(bind=engine)

route = APIRouter(prefix="/users", tags=["Users"])

@route.get("/")
def get_all():
    return {"todo": "get_all_users"}