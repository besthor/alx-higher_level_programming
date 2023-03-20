#!/usr/bin/python3
"""
python script that lists all states from the database hbtn_0e_0_usa with a
given name and is safe from MySQL injections
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # Connect to the database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         charset="utf8")

    # Create a cursor object to execute SQL queries
    cur = db.cursor()

    # Execute the SQL query to select all states with names starting with 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all the rows and print them in the desired format
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and database connections
    cur.close()
    db.close()
