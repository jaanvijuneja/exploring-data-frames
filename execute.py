import functions


localhost = '127.0.0.1'
username = 'root'
password = 'Secret55'
database = 'companydb'

# sql_query = f"""
# INSERT INTO Employees (EmployeeID, Name, DepartmentID, ManagerID, HireDate) VALUES (7, 'Alex', 113, 119, '2024-02-21')
# """

# functions.sql_run_query(localhost, username, password, database, sql_query)


sql_query_df = f"""
select * from Employees
"""

result_df = functions.get_dataframe(localhost, username, password, database, sql_query_df)

print(result_df.head())
