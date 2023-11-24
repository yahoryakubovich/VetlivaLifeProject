from sqlalchemy import Column, Integer, String, Text, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    problem = Column(Text)
    condition = Column(Text)
    experience = Column(Text)
    preferences = Column(Text)
    approach = Column(Text)
    format = Column(Text)
    price = Column(Text)
    young_specialist = Column(Text)
    additional_wishes = Column(Text)
    source = Column(Text)

DATABASE_URL = "sqlite:///./test.db"  # Пример URL для SQLite. Замените на свой URL.

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)