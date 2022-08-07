
# # Task 1 - FitbitDataset
# 1. Read fitbit dataset in pandas, mysql and Mongodb
# 2. While creating a table in mysql, use automation to create table in mysql. use csvkit library to automate the task
# 3. Convert all the dates available in dataset to timestamp format in pandas and in sql convert it into dateformat
# 4. Find out unique id's in data
# 5. Find out Active id dataset
# 6. How many of them have not logged there activity, find out their ids
# 7. Find out who is laziest person id in the dataset
# 8. Search on internet how much calories are burn is required for a healthy person and find out how many person we have in our data
# 9. How many are not active regularly
# 10. Third most active person in dataset, find out using pandas and sql
# 11. 5th most laziest person in the dataset
# 12. what is a total cumulative clories burn for a person

import mysql.connector as connection
import pandas as pd
import csv
import csvkit

def mysql_db_connection():

    sql_conn_flag = True
    while sql_conn_flag:
        choice1 = int(input("\nSQL Operataions\n1.Able to connect to MYSQL \n2.Create script of table Fitbit \n3.Create a table fitbit in MYSQL\n4. Do a bulk load fitbit dataset in MYSQL\n\nEnter Your Choice :"))
        if choice1   == 1:
            connect_db()
        elif choice1 == 2:
            create_table_script()
        elif choice1 == 3:
            create_mysql_table()
        elif choice1 == 4:
            load_mysql_table()
        else:
            print("Return to Main Operations")
            sql_conn_flag = False


def connect_db():
    try:
        mydb = connection.connect(host="localhost",database= "projectdb", user="devuser", passwd="Logitech1234#", use_pure=True)
        show_query = "SHOW DATABASES"
        print("we are in connect_db")
        cursor = mydb.cursor()  # create a cursor to execute queries
        cursor.execute(show_query)
        print("able to connect to MYSQL DATABASE")
        return(mydb)
    except Exception as e:
            mydb.close()
            return (str(e))

def create_table_script():
    try:
        import os
        os.popen('"csvsql --dialect mysql - -snifflimit 100000 "D:\Study\Data Science\Python\ineuron\Data_Set\FitBit_Data.csv" > "D:\Study\Data Science\Python\ineuron\Data_Set\fitbit_output.sql"')
    except Exception as e:
            print(f"Error in create_table_Script {e}")


def create_mysql_table():
    try:
        mydb = connection.connect(host="localhost", user="devuser", passwd="Logitech1234#", use_pure=True)

        cursor = mydb.cursor()  # create a cursor to execute queries
        use_db_command = "USE projectdb"
        cursor.execute(use_db_command)
        # Open and read the file as a single buffer
        fd = open('D:\Study\Data Science\Python\ineuron\Data_Set\\sql_fitbit.sql', 'r')
        sqlFile = fd.read()
        print(sqlFile)
        fd.close()
        # In case of multiple sql commands in file we can apply below approach
        table_create_command = sqlFile.split(';')
        for command in table_create_command:
            print(command)
            cursor.execute(command)
        # table_create_command = sqlFile
        # print(table_create_command)

        # cursor.execute(table_create_command)
        print("connection success")
    except Exception as e:
            print(str(e))
            mydb.close()

def load_mysql_table():
    try:
        mydb = connection.connect(host="localhost", user="devuser", passwd="Logitech1234#", use_pure=True)
        cursor = mydb.cursor()  # create a cursor to execute queries
        use_db_command = "USE projectdb"
        cursor.execute(use_db_command)
        load_data_query = "load data  infile 'D://Study//Data Science//Python//ineuron//Data_Set//FitBit_Data.csv' into table FitBit_Data fields terminated by ','  Enclosed by '" "'  IGNORE 1 ROWS;"
        cursor.execute(load_data_query)
        print("upload success")
        mydb.commit()
    except Exception as e:
            mydb.close()
            print(f"upload fail : {e}")
