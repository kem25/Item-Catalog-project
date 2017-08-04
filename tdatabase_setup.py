import sys
from sqlalchemy import Column,ForeignKey,Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base=declarative_base()

class Country(Base):
    __tablename__='country'
    name=Column(String(80),nullable=False)
    id=Column(Integer, primary_key=True)


class VisitList(Base):
    __tablename__='visit_list'
    name=Column(String(80),nullable=False)
    id=Column(Integer,primary_key=True)
    country_id=Column(Integer,ForeignKey('country.id'))
    country=relationship(Country)
    description=Column(String(500))
    category=Column(String(40))
    besttime=Column(String(40))


engine=create_engine('sqlite:///catalog.db')

Base.metadata.create_all(engine)

