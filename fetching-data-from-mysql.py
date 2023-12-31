#! /usr/bin/env python3
import mysql.connector

connection_strings = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Secret55",
    database="companydb"
)

cursor = connection_strings.cursor()

cursor.execute("SELECT * FROM Employees")

results = cursor.fetchall()
for row in results:
    print(row)

cursor.close()
connection_strings.close()

