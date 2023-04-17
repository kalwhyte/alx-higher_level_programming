#!/usr/bin/python3
"""Lists the State object with the name passed as argument
from the database hbtn_0e_6_usa.
Usage: ./10-model_state_my_get.py <mysql username> /
                                  <mysql password> /
                                  <database name>
                                  <state name searched>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create a connection to the database.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create a configured "Session" class.
    Session = sessionmaker(bind=engine)

    # Create a Session object for our queries.
    session = Session()

    # Query the database for the state with the specified name.
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Print the state's ID or "Not found" if the state is not in the database.
    if state:
        print(state.id)
    else:
        print("Not found")
