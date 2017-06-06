from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///data/nobel_prize.db', echo=True)

Session = session_maker(engine)

Base = declarative_base()

Base.meta.create_all()

class Winner(Base):
    __tablename__ = 'winners'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    year = Column(Integer)
    nationality = Column(String)
    sex = Column(Enum('male', 'female'))

    def __repr__(self):
        return "<Winner(name='%s', category='%s', year='%s')>" %(self.name, self.category, self.year)
