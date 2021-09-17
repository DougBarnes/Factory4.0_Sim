#!/usr/bin/python

"""factory_database.py: Connects to a postgreSQL data base to control HBW inventory. """

__author__      = "Doug Barnes"
__version__     = "1.0.0"
__maintainer__  = "Doug Barnes"
__email__       = "barn1855@vandals.uidaho.edu"
__status__      = "Production"

import psycopg2
from psycopg2 import Error

try:
    #### Connect to an existing database ####
    connection = psycopg2.connect(user="postgres",
                                  password="qwerty",
                                  host="localhost",
                                  database="factorydb")

    #### Create a cursor to perform database operations ####
    cursor = connection.cursor()

    #### SQL query to create a new table ####
    create_table_query = '''CREATE TABLE mobile
          (ID INT PRIMARY KEY     NOT NULL,
          MODEL           TEXT    NOT NULL,
          PRICE         REAL); '''

    #### Execute a command: this creates a new table ####
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")

    #### Print PostgreSQL details ####
    #print("PostgreSQL server information")
    #print(connection.get_dsn_parameters(), "\n")

    #### Executing a SQL query ####
    #cursor.execute("SELECT version();")

    #### Fetch result ####
    #record = cursor.fetchone()
    #print("You are connected to - ", record, "\n")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

#https://pynative.com/python-postgresql-tutorial/
#https://www.postgresqltutorial.com/postgresql-python/connect/