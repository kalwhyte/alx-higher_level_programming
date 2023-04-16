#!/usr/bin/python3
"""Lists all states with a name starting with N (upper N)"""

import MySQLdb
import sys

if __name__ == '__main__':
    db_connection = MySQLdb.connect(
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]
    )
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM `states` ORDER BY `id`")
    states = cursor.fetchall()
    [print(state) for state in states if state[1][0] == "N"]
