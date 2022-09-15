#!/usr/bin/python3

"""
Takes 3 arguments and lists all states in the database
"""
import sys
import MySQLdb


def main(argv):
"""Connects to a SQL database and lists all items in it"""
conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == '__main__':
    if len(sys.argv) == 4:
        main(sys.argv)
