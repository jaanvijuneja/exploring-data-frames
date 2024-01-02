from connection_class import sql_connector

localhost = '127.0.0.1'
username = 'root'
password = 'Secret55'
database = 'companydb'

mysql_connector = sql_connector(localhost, username, password, database)

# sql_query = f"""
# INSERT INTO Employees (EmployeeID, Name, DepartmentID, ManagerID, HireDate) VALUES (8, 'Alex', 114, 119, '2024-02-21')
# """

# mysql_connector.sql_run_query(sql_query)


sql_query_df = f"""
select * from Employees
"""

result_df = mysql_connector.get_dataframe(sql_query_df)

print(result_df.head(10))
