#!/usr/bin/python
# -*- coding: latin-1 -*-

import sqlite3 
import re

# open file
f = open("cities.txt")
lines = f.readlines()

# database connection
connection = sqlite3.connect("cities.db")
cursor = connection.cursor()
query = "SELECT * FROM cities WHERE name LIKE "


for line in lines:
    # remove any non-relevant characters
    name = re.sub("[^\wäöü. ]", "", line)   
    cursor.execute(query + "'" + name + "'")
    data = cursor.fetchall() 

    # pick first result if found
    if len(data) >= 1:
        print data[0][0]+","+data[0][1]+","+data[0][2]
    #else:
        #print name+",0,0"
        
