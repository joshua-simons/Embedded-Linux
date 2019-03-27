#!/usr/bin/python
#Import libraries needed
import sqlite3
import sys
import json

#Connect to the database
con = sqlite3.connect('../../log/templog.db')
cur = con.cursor()

print("Content-type:text/json;charset=utf-8\n")
con.row_factory = sqlite3.Row
cur.execute("SELECT * FROM templog")
dataset = cur.fetchall()
chartJSON = []
for row in dataset:
	chartJSON.append({"Date": row[0], "Temperature": float(row[1])})
print(json.dumps(chartJSON))
con.close()
exit(0)
