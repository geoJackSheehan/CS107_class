#!/usr/bin/env python3
# File       : exercise_1.py
# Description: PP11: SQLite3 and data processing in Python
# Copyright 2022 Harvard University. All Rights Reserved.
import sqlite3


class CandidateReader:
    """Iterable reader for presidential candidates data.

    Example:
    --------

    >>> nominees = CandidateReader("./data/candidates.txt")
    >>> len(nominees)
    17

    """

    def __init__(self, path, *, sep="|"):
        """
        Initialize presidential candidates reader.

        Parameters
        ----------
        path : str
            Path to data file.

        """
        self._data_path = path
        self._delimiter = sep
        with open(self._data_path, 'r') as raw:
            self._header = tuple(
                [item.strip() for item in next(raw).split(self._delimiter)]
            )
            self._candidates = []
            for line in raw:
                self._candidates.append(
                    tuple(
                        [
                            cdata.strip()
                            for cdata in line.split(self._delimiter)
                        ]
                    )
                )

    def __len__(self):
        """Number of candidates in data."""
        return len(self._candidates)

    def __iter__(self):
        """Data is iterable."""
        for candidate in self._candidates:
            yield candidate

    def get_header(self):
        """Get an iterable for data header items."""
        return self._header


def add_table(fname, table_name, cursor):
    """
    Add a new table to sqlite3 database.

    Add the data in the file `fname` to a new table with `table_name` to the
    `cursor` sqlite3 object. Column names are determined from the header
    associated to the data file.  If a table with `table_name` exists in the
    `cursor` object, the table will be dropped before a new table is added.

    Parameters
    ----------
    fname : str
        Path to data file.
    table_name : str
        Name of the new table.  Drop the table if it exists.
    cursor : sqlite3.Cursor
        SQLite3 cursor object.

    Notes
    -----
    The function replaces all occurrences of white space in file header items
    with underscore characters.

    """
    # drop table if it exists
    cursor.execute(f'DROP TABLE IF EXISTS {table_name}')

    # create data reader object
    nominees = CandidateReader(fname)

    # create new table
    # fields `id` and `party` are expected to be in the file header of the data,
    # other header items may be arbitrary and contain space.  If there are
    # spaces in header fields, they will be replaced below with underscores for
    # more robustness.
    type_map = {'id': 'INTEGER PRIMARY KEY NOT NULL', 'party': 'TEXT NOT NULL'}
    safe_fields = [item.replace(' ', '_') for item in nominees.get_header()]
    cmd = f"CREATE TABLE {table_name} ("
    for field in safe_fields:
        cmd += f"{field} {type_map.get(field, 'TEXT')},"
    cmd = cmd.strip(',') + ")"
    cursor.execute(cmd)  # add empty table

    # add nominees to table
    cmd = f"INSERT INTO {table_name} ("
    for field in safe_fields:
        cmd += f"{field},"
    cmd = cmd.strip(',') + ") VALUES (" + (len(safe_fields) *
                                           "?,").strip(',') + ")"
    cursor.executemany(cmd, nominees)  # nominees is iterable


if __name__ == "__main__":
    db = sqlite3.connect('presidential.db')

    # obtain a cursor object for the `db` database
    # https://www.python.org/dev/peps/pep-0249/#cursor-objects
    cursor = db.cursor()
    cursor.execute('PRAGMA foreign_keys=1')

    # add candidates from data file
    add_table("./data/candidates.txt", "candidates", cursor)
    db.commit()
    db.close()
