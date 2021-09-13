from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declared_attr

from app.core.config import settings


engine = create_engine(settings.get_db_uri())
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()