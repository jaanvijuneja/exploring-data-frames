import mysql.connector
import pandas as pd

def sql_run_query(host_string, user_name, password, database, sql_query):
    connection_strings = mysql.connector.connect(
    host=host_string,
    user=user_name,
    password=password,
    database=database)

    with connection_strings.cursor() as cursor:
        cursor.execute(sql_query)
        connection_strings.commit()


def get_dataframe(host_string, user_name, password, database, sql_query):
    connection_strings = mysql.connector.connect(
    host=host_string,
    user=user_name,
    password=password,
    database=database)

    with connection_strings.cursor() as cursor:
        cursor.execute(sql_query)
        data = cursor.fetchall()
        column_names = [column[0] for column in cursor.description]
        df = pd.DataFrame(data, columns=column_names)

    return df
