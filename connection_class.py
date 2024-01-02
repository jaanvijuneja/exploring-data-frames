import mysql.connector
import pandas as pd

class sql_connector:
    def __init__(self, host_string, user_name, password, database):
        self.connection_strings = mysql.connector.connect(
        host=host_string,
        user=user_name,
        password=password,
        database=database)

    def sql_run_query(self, sql_query):

        with self.connection_strings.cursor() as cursor:
            cursor.execute(sql_query)
            self.connection_strings.commit()


    def get_dataframe(self, sql_query):
        
        with self.connection_strings.cursor() as cursor:
            cursor.execute(sql_query)
            data = cursor.fetchall()
            column_names = [column[0] for column in cursor.description]
            df = pd.DataFrame(data, columns=column_names)

        return df
