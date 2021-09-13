from app.core.database import Base
from sqlalchemy import Column, String, Boolean, DateTime


class User(Base):
    first_name = Column(String(30), nullable=True)
    last_name = Column(String(60), nullable=True)

    email = Column(String(50), unique=True)
    password = Column(String(128))
    telephone = Column(String(8))

    birth_date = Column(DateTime, nullable=True)
    address = Column(String(128), nullable=True)

    is_active = Column(Boolean, default=True)
