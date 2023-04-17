#!/usr/bin/python3
"""Deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa.
Usage: ./13-model_state_delete_a.py <mysql username> /
                                    <mysql password> /
                                    <database name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == '__main__':
    # Create a connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and delete all State objects with a name containing 'a'
    for state in session.query(State).filter(State.name.like('%a%')):
        session.delete(state)

    # Commit the changes and close the session
    session.commit()
    session.close()
