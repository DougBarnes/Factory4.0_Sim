#!/usr/bin/python

"""factory_database.py: Connects to a postgreSQL database 
   to create and fill HBW inventory. """
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

    # HBW (factory_t)
    #|1||2||3|
    #|4||5||6|
    #|7||8||9|

    #### SQL query to create a new table ####
    #create_table_query = '''CREATE TABLE factory_t
          #(LOCATION INT PRIMARY KEY     NOT NULL,
          #COLOR_ID           TEXT       NOT NULL,
          #DISK_STORED        BOOL       NOT NULL,
          #PALLET_STORED      BOOL       NOT NULL); '''

    #### Execute a command: this creates a new table ####
    #cursor.execute(create_table_query)
    #connection.commit()
    #print("Table created successfully in PostgreSQL ")

    # Executing a SQL query to insert data into  table
    '''insert_query = """ INSERT INTO factory_t (LOCATION, COLOR_ID, DISK_STORED, PALLET_STORED) VALUES (1, 'Red01', True, True)"""
    cursor.execute(insert_query)
    connection.commit()
    insert_query = """ INSERT INTO factory_t (LOCATION, COLOR_ID, DISK_STORED, PALLET_STORED) VALUES (2, 'Red02', True, True)"""
    cursor.execute(insert_query)
    connection.commit()
    insert_query = """ INSERT INTO factory_t (LOCATION, COLOR_ID, DISK_STORED, PALLET_STORED) VALUES (3, 'Red03', True, True)"""
    cursor.execute(insert_query)
    connection.commit()
    insert_query = """ INSERT INTO factory_t (LOCATION, COLOR_ID, DISK_STORED, PALLET_STORED) VALUES (4, 'Blue01', True, True)"""
    cursor.execute(insert_query)
    connection.commit()
    insert_query = """ INSERT INTO factory_t (LOCATION, COLOR_ID, DISK_STORED, PALLET_STORED) VALUES (5, 'Blue02', True, True)"""
    cursor.execute(insert_query)
    connection.commit()
    insert_query = """ INSERT INTO factory_t (LOCATION, COLOR_ID, DISK_STORED, PALLET_STORED) VALUES (6, 'Blue03', True, True)"""
    cursor.execute(insert_query)
    connection.commit()
    insert_query = """ INSERT INTO factory_t (LOCATION, COLOR_ID, DISK_STORED, PALLET_STORED) VALUES (7, 'White01', True, True)"""
    cursor.execute(insert_query)
    connection.commit()
    insert_query = """ INSERT INTO factory_t (LOCATION, COLOR_ID, DISK_STORED, PALLET_STORED) VALUES (8, 'White02', True, True)"""
    cursor.execute(insert_query)
    connection.commit()
    insert_query = """ INSERT INTO factory_t (LOCATION, COLOR_ID, DISK_STORED, PALLET_STORED) VALUES (9, 'White03', True, True)"""
    cursor.execute(insert_query)
    connection.commit()
    print("Record inserted successfully") '''

    # Fetch result
    cursor.execute("SELECT * FROM factory_t")
    record = cursor.fetchall()
    print("Result ", record)

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

#https://pynative.com/python-postgresql-tutorial/
#https://www.postgresqltutorial.com/postgresql-python/connect/