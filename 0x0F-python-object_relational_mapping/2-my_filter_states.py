#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host='localhost',
                         user=username,
                         passwd=password,
                         db=db_name,
                         port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
