#!/usr/bin/python3
"""Lists all City objects from the database hbtn_0e_14_usa.
Usage: ./14-model_city_fetch_by_state.py <mysql username> /
                                         <mysql password> /
                                         <database name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    # Set up connection to the database
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine(f'mysql+mysqldb://{user}:{password}@localhost/{db_name}')
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()

    # Query the database and print results
    query = session.query(City, State).filter(City.state_id == State.id).order_by(City.id)
    for city, state in query.all():
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
