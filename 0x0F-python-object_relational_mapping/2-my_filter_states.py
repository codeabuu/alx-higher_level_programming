#!/usr/bin/python3
"""
This script takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb as db
from sys import argv

if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """
    conn = db.connect(host="localhost", port=3306,
                      user=argv[1], passwd=argv[2], db=argv[3])

    db_cursor = conn.cursor()
    db_cursor.execute(
            "SELECT * FROM states WHERE name = '{}' ORDER BY \
                    id ASC".format(argv[4]))
    sel_rows = db_cursor.fetchall()
    for row in sel_rows:
        print(row)
