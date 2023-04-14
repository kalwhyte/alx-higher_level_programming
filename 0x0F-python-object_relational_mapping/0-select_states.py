#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Open database connection
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    # execute SQL query using execute() method.
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    
    # Fetch all rows using fetchall() method.
    data = cursor.fetchall()
    
    # Print each row
    for row in data:
        print(row)
    
    # disconnect from server
    cursor.close()
    db.close()
