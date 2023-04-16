#!/usr/bin/env python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <MySQL username> <MySQL password> <database name>")
        exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)
        cursor = db.cursor()
        cursor.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print(f"MySQL Error [{e.errno}]: {e.msg}")
        exit(1)
