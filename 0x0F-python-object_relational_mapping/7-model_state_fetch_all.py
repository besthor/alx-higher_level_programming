#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa in ascending order by states.id
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        exit(1)

    # Create engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a session to communicate with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects and sort by states.id
    states = session.query(State).order_by(State.id).all()

    # Print the results in the format "[<state.id>:] <state.name>"
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()

