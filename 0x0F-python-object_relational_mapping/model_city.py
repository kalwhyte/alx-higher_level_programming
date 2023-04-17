#!/usr/bin/python3
"""Defines a City model.
Inherits from SQLAlchemy Base and links to the MySQL table cities.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

Base = declarative_base()


class City(Base):
    """Represents a city for a MySQL database.

    Attributes:
        id (str): The city's id.
        name (sqlalchemy.Integer): The city's name.
        state_id (sqlalchemy.String): The city's state id.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
