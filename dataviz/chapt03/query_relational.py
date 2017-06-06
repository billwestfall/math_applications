

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///nobel_prize.db', echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Winner(Base):
    __tablename__ = 'winners'

    id = Column(Integer, primary_key=True)
    category = Column(String)
    name = Column(String)
    nationality = Column(String)
    sex = Column(Enum('male', 'female'))
    year = Column(Integer)

    def __repr__(self):
        return "<Winner(name='%s', category='%s', year='%s')>" %(self.name, self.category, self.year)

session.new
session.query(Winner).count()
