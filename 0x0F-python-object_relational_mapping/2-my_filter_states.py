#!/usr/bin/python3
"""
Takes 3 args and lists all states starting with a given string
"""
import sys
import MySQLdb

def main(argv):
    """connects to a DB and produces filterd list"""
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}%'\
                ORDER BY id ASC".format(argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    pass
    cur.close()
    conn.close()


if __name__ == '__main__':
    if len(sys.argv) == 5:
        main(sys.argv)
