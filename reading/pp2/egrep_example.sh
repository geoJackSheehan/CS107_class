#!/bin/bash
echo $(grep '\d+' sample.txt)
echo $(grep -E "\d+" sample.txt)
echo $(egrep "\d+" sample.txt)
