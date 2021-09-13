from app.core.database import Base
from sqlalchemy import Column, String, Boolean


class User(Base):
    first_name = Column(String(30), nullable=True)    
    last_name = Column(String(60), nullable=True)  
    email = Column(String(50), unique=True)
    hashed_password = Column(String(128))
    is_active = Column(Boolean, default=True)
    address = Column(String(128), nullable=True)
    telephone = Column(String(8), nullable=True)
