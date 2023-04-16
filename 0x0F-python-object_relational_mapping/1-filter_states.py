#!/usr/bin/python3
"""Lists all states with a name starting with N (upper N)"""

import MySQLdb
import sys

if __name__ == '__main__':
    # Connection parameters
    db_user = sys.argv[1]
    db_passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to database
    db = MySQLdb.connect(user=db_user,
                         passwd=db_passwd,
                         db=db_name,
                         port=3306,
                         host='localhost')
    cursor = db.cursor()

    # Execute query
    cursor.execute("""SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC""")
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    # Close cursor and database
    cursor.close()
    db.close()
