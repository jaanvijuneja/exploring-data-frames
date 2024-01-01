#! /home/jaanvi/.pyenv/versions/3.12.0/bin/python3.12
import mysql.connector
import pandas as pandas_py

connection_strings = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Secret55",
    database="companydb"
)

cursor = connection_strings.cursor()

cursor.execute("SELECT * FROM Employees")

results = cursor.fetchall()

column_names = [desc[0] for desc in cursor.description]

dictionary_data = {}

for row in results:
    row_dict = dict(zip(column_names, row))
    row_id = row_dict['EmployeeID']
    dictionary_data[row_id] = row_dict

df = pandas_py.DataFrame(dictionary_data)

# Viewing the Dataframe
print("Original Dataframe:")
print(df)

cursor.close()
connection_strings.close()

