#!/usr/bin/env bash
# File       : format_code.sh
# Created    : Sat Sep 11 2021 11:51:15 AM (-0400)
# Author     : Fabian Wermelinger
# Description: Maintenance script to format python code.  Formatting rules are
#              defined in .style.yapf at the project root.
# Copyright 2021 Harvard University. All Rights Reserved.

yapf --in-place --recursive --parallel .
