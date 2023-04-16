#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db_user = sys.argv[1]
    db_pass = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(user=db_user,
                         passwd=db_pass,
                         db=db_name,
                         host="localhost",
                         port=3306)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC", (state_name,))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()

    db.close()
