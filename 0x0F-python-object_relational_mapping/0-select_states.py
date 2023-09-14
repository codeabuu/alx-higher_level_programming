#!/usr/bin/python3
"""
Script to list all states from the dbase hbtn_0e_0_USA
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """
    conn = MySQLdb.connect(
            host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])
    db_cursor = conn.cursor()
    db_cursor.execute("SELECT*FROM states")

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
