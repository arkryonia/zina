from app.apis.users import models
from passlib.hash import bcrypt

def register(user_in, db):
    # new_user = user_in.dict()
    new_user = models.User(**user_in.dict())
    new_user.password=bcrypt.hash(new_user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"user": new_user}
