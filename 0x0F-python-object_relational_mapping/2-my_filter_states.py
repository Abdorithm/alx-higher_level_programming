#!/usr/bin/python3
"""lists all states from the database with IDs in ascending order"""

import MySQLdb
import sys

if __name__ == "__main__":
    userName = sys.argv[1]
    passwd = sys.argv[2]
    table = sys.argv[3]
    state = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306, user=userName,
                           passwd=passwd, db=table, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(state))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
