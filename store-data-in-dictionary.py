#! /home/jaanvi/.pyenv/versions/3.12.0/bin/python3.12
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

column_names = [desc[0] for desc in cursor.description]

dictionary_data = {}

# i = 1
# for row in results:
#    dictionary_data[i] = dict(zip(column_names, row))
#    i += 1


for row in results:
    row_dict = dict(zip(column_names, row))
    row_id = row_dict['EmployeeID']
    dictionary_data[row_id] = row_dict

print(dictionary_data)

cursor.close()
connection_strings.close()

