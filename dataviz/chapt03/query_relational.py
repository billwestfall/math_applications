

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///nobel_prize.db', echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

session.new
session.query(Winner).count()
