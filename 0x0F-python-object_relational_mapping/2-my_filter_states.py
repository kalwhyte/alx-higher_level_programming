#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    db_connection = MySQLdb.connect(user=sys.argv[1], 
                                    passwd=sys.argv[2],
                                    db=sys.argv[3])
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM `states` WHERE BINARY `name` = %s", (sys.argv[4],))
    [print(state) for state in cursor.fetchall()]
