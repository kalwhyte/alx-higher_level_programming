#!/usr/bin/python3
"""
Displays all values in the states table of the database hbtn_0e_0_usa
whose name matches that supplied as argument.
Usage: ./filter_states.py <mysql username>
                          <mysql password>
                          <database name>
                          <state name searched>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db_connection = MySQLdb.connect(
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]
    )
    cursor = db_connection.cursor()

    # Clear the states table
    cursor.execute("DELETE FROM `states`")

    # Insert some test data
    cursor.execute("INSERT INTO `states` (`name`) VALUES ('Arizona')")
    cursor.execute("INSERT INTO `states` (`name`) VALUES ('Texas')")
    cursor.execute("INSERT INTO `states` (`name`) VALUES ('California')")

    # Select and print matching states
    cursor.execute("SELECT * \
                     FROM `states` \
                     WHERE BINARY `name` = '{}'".format(sys.argv[4]))
    states = cursor.fetchall()
    [print(state) for state in states]
