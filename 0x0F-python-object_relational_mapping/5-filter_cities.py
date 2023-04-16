#!/usr/bin/python3
"""
Displays all cities of a given state from the states table of the database hbtn_0e_4_usa.
Safe from SQL injections.

Usage: ./5-filter_cities.py <mysql username> <mysql password> <database name> <state name searched>
"""

import sys
import MySQLdb


if __name__ == "__main__":
    db_username, db_password, db_name, state_name = sys.argv[1:5]

    db_connection = MySQLdb.connect(user=db_username, passwd=db_password, db=db_name)
    cursor = db_connection.cursor()

    cursor.execute("SELECT `c`.`name` \
                    FROM `cities` as `c` \
                    INNER JOIN `states` as `s` \
                    ON `c`.`state_id` = `s`.`id` \
                    WHERE `s`.`name` = %s \
                    ORDER BY `c`.`id`", (state_name,))

    cities = [ct[0] for ct in cursor.fetchall()]

    print(", ".join(cities))

    cursor.close()
    db_connection.close()
