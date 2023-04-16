#!/usr/bin/python3
"""
Lists all cities of the database hbtn_0e_4_usa, ordered by city id.

Usage: ./4-cities_by_state.py <mysql username> <mysql password> <database name>
"""

import sys
import MySQLdb


if __name__ == "__main__":
    db_username, db_password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(user=db_username, passwd=db_password, db=db_name)
    cursor = db.cursor()

    cursor.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                     FROM `cities` as `c` \
                     INNER JOIN `states` as `s` \
                     ON `c`.`state_id` = `s`.`id` \
                     ORDER BY `c`.`id`")

    [print(city) for city in cursor.fetchall()]

    cursor.close()
    db.close()
