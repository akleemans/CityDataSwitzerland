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
    # without regex
    #name = line.replace("\n","")
    #name = name[:len(name)-2] + "%"

    name = re.sub("[^\wäöü. ]", "", line)   

    cursor.execute(query + "'" + name + "'")
    data = cursor.fetchall() 

    if len(data) >= 1:
        print name, "|", data[0][0], data[0][1], data[0][2]
    #if len(data) == 0:
        #print "no results for", name
