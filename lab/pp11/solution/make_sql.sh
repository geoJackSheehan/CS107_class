#!/usr/bin/env bash
# File       : make_sql.sh
# Description: Convert SQLite3 database to SQL
# Copyright 2022 Harvard University. All Rights Reserved.
set -e
python exercise_1.py
sqlite3 presidential.db .dump >presidential.sql
