#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(
            host="localhost", port=3306,
            user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = conn.cursor()
    db_cursor.execute(
            "SELECT * FROM states WHERE name LIKE 'N%' \
                    ORDER BY id ASC")
    row_selected = db_cursor.fetchall()
    for row in row_selected:
        print(row)
