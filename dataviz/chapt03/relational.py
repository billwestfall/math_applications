from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Enum

engine = create_engine('sqlite:///data/nobel_prize.db', echo=True)

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
