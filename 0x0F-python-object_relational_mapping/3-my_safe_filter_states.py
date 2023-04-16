#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor object to interact with the MySQL server
    cur = db.cursor()

    # Execute a safe SQL query using parameters
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (sys.argv[4],))

    # Fetch all the rows and print them
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connections
    cur.close()
    db.close()
