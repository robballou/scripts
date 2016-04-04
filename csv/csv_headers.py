#!/usr/bin/env python
import csv

with open('file.csv', 'rb') as original_file:
    data = csv.reader(original_file)
    for row in data:
        for item in row:
            print "%s" % item
        break
