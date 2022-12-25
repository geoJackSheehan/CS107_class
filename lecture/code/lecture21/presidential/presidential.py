#!/usr/bin/env python3
# vim: foldmethod=marker
# File       : presidential.py
# Description: SQLite database class demo for presidential candidates in 2008
# Copyright 2022 Harvard University. All Rights Reserved.
import sqlite3


# main() {{{1
def main():
    # create a connection to the database {{{2
    # https://www.python.org/dev/peps/pep-0249/#connection-objects
    db = sqlite3.connect('presidential.sqlite')

    # obtain a cursor object for the `db` database {{{2
    # https://www.python.org/dev/peps/pep-0249/#cursor-objects
    cursor = db.cursor()

    # drop existing tables to start fresh for the purpose of this demo
    cursor.execute('DROP TABLE IF EXISTS candidates')
    cursor.execute('DROP TABLE IF EXISTS contributors')

    # turn on FOREIGN KEY support in SQLite (off by default).  If
    # foreign_keys=1, a sqlite3.IntegrityError will be raised if a FOREIGN KEY
    # constraint fails.
    cursor.execute('PRAGMA foreign_keys=1')

    # create a table for the `candidates` {{{2
    cursor.execute(
        '''CREATE TABLE candidates (
    id INTEGER PRIMARY KEY NOT NULL,
    first_name TEXT,
    last_name TEXT,
    middle_initial TEXT,
    party TEXT NOT NULL)'''
    )
    db.commit()  # commit the changes to the database

    # insert rows {{{2
    cursor.execute(
        '''INSERT INTO candidates
    (id, first_name, last_name, middle_initial, party)
    VALUES (?, ?, ?, ?, ?)''', (16, 'Mike', 'Huckabee', '', 'R')
    )

    cursor.execute(
        '''INSERT INTO candidates
            (id, first_name, last_name, middle_initial, party)
            VALUES (?, ?, ?, ?, ?)''', (32, 'Ron', 'Paul', '', 'R')
    )

    cursor.execute(
        '''INSERT INTO candidates
            (id, first_name, last_name, middle_initial, party)
            VALUES (?, ?, ?, ?, ?)''', (20, 'Barack', 'Obama', '', 'D')
    )

    db.commit()  # commit the changes to the database

    # queries {{{2
    # getting all columns returned in rows {{{3
    cursor.execute("SELECT * FROM candidates")
    rows = cursor.fetchall()
    print(f'All rows and columns: got {len(rows)} rows')
    for row in rows:
        print(row)

    # explicit selects with WHERE {{{3
    cursor.execute("SELECT * FROM candidates WHERE first_name = 'mike'")
    # cursor.execute("SELECT * FROM candidates WHERE LOWER(first_name) = 'mike'")
    rows = cursor.fetchall()
    print(f"Looking for 'mike': got {len(rows)} rows")
    for row in rows:
        print(row)

    # explicit select of specified column {{{3
    cursor.execute("SELECT first_name FROM candidates")
    rows = cursor.fetchall()
    print(f"Looking for first_name: got {len(rows)} rows")
    for row in rows:
        print(row)

    # create a table for the `contributors` {{{2
    cursor.execute(
        '''CREATE TABLE contributors (
              id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
              last_name TEXT,
              first_name TEXT,
              middle_name TEXT,
              street_1 TEXT,
              street_2 TEXT,
              city TEXT,
              state TEXT,
              zip TEXT, 
              amount FLOAT(7,3),
              date DATETIME,
              candidate_id INTEGER NOT NULL,
              FOREIGN KEY(candidate_id) REFERENCES candidates(id))'''
    )
    db.commit()  # commit the changes to the database

    # add contributors {{{2
    contributors = [
        (
            "Agee", "Steven", "", "549 Laurel Branch Road", "", "Floyd", "VA",
            int(24091), 500.0, '2007-06-30', 16
        ),
        (
            "Buck", "Jay", "K.", "1855 Old Willow Rd Unit 322", "",
            "Northfield", "IL", int(600932918), 200.0, '2007-09-12', 20
        ),
        (
            "Choe", "Hyeokchan", "", "207 Bridle Way", "", "Fort Lee", "NJ",
            int(70246302), -39.50, '2008-04-21', 32
        ),
    ]

    cursor.executemany(
        '''INSERT INTO contributors
    (last_name, first_name, middle_name, street_1, street_2, city, state, zip,
    amount, date, candidate_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
        contributors
    )
    db.commit()

    cursor.execute('SELECT last_name FROM contributors WHERE amount <= 200')
    for row in cursor.fetchall():
        print(row)

    # foreign key violation {{{2
    try:
        cursor.execute(
            '''INSERT INTO contributors
        (last_name, first_name, middle_name, street_1, street_2, city, state, zip,
        amount, date, candidate_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (
                "Buckler", "Steve", "", "24351 Armada Dr.", "", "Dana Point",
                "CA", int(926291), 50, '2007-07-30', 34
            )
        )
    except sqlite3.IntegrityError as e:
        # we expect this error and allow to pass such that we can close the
        # database in the next section
        print(e)
        pass

    # close database when done {{{2
    db.close()


# __main__ {{{1
if __name__ == "__main__":
    main()
